"""
=============================================================
  Construction de la Master Table
  Chargement et fusion des tables de données
  À importer via : from main_import import creer_master_table
=============================================================
"""

import pandas as pd

# Paramètres de lecture robustes pour Linux/Mac
PARAMS_BASE   = dict(encoding="latin-1")
PARAMS_ROBUST = dict(encoding="latin-1", sep=None, engine="python", on_bad_lines="skip")

# ============================================================
# GROUPES DE MARQUES
# ============================================================

GROUPES_MARQUES = {
    "Généraliste FR":  ["Peugeot", "Citroën", "Renault", "Dacia", "DS"],
    "Généraliste ETR": ["Volkswagen", "Toyota", "Nissan", "Ford", "Opel",
                        "Suzuki", "Kia", "Hyundai", "Fiat", "Seat", "Skoda",
                        "Mitsubishi", "Jeep", "Mazda", "Honda", "MG", "Cupra"],
    "Premium":         ["Audi", "Mercedes", "BMW", "Volvo", "Mini", "Jaguar",
                        "Land Rover", "Lexus", "Alfa Romeo", "Lynk&Co"],
    "Élec/Innovant":   ["Tesla", "Smart"],
}

def attribuer_groupe_marque(marque):
    if pd.isna(marque):
        return "Inconnu"
    for groupe, marques in GROUPES_MARQUES.items():
        if marque in marques:
            return groupe
    return "Autre"


# ============================================================
# CONSTRUCTION DE LA MASTER TABLE
# ============================================================

def creer_master_table(dossier="data"):
    """
    Charge les 5 tables et les fusionne en une master table.
    Reproduit exactement la logique du prof avec corrections Linux.
    Retourne le DataFrame final prêt à l'emploi.
    """

    # --- Chargement ---
    df_client           = pd.read_csv(f"{dossier}/table_client.csv",          **PARAMS_BASE)
    df_commande_reprise = pd.read_csv(f"{dossier}/table_commande_reprise.csv", **PARAMS_BASE)
    df_vehicule         = pd.read_csv(f"{dossier}/table_vehicule.csv",         **PARAMS_ROBUST)
    df_financement      = pd.read_csv(f"{dossier}/table_financement.csv",      **PARAMS_BASE)
    df_nearest_agency   = pd.read_csv(f"{dossier}/table_nearest_agency.csv",   **PARAMS_BASE)

    print(f"  [OK] table_client           : {df_client.shape}")
    print(f"  [OK] table_commande_reprise : {df_commande_reprise.shape}")
    print(f"  [OK] table_vehicule         : {df_vehicule.shape}")
    print(f"  [OK] table_financement      : {df_financement.shape}")
    print(f"  [OK] table_nearest_agency   : {df_nearest_agency.shape}")

    # --- Normalisation Lynk & Co ---
    df_vehicule["VEHICULE_MARQUE"] = (
        df_vehicule["VEHICULE_MARQUE"].str.strip().replace("Lynk & Co", "Lynk&Co")
    )

    # --- Étape 2 : Déduplication clients ---
    df_client = df_client.drop_duplicates(subset="ID_LEAD")

    # --- Étape 3 : Merge commande_reprise + client ---
    df = pd.merge(df_commande_reprise, df_client,
                  left_on="LEAD_ID", right_on="ID_LEAD", how="left")

    # --- Étape 4 : Calcul de l'âge depuis DATE_PANIER ---
    df["DATE_PANIER"]    = pd.to_datetime(df["DATE_PANIER"], errors="coerce")
    df["AGE"]            = df["DATE_PANIER"].dt.year - df["YEAR_NAISSANCE"]
    df["MOIS_COMMANDE"]  = df["DATE_PANIER"].dt.month
    df["ANNEE_COMMANDE"] = df["DATE_PANIER"].dt.year

    # --- Étape 5 : Split commande / reprise ---
    df_reprise  = df[df["TYPE_PANIER"] == "Reprise"]
    df_commande = df[df["TYPE_PANIER"] == "Commande"]

    # --- Étape 6 : Merge + véhicule ---
    df_commande_vehicule = pd.merge(df_commande, df_vehicule,
                                    on="VEHICULE_ID", how="left")

    # --- Étape 7 : Merge + financement (double clé) ---
    df_commande_vehicule_financement = pd.merge(
        df_commande_vehicule, df_financement,
        on=["LEAD_ID", "VEHICULE_ID"], how="left"
    )

    # --- Étape 8 : Merge + agences ---
    df_master = pd.merge(
        df_commande_vehicule_financement, df_nearest_agency,
        left_on="CODE_POSTAL", right_on="ZIP_CODE", how="left"
    )

    df_master["FI_TYPE"] = df_master["FI_TYPE"].fillna("Sans financement")

    # --- Nettoyage villes ---
    if "VILLE" in df_master.columns:
        df_master["VILLE"] = df_master["VILLE"].str.strip().str.upper()
        df_master["VILLE"] = df_master["VILLE"].replace(
            ["NON REPONSE", "NON_REPONSE", "X", "NR", "N/A", "", "INCONNU"], pd.NA
        )

    # --- Filtrage âges aberrants ---
    df_master = df_master[(df_master["AGE"] >= 18) & (df_master["AGE"] <= 100)]

    # --- Tranches d'âge ---
    bins   = [18, 30, 40, 50, 60, 70, 100]
    labels = ["18-30", "31-40", "41-50", "51-60", "61-70", "70+"]
    df_master["TRANCHE_AGE"] = pd.cut(df_master["AGE"], bins=bins, labels=labels, right=True)

    # --- Groupe de marque ---
    df_master["GROUPE_MARQUE"] = df_master["VEHICULE_MARQUE"].apply(attribuer_groupe_marque)

    print(f"\n  MASTER TABLE : {df_master.shape[0]} lignes × {df_master.shape[1]} colonnes")
    print(f"  Commandes    : {len(df_commande)}")
    print(f"  Reprises     : {len(df_reprise)}")

    # --- Région à partir du code postal ---
    def cp_to_region(cp):
        try:
            dep = str(int(cp)).zfill(5)[:2]
        except:
            return "Inconnu"
        mapping = {
            # Île-de-France
            "75": "Île-de-France", "77": "Île-de-France", "78": "Île-de-France",
            "91": "Île-de-France", "92": "Île-de-France", "93": "Île-de-France",
            "94": "Île-de-France", "95": "Île-de-France",
            # PACA
            "04": "PACA", "05": "PACA", "06": "PACA",
            "13": "PACA", "83": "PACA", "84": "PACA",
            # Auvergne-Rhône-Alpes
            "01": "Auvergne-Rhône-Alpes", "03": "Auvergne-Rhône-Alpes",
            "07": "Auvergne-Rhône-Alpes", "15": "Auvergne-Rhône-Alpes",
            "26": "Auvergne-Rhône-Alpes", "38": "Auvergne-Rhône-Alpes",
            "42": "Auvergne-Rhône-Alpes", "43": "Auvergne-Rhône-Alpes",
            "63": "Auvergne-Rhône-Alpes", "69": "Auvergne-Rhône-Alpes",
            "73": "Auvergne-Rhône-Alpes", "74": "Auvergne-Rhône-Alpes",
            # Nouvelle-Aquitaine
            "16": "Nouvelle-Aquitaine", "17": "Nouvelle-Aquitaine", "19": "Nouvelle-Aquitaine",
            "23": "Nouvelle-Aquitaine", "24": "Nouvelle-Aquitaine", "33": "Nouvelle-Aquitaine",
            "40": "Nouvelle-Aquitaine", "47": "Nouvelle-Aquitaine", "64": "Nouvelle-Aquitaine",
            "79": "Nouvelle-Aquitaine", "86": "Nouvelle-Aquitaine", "87": "Nouvelle-Aquitaine",
            # Occitanie
            "09": "Occitanie", "11": "Occitanie", "12": "Occitanie", "30": "Occitanie",
            "31": "Occitanie", "32": "Occitanie", "34": "Occitanie", "46": "Occitanie",
            "48": "Occitanie", "65": "Occitanie", "66": "Occitanie", "81": "Occitanie", "82": "Occitanie",
            # Hauts-de-France
            "02": "Hauts-de-France", "59": "Hauts-de-France", "60": "Hauts-de-France",
            "62": "Hauts-de-France", "80": "Hauts-de-France",
            # Grand Est
            "08": "Grand Est", "10": "Grand Est", "51": "Grand Est", "52": "Grand Est",
            "54": "Grand Est", "55": "Grand Est", "57": "Grand Est", "67": "Grand Est",
            "68": "Grand Est", "88": "Grand Est",
            # Normandie
            "14": "Normandie", "27": "Normandie", "50": "Normandie", "61": "Normandie", "76": "Normandie",
            # Bretagne
            "22": "Bretagne", "29": "Bretagne", "35": "Bretagne", "56": "Bretagne",
            # Pays de la Loire
            "44": "Pays de la Loire", "49": "Pays de la Loire", "53": "Pays de la Loire",
            "72": "Pays de la Loire", "85": "Pays de la Loire",
            # Centre-Val de Loire
            "18": "Centre-Val de Loire", "28": "Centre-Val de Loire", "36": "Centre-Val de Loire",
            "37": "Centre-Val de Loire", "41": "Centre-Val de Loire", "45": "Centre-Val de Loire",
            # Bourgogne-Franche-Comté
            "21": "Bourgogne-Franche-Comté", "25": "Bourgogne-Franche-Comté",
            "39": "Bourgogne-Franche-Comté", "58": "Bourgogne-Franche-Comté",
            "70": "Bourgogne-Franche-Comté", "71": "Bourgogne-Franche-Comté",
            "89": "Bourgogne-Franche-Comté", "90": "Bourgogne-Franche-Comté",
            # Corse
            "2A": "Corse", "2B": "Corse",
            # DOM-TOM
            "97": "DOM-TOM", "98": "DOM-TOM",
        }
        return mapping.get(dep, "Inconnu")

    df_master["REGION"] = df_master["CODE_POSTAL"].apply(cp_to_region)

    return df_master


# ============================================================
# LANCEMENT DIRECT (vérification)
# ============================================================

if __name__ == "__main__":
    print("\n========================================")
    print("  MASTER TABLE — Vérification")
    print("========================================\n")

    table = creer_master_table(dossier="data")

    print("\nColonnes :")
    print(table.columns.tolist())
    print("\nTranches d'âge :")
    print(table["TRANCHE_AGE"].value_counts().sort_index())
