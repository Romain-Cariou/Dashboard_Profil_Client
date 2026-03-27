"""
=============================================================
  Application Streamlit
  Analyse du profil des clients
=============================================================
  Lancement : streamlit run app.py
=============================================================
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from main_import import creer_master_table

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Dashboard — Profil clients",
    page_icon="🚗",
    layout="wide"
)

COULEUR_PRINCIPALE = "#2E86AB"
COULEUR_SECONDAIRE = "#E84855"
COULEURS           = ["#2E86AB", "#E84855", "#F4A261", "#57CC99", "#9B5DE5", "#FEE440"]
ORDRE_TRANCHES     = ["18-30", "31-40", "41-50", "51-60", "61-70", "70+"]
PCT_FMT            = FuncFormatter(lambda x, _: f"{x:.0f}%")
MOIS_FR            = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
                       "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# ============================================================
# CHARGEMENT
# ============================================================

@st.cache_data
def charger_donnees():
    return creer_master_table(dossier="data")


# ============================================================
# PAGE 0 — ACCUEIL
# ============================================================

def page_accueil():
    # Titre principal
    st.markdown("""
    <h1 style='text-align: center; color: #2E86AB; font-size: 3em;'>
        🚗 Bienvenue sur le Dashboard Clients
    </h1>
    <h3 style='text-align: center; color: #555;'>
        Analyse du profil des clients — Projet Datamining 2025/2026
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Présentation entreprise
    st.header("🏢 Présentation de l'entreprise")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        Notre client est le **leader européen de la vente en ligne de voitures d'occasion reconditionnées**,
        pionnier du e-commerce automobile en France.

        Pionnière du e-commerce automobile en France, l'entreprise s'est imposée en révolutionnant
        l'achat de véhicules d'occasion grâce à une approche 100% digitale, combinée à un réseau
        d'agences physiques en pleine expansion.

        L'entreprise est cotée en bourse et fait partie d'un grand groupe automobile européen.
        """)
        st.markdown("<br>", unsafe_allow_html=True)
        # Logo retiré pour anonymisation

    with col2:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #2E86AB;'>X Mds €</h2>
            <p>Chiffre d'affaires annuel</p>
            <h2 style='color: #2E86AB;'>XXX 000</h2>
            <p>Véhicules vendus / an</p>
            <h2 style='color: #2E86AB;'>X 000+</h2>
            <p>Collaborateurs</p>
            <h2 style='color: #2E86AB;'>6</h2>
            <p>Pays en Europe</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Timeline
    st.header("📅 Grandes étapes")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 15px; border-radius: 8px; text-align: center;'>
            <h3 style='color: #2E86AB;'>Années XXXX</h3>
            <p>Fondation de l'entreprise par ses fondateurs</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 15px; border-radius: 8px; text-align: center;'>
            <h3 style='color: #2E86AB;'>Années XXXX</h3>
            <p>Lancement de l'offre véhicules d'occasion reconditionnés</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 15px; border-radius: 8px; text-align: center;'>
            <h3 style='color: #2E86AB;'>Années XXXX</h3>
            <p>Introduction en bourse sur un marché boursier européen</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 15px; border-radius: 8px; text-align: center;'>
            <h3 style='color: #2E86AB;'>Aujourd'hui</h3>
            <p>CA de X Mds € — forte croissance annuelle</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Présentation du projet
    st.header("🎯 Présentation du projet")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Contexte
        L'entreprise souhaite mieux comprendre le **profil de ses clients** pour optimiser
        sa stratégie marketing. Ce projet s'appuie sur des **données internes** issues de
        6 tables : commandes, clients, véhicules, financement, navigation web et agences.

        ### Objectifs
        - 📊 **Analyser** les données internes pour identifier les comportements clients
        - 🔗 **Enrichir** avec des données externes si nécessaire
        - 💻 **Développer** une application interactive pour visualiser les résultats
        - 📣 **Proposer** des recommandations marketing à l'entreprise
        """)

    with col2:
        st.markdown("""
        ### Structure de l'application
        """)
        st.markdown("""
        | Page | Contenu |
        |------|---------|
        | 🏠 Accueil | Présentation entreprise & projet |
        | 📈 Vue Globale | KPIs, âge, genre, villes, saisonnalité |
        | 📊 Hypothèse 1 | L'âge impacte-t-il les choix clients ? |
        | 📊 Hypothèse 2 | Le genre impacte-t-il les choix clients ? |
        | 📊 Hypothèse 3 | La région impacte-t-elle les choix clients ? |
        | 📊 Tests Statistiques | Validation statistique des hypothèses (Chi²) |
        | 📊 AFDM - Analyse| Relations entre variables |
        | 💡 Recommandations | Recommandations Marketing suite aux analyses |
        """)

        st.markdown("""
        ### Données analysées
        - 📦 **4 212** commandes sur une période de 5 mois
        - 👥 **4 212** clients uniques
        - 🚗 **4 212** véhicules référencés
        """)

    st.markdown("---")
    st.markdown("""
    <p style='text-align: center; color: #aaa; font-size: 0.9em;'>
        Projet Datamining M1 — 2025/2026 | Données confidentielles
    </p>
    """, unsafe_allow_html=True)


# ============================================================
# PAGE 1 — GLOBAL
# ============================================================

def page_global(df):
    import plotly.graph_objects as go
    import plotly.express as px

    st.title("📈 Vue Globale — Profil des clients")
    st.markdown("---")

    clients_uniques = df.drop_duplicates("LEAD_ID")
    nb_commandes = len(df)
    nb_clients   = df["LEAD_ID"].nunique()
    age_moyen    = clients_uniques["AGE"].mean()
    age_median   = clients_uniques["AGE"].median()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("📦 Commandes",        f"{nb_commandes:,}")
    col2.metric("👥 Clients uniques",   f"{nb_clients:,}")
    col3.metric("📅 Âge moyen",        f"{age_moyen:.1f} ans")
    col4.metric("📅 Âge médian",       f"{age_median:.0f} ans")
    col5.metric("👤 Genre majoritaire",
                "Hommes" if clients_uniques["GENDER"].value_counts().index[0] == "H" else "Femmes"
                if "GENDER" in df.columns else "N/A")

    st.markdown("---")

    # --- Âge + Genre ---
    col_g1, col_g2 = st.columns([2, 1])

    with col_g1:
        st.subheader("Répartition des clients par âge")
        ages = clients_uniques["AGE"].dropna()
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=ages, nbinsx=25,
            marker_color=COULEUR_PRINCIPALE, opacity=0.85,
            hovertemplate="Âge : %{x}<br>Nombre : %{y}<extra></extra>",
        ))
        fig.add_vline(x=age_moyen, line_dash="dash", line_color=COULEUR_SECONDAIRE,
                      annotation_text=f"Moyenne : {age_moyen:.1f} ans",
                      annotation_position="top right")
        fig.update_layout(
            xaxis_title="Âge", yaxis_title="Nombre de clients",
            plot_bgcolor="white", height=350,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        st.info(f"💡 L'âge moyen est de **{age_moyen:.1f} ans** (médiane : {age_median:.0f} ans). "
                f"La clientèle est majoritairement mature, avec un pic entre 35 et 60 ans.")

    with col_g2:
        st.subheader("Répartition Homme / Femme")
        genre_counts = clients_uniques["GENDER"].value_counts()
        fig = go.Figure(go.Bar(
            x=["Hommes", "Femmes"],
            y=[genre_counts.get("H", 0), genre_counts.get("F", 0)],
            marker_color=[COULEUR_PRINCIPALE, COULEUR_SECONDAIRE],
            hovertemplate="%{x}<br>Effectif : %{y}<extra></extra>",
        ))
        fig.update_layout(
            yaxis_title="Nombre de clients",
            plot_bgcolor="white", height=350,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        pct_h = genre_counts.get("H", 0) / genre_counts.sum() * 100
        st.info(f"💡 Clientèle majoritairement masculine (**{pct_h:.1f}%** d'hommes).")

    st.markdown("---")

    # --- Commandes par mois + Top villes ---
    col_g3, col_g4 = st.columns([2, 1])

    with col_g3:
        st.subheader("Volume de commandes par mois")
        commandes_mois = df.groupby("MOIS_COMMANDE").size().reset_index(name="nb")
        commandes_mois["mois_label"] = commandes_mois["MOIS_COMMANDE"].apply(lambda m: MOIS_FR[m - 1])
        fig = go.Figure(go.Bar(
            x=commandes_mois["mois_label"],
            y=commandes_mois["nb"],
            marker_color=COULEUR_PRINCIPALE,
            hovertemplate="%{x}<br>Commandes : %{y}<extra></extra>",
        ))
        fig.update_layout(
            xaxis_title="", yaxis_title="Nombre de commandes",
            plot_bgcolor="white", height=350,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        mois_max = MOIS_FR[commandes_mois.set_index("MOIS_COMMANDE")["nb"].idxmax() - 1]
        st.info(f"💡 Pic de commandes en **{mois_max}**, pas de creux identifiés sur cette période.")

    with col_g4:
        st.subheader("Top 10 villes clientes")
        top_villes = clients_uniques["VILLE"].value_counts().head(10).reset_index()
        top_villes.columns = ["Ville", "Nb"]
        fig = go.Figure(go.Bar(
            x=top_villes["Nb"][::-1],
            y=top_villes["Ville"][::-1],
            orientation="h",
            marker_color=COULEUR_PRINCIPALE,
            hovertemplate="%{y}<br>Clients : %{x}<extra></extra>",
        ))
        fig.update_layout(
            xaxis_title="Nombre de clients",
            plot_bgcolor="white", height=380,
        )
        fig.update_xaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        st.info(f"💡 **{top_villes['Ville'].iloc[0]}** est la ville la plus représentée.")

    st.markdown("---")

    # --- Financement + Neuf/Occasion ---
    col_g5, col_g6 = st.columns(2)

    with col_g5:
        st.subheader("Mode de financement")
        fi_counts = df["FI_TYPE"].value_counts().reset_index()
        fi_counts.columns = ["Financement", "Nb"]
        fig = go.Figure(go.Bar(
            x=fi_counts["Financement"],
            y=fi_counts["Nb"],
            marker_color=COULEURS[:len(fi_counts)],
            hovertemplate="%{x}<br>Effectif : %{y}<extra></extra>",
        ))
        fig.update_layout(
            yaxis_title="Nombre de commandes",
            plot_bgcolor="white", height=350,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        pct_sf = df["FI_TYPE"].value_counts(normalize=True).get("Sans financement", 0) * 100
        st.info(f"💡 **{pct_sf:.1f}%** des clients achètent sans financement.")

    with col_g6:
        st.subheader("Neuf vs Occasion")
        type_counts = df["VEHICULE_TYPE"].value_counts().sort_index()
        fig = go.Figure(go.Bar(
            x=["Véhicule Neuf", "Véhicule Occasion"],
            y=[type_counts.get("VN", 0), type_counts.get("VO", 0)],
            marker_color=[COULEUR_PRINCIPALE, COULEUR_SECONDAIRE],
            hovertemplate="%{x}<br>Effectif : %{y}<extra></extra>",
        ))
        fig.update_layout(
            yaxis_title="Nombre de commandes",
            plot_bgcolor="white", height=350,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)
        pct_vo = type_counts.get("VO", 0) / type_counts.sum() * 100
        st.info(f"La majorité des clients achètent des **véhicules d'occasion** (**{pct_vo:.1f}%**).")


# ============================================================
# PAGE 2 — HYPOTHÈSE 1 : IMPACT DE L'ÂGE
# ============================================================

def page_hypothese_age(df):
    import plotly.graph_objects as go

    ORDRE_FINANCEMENT    = ["Crédit", "LOA", "Sans financement"]
    COULEURS_FINANCEMENT = {"Crédit": "#2E86AB", "LOA": "#E84855", "Sans financement": "#F4A261"}
    LABELS_MAP           = {"VN": "Véhicule Neuf", "VO": "Véhicule Occasion"}

    st.title("📊 Hypothèse 1 — L'âge impacte-t-il les choix des clients ?")
    st.markdown("""
    > **Hypothèse** : L'âge du client influence ses choix en matière de véhicule
    > (neuf/occasion, catégorie, groupe de marque) et mode de financement.
    """)
    st.markdown("---")

    def boxplot_plotly(df, col):
        """Boxplot interactif Plotly — distribution de l'âge par modalité."""
        if col not in df.columns:
            return
        modalites = df[col].dropna().unique().tolist()
        if col == "FI_TYPE":
            modalites = [m for m in ORDRE_FINANCEMENT if m in modalites]

        fig = go.Figure()
        for m, couleur in zip(modalites, COULEURS * 10):
            label = LABELS_MAP.get(m, m)
            data  = df[df[col] == m]["AGE"].dropna()
            fig.add_trace(go.Box(
                y=data, name=label,
                marker_color=couleur,
                boxmean=True,
                hovertemplate=f"<b>{label}</b><br>Âge : %{{y}}<extra></extra>",
            ))
        fig.update_layout(
            yaxis_title="Âge", showlegend=False,
            plot_bgcolor="white", height=380,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)

    def barres_plotly(df, col, titre, legende_titre):
        """Barres empilées interactives Plotly — % par tranche d'âge."""
        if col not in df.columns:
            return
        pivot_n = (
            df.groupby(["TRANCHE_AGE", col], observed=True)
            .size().unstack(fill_value=0)
        )
        pivot_n = pivot_n.reindex(ORDRE_TRANCHES).dropna(how="all")
        if col == "FI_TYPE":
            pivot_n = pivot_n[[c for c in ORDRE_FINANCEMENT if c in pivot_n.columns]]
        pivot_pct = pivot_n.div(pivot_n.sum(axis=1), axis=0) * 100
        pivot_pct.columns = [LABELS_MAP.get(c, c) for c in pivot_pct.columns]
        pivot_n.columns   = [LABELS_MAP.get(c, c) for c in pivot_n.columns]

        fig = go.Figure()
        for i, modalite in enumerate(pivot_pct.columns):
            if col == "FI_TYPE":
                couleur = COULEURS_FINANCEMENT.get(modalite, COULEURS[i])
            else:
                couleur = COULEURS[i % len(COULEURS)]
            fig.add_trace(go.Bar(
                name=modalite,
                x=pivot_pct.index.tolist(),
                y=pivot_pct[modalite].round(1),
                marker_color=couleur,
                customdata=pivot_n[modalite].values,
                hovertemplate=f"<b>%{{x}}</b><br>{modalite}<br>"
                              "Part : %{y:.1f}%<br>Effectif : %{customdata}<extra></extra>",
            ))
        fig.update_layout(
            title=dict(text=titre, font=dict(size=13)),
            barmode="stack",
            xaxis_title="Tranche d'âge",
            yaxis=dict(title="% des commandes", ticksuffix="%"),
            legend=dict(title=legende_titre),
            plot_bgcolor="white", height=420,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)

    def tableau_stats(df, col):
        if col not in df.columns:
            return
        stats = (
            df.groupby(col, observed=True)["AGE"]
            .agg(Moyenne="mean", Médiane="median", Nombre="count")
            .round(1).reset_index().sort_values("Moyenne")
        )
        stats[col] = stats[col].map(lambda x: LABELS_MAP.get(x, x))
        stats = stats.rename(columns={col: "Modalité"})
        st.dataframe(stats, use_container_width=True, hide_index=True)

    themes = [
        ("VEHICULE_TYPE",      "Neuf vs Occasion",     "Type de véhicule",
         "Les jeunes (18-40 ans) achètent majoritairement de l'**occasion** (~70%), "
         "à partir de la cinquantaine les clients basculent majoritairement vers le **neuf**. L'âge impacte clairement ce choix."),
        ("VEHICULE_CATEGORIE", "Catégorie de véhicule", "Catégorie",
         "Les 18-30 ans privilégient les **citadines**, tandis que les 61+ préfèrent les **4x4/SUV**. "
         "Tendance très nette entre jeunes et seniors."),
        ("GROUPE_MARQUE",      "Groupe de marque",      "Groupe de marque",
         "Le **Généraliste Français** domine toutes les tranches. Les 30-50 ans commencent légèrement "
         "à acheter des véhicules **Électrique/Innovant** (Tesla, Smart)."),
        ("FI_TYPE",            "Type de financement",   "Financement",
         "La **LOA** (location avec option d'achat) progresse avec l'âge (42% chez 18-30 → 75% chez 70+). "
         "Les seniors préfèrent la location longue durée au crédit classique."),
    ]

    for col, titre, legende, commentaire in themes:
        st.subheader(f"📌 {titre}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Distribution de l'âge par modalité**")
            boxplot_plotly(df, col)
            st.markdown("**Statistiques descriptives**")
            tableau_stats(df, col)
        with col2:
            st.markdown("**Répartition par tranche d'âge (%)**")
            barres_plotly(df, col, f"{titre} par tranche d'âge", legende)
        st.success(f"✅ **Conclusion** : {commentaire}")
        st.markdown("---")

    st.subheader("🎯 Conclusion générale")
    st.markdown("""
    **L'âge impacte significativement les choix des clients :**
    - 🚗 Les **jeunes** achètent de l'occasion, des citadines, sans financement LOA
    - 🏆 Les **seniors** achètent du neuf, des SUV, et privilégient la LOA
    - 🏷️ Le groupe de marque est moins impacté par l'âge
    - ✅ L'hypothèse est **confirmée** pour 3 des 4 dimensions analysées
    """)


# ============================================================
# PAGE 3 — HYPOTHÈSE 2 : IMPACT DU GENRE
# ============================================================

def page_hypothese_genre(df):
    import plotly.graph_objects as go

    st.title("📊 Hypothèse 2 — Le genre impacte-t-il les choix des clients ?")
    st.markdown("""
    > **Hypothèse** : Le genre du client (Homme / Femme) influence ses choix en matière
    > de véhicule (neuf/occasion, catégorie, groupe de marque) et de financement.
    """)
    st.markdown("---")

    LABELS_GENRE      = {"H": "Hommes", "F": "Femmes"}
    ORDRE_FINANCEMENT = ["Crédit", "LOA", "Sans financement"]
    LABELS_MAP        = {"VN": "Véhicule Neuf", "VO": "Véhicule Occasion"}

    def graphique_interactif(df, col, titre):
        """Barres empilées 100% par modalité, genre en couleur, effectif au survol."""
        if col not in df.columns:
            st.warning(f"Colonne {col} manquante")
            return

        # pivot : lignes = genres, colonnes = modalités
        pivot_n = (
            df.groupby(["GENDER", col], observed=True)
            .size().unstack(fill_value=0)
        )
        if col == "FI_TYPE":
            pivot_n = pivot_n[[c for c in ORDRE_FINANCEMENT if c in pivot_n.columns]]
        pivot_n.index = [LABELS_GENRE.get(i, i) for i in pivot_n.index]
        pivot_n.columns = [LABELS_MAP.get(c, c) for c in pivot_n.columns]
        pivot_pct = pivot_n.div(pivot_n.sum(axis=1), axis=0) * 100

        genres    = pivot_pct.index.tolist()       # Hommes / Femmes → axe X
        modalites = pivot_pct.columns.tolist()     # Citadine, SUV... → couleurs
        fig = go.Figure()

        for modalite, couleur in zip(modalites, COULEURS):
            fig.add_trace(go.Bar(
                name=modalite,
                x=genres,
                y=pivot_pct[modalite].round(1),
                marker_color=couleur,
                customdata=pivot_n[modalite].values,
                hovertemplate="<b>%{x}</b><br>"
                              f"{modalite}<br>"
                              "Part : %{{y:.1f}}%<br>"
                              "Effectif : %{{customdata}}<extra></extra>",
            ))

        fig.update_layout(
            title=dict(text=titre, font=dict(size=14)),
            barmode="stack",
            yaxis=dict(title="% des commandes", ticksuffix="%", range=[0, 100]),
            xaxis=dict(title=""),
            legend=dict(title="Genre"),
            plot_bgcolor="white",
            height=420,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)

    themes = [
        ("VEHICULE_TYPE",      "Neuf vs Occasion par genre",
         "Hommes et femmes achètent majoritairement de l'**occasion**. "
         "La différence est faible, le genre n'impacte pas significativement ce choix."),
        ("VEHICULE_CATEGORIE", "Catégorie de véhicule par genre",
         "Les **SUV** dominent les commandes des deux sexes (49-57%)."
         "Cependant, les **femmes** privilégient nettement les **citadines (35%)**,"
         "tandis que les **hommes** s'orientent davantage vers les **berlines** compactes et les **breaks**."),
        ("GROUPE_MARQUE",      "Groupe de marque par genre",
         "Le **Généraliste Français** domine chez les deux genres. "
         "Proportionnellement, les hommes sont légèrement plus représentés sur les marques **Premium**."),
        ("FI_TYPE",            "Type de financement par genre",
         "Légères différences sur le financement : les femmes achètent un peu plus souvent "
         "**sans financement** que les hommes."),
    ]

    for col, titre, commentaire in themes:
        st.subheader(f"📌 {titre.split(' par ')[0]}")
        graphique_interactif(df, col, titre)
        st.success(f"✅ **Conclusion** : {commentaire}")
        st.markdown("---")

    st.subheader("🎯 Conclusion générale")
    st.markdown("""
    **Le genre a un impact très modéré sur les choix des clients :**
    - 🚗 Peu de différence sur le choix **neuf vs occasion**
    - 🏙️ Les **femmes** achètent plus de **citadines**, les **hommes** plus de **berlines/breaks**
    - 🏷️ Le groupe de marque est similaire entre les deux genres
    - 💳 Légères différences sur le **financement** mais pas déterminantes
    - ⚠️ L'hypothèse ne peut pas être confirmée — le genre semble seulement avoir une influence sur le choix de la catégorie
    """)


# ============================================================
# PAGE 4 — HYPOTHÈSE 3 : IMPACT DE LA RÉGION
# ============================================================

def page_hypothese_region(df):
    import plotly.graph_objects as go

    st.title("📊 Hypothèse 3 — La région influence-t-elle le type de véhicule ?")
    st.markdown("""
    > **Hypothèse** : La région de résidence du client influence ses choix en matière
    > de véhicule (neuf/occasion, catégorie, groupe de marque) et de financement.
    """)
    st.markdown("---")

    LABELS_MAP        = {"VN": "Véhicule Neuf", "VO": "Véhicule Occasion"}
    ORDRE_FINANCEMENT = ["Crédit", "LOA", "Sans financement"]
    ORDRE_REGIONS     = [
        "Île-de-France", "Auvergne-Rhône-Alpes", "PACA", "Occitanie",
        "Nouvelle-Aquitaine", "Grand Est", "Hauts-de-France", "Normandie",
        "Bretagne", "Pays de la Loire", "Centre-Val de Loire", "Bourgogne-Franche-Comté"
    ]

    df = df[df["REGION"].isin(ORDRE_REGIONS)]

    def barres_region(df, col, titre):
        if col not in df.columns:
            st.warning(f"Colonne {col} manquante")
            return
        pivot_n = (
            df.groupby(["REGION", col], observed=True)
            .size().unstack(fill_value=0)
        )
        if col == "FI_TYPE":
            pivot_n = pivot_n[[c for c in ORDRE_FINANCEMENT if c in pivot_n.columns]]
        pivot_n = pivot_n.reindex([r for r in ORDRE_REGIONS if r in pivot_n.index])
        pivot_n.columns = [LABELS_MAP.get(c, c) for c in pivot_n.columns]
        pivot_pct = pivot_n.div(pivot_n.sum(axis=1), axis=0) * 100

        fig = go.Figure()
        for i, modalite in enumerate(pivot_pct.columns):
            fig.add_trace(go.Bar(
                name=modalite,
                x=pivot_pct.index.tolist(),
                y=pivot_pct[modalite].round(1),
                marker_color=COULEURS[i % len(COULEURS)],
                customdata=pivot_n[modalite].values,
                hovertemplate="<b>%{x}</b><br>" + modalite + "<br>Part : %{y:.1f}%<br>Effectif : %{customdata}<extra></extra>",
            ))
        fig.update_layout(
            title=dict(text=titre, font=dict(size=13)),
            barmode="stack",
            xaxis=dict(title="", tickangle=-30),
            yaxis=dict(title="% des commandes", ticksuffix="%", range=[0, 100]),
            legend=dict(title="Modalité"),
            plot_bgcolor="white", height=450,
        )
        fig.update_yaxes(gridcolor="#eeeeee")
        st.plotly_chart(fig, use_container_width=True)

    themes = [
        ("VEHICULE_TYPE",      "Neuf vs Occasion par région",
         "L'**occasion** domine largement le marché français (environ **60 %**) dans toutes les régions. "
         "Les Hauts-de-France affichent la part de neuf la plus élevée, tandis que la Bretagne privilégie massivement l'occasion."),
        ("VEHICULE_CATEGORIE", "Catégorie de véhicule par région",
         "Les **SUV** dominent largement toutes les régions (environ **50-60 %**). Les **citadines** sont le second choix partout, "
         "suivies par les **berlines compactes**."),
        ("GROUPE_MARQUE",      "Groupe de marque par région",
         "Les marques généralistes françaises dominent massivement toutes les régions (environ 70 %). "
         "PACA se distingue par la plus forte part de généralistes étrangères,"
         " tandis que le segment premium reste marginal partout. "),
        ("FI_TYPE",            "Type de financement par région",
         "Le **sans financement** domine dans toutes les régions. "
         "La **LOA** est légèrement plus présente en **Île-de-France** et dans les grandes métropoles."),
    ]

    for col, titre, commentaire in themes:
        st.subheader(f"📌 {titre.split(' par ')[0]}")
        barres_region(df, col, titre)
        st.success(f"✅ **Conclusion** : {commentaire}")
        st.markdown("---")

    st.subheader("🎯 Conclusion générale")
    st.markdown("""
    **La région influence modérément les choix des clients :**
    - 🚗 Les régions du **Sud** achètent légèrement plus de véhicules **neufs**
    - 🏙️ Les **4x4/SUV** dominent partout mais davantage dans les régions montagneuses
    - 🏷️ Les marques **Premium** légèrement plus présentes en **Île-de-France**
    - 💳 La **LOA** plus répandue dans les grandes agglomérations
    - ⚠️ L'hypothèse est **partiellement confirmée** — les différences existent mais restent modérées
    """)


# ============================================================
# PAGE 5 — TESTS STATISTIQUES (Chi²)
# ============================================================

def page_tests_statistiques(df):
    """
    Page dédiée aux tests statistiques Chi² et V de Cramér
    pour valider/infirmer les 3 hypothèses marketing.
    """
    import numpy as np
    from scipy.stats import chi2_contingency
    
    st.title("📊 Tests Statistiques — Validation des hypothèses")
    st.markdown("""
    > Cette page présente les résultats des tests du **Chi²** et du **V de Cramér**  
    > pour valider ou infirmer statistiquement les trois hypothèses marketing.
    """)
    st.markdown("---")
    
    # ============================================================
    # FONCTION DE CALCUL
    # ============================================================
    
    def calculer_chi2_vcramer(df, var1, var2):
        """Calcule Chi², p-value et V de Cramér entre deux variables."""
        table = pd.crosstab(df[var1], df[var2])
        chi2, p, dof, expected = chi2_contingency(table)
        n = len(df)
        k = min(table.shape) - 1
        v_cramer = np.sqrt(chi2 / (n * k)) if k > 0 else 0
        return chi2, p, dof, v_cramer
    
    def interpreter_pvalue(p):
        """Interprète la p-value avec étoiles."""
        if p < 0.001:
            return "*** (très significatif)", "🟢", "p < 0.001"
        elif p < 0.01:
            return "** (très significatif)", "🟢", "p < 0.01"
        elif p < 0.05:
            return "* (significatif)", "🟡", "p < 0.05"
        else:
            return "ns (non significatif)", "🔴", f"p = {p:.4f}"
    
    def interpreter_vcramer(v):
        """Interprète le V de Cramér."""
        if v >= 0.3:
            return "Forte", "🟢"
        elif v >= 0.1:
            return "Modérée", "🟡"
        else:
            return "Faible", "🔴"
    
    # ============================================================
    # HYPOTHÈSE 1 : ÂGE
    # ============================================================
    
    st.header("📌 Hypothèse 1 : L'âge impacte-t-il les choix des clients ?")
    
    with st.expander("🔍 Détails des tests", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        # Test 1 : Âge vs Type de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "TRANCHE_AGE", "VEHICULE_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚗 Âge → Type véhicule</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 2 : Âge vs Catégorie de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "TRANCHE_AGE", "VEHICULE_CATEGORIE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚙 Âge → Catégorie</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 3 : Âge vs Financement
        chi2, p, dof, v = calculer_chi2_vcramer(df, "TRANCHE_AGE", "FI_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col3:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>💰 Âge → Financement</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Conclusion Hypothèse 1
    st.markdown("""
    <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; margin-top: 10px;'>
        <h4 style='color: #2e7d32;'>🎯 Conclusion Hypothèse 1</h4>
        <p>✅ <strong>HYPOTHÈSE CONFIRMÉE</strong> — L'âge influence significativement les choix :</p>
        <ul>
            <li>Type de véhicule (neuf/occasion) : V de Cramér > 0.1, p < 0.001</li>
            <li>Catégorie de véhicule : V de Cramér modéré, très significatif</li>
            <li>Mode de financement : V de Cramér modéré, très significatif</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================================
    # HYPOTHÈSE 2 : GENRE
    # ============================================================
    
    st.header("📌 Hypothèse 2 : Le genre impacte-t-il les choix des clients ?")
    
    with st.expander("🔍 Détails des tests", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        # Test 1 : Genre vs Type de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "GENDER", "VEHICULE_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚗 Genre → Type véhicule</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 2 : Genre vs Catégorie de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "GENDER", "VEHICULE_CATEGORIE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚙 Genre → Catégorie</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 3 : Genre vs Financement
        chi2, p, dof, v = calculer_chi2_vcramer(df, "GENDER", "FI_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col3:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>💰 Genre → Financement</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Conclusion Hypothèse 2
    st.markdown("""
    <div style='background-color: #fff3e0; padding: 15px; border-radius: 10px; margin-top: 10px;'>
        <h4 style='color: #ed6c02;'>🎯 Conclusion Hypothèse 2</h4>
        <p>⚠️ <strong>HYPOTHÈSE PARTIELLEMENT CONFIRMÉE</strong> — Le genre a un impact modéré :</p>
        <ul>
            <li>Type de véhicule : différence significative V de Cramér faible</li>
            <li>Catégorie de véhicule : différence significative mais V de Cramér modérée</li>
            <li>Financement : légère différence mais V de Cramér faible</li>
        </ul>
        <p><strong>→ Le genre influence principalement le choix de la catégorie de véhicule.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================================
    # HYPOTHÈSE 3 : RÉGION
    # ============================================================
    
    st.header("📌 Hypothèse 3 : La région impacte-t-elle les choix des clients ?")
    
    with st.expander("🔍 Détails des tests", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        # Test 1 : Région vs Type de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "REGION", "VEHICULE_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚗 Région → Type véhicule</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 2 : Région vs Catégorie de véhicule
        chi2, p, dof, v = calculer_chi2_vcramer(df, "REGION", "VEHICULE_CATEGORIE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>🚙 Région → Catégorie</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Test 3 : Région vs Financement
        chi2, p, dof, v = calculer_chi2_vcramer(df, "REGION", "FI_TYPE")
        interp_p, icon_p, detail_p = interpreter_pvalue(p)
        interp_v, icon_v = interpreter_vcramer(v)
        
        with col3:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>💰 Région → Financement</h4>
                <hr>
                <p><strong>Chi²</strong> = {chi2:.1f}</p>
                <p><strong>ddl</strong> = {dof}</p>
                <p><strong>p-value</strong> = {p:.4f}<br>{icon_p} {interp_p}</p>
                <p><strong>V de Cramér</strong> = {v:.3f}<br>{icon_v} {interp_v}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Conclusion Hypothèse 3
    st.markdown("""
    <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; margin-top: 10px;'>
        <h4 style='color: #0288d1;'>🎯 Conclusion Hypothèse 3</h4>
        <p>⚠️ <strong>HYPOTHÈSE PARTIELLEMENT CONFIRMÉE</strong> — La région a un impact marginal :</p>
        <ul>
            <li>Type de véhicule (neuf/occasion) : non significatif</li>
            <li>Catégorie de véhicule : V de Cramér faible mais significatif</li>
            <li>Financement : V de Cramér faible mais significatif</li>
        </ul>
        <p><strong>→ La région n'a aucune influence sur le choix entre neuf et occasion. 
                Elle exerce une influence significative mais très faible sur le financement et la catégorie de véhicule, 
                suggérant des habitudes régionales très proches les unes des autres.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================================
    # TABLEAU RÉCAPITULATIF
    # ============================================================
    
    st.subheader("📋 Tableau récapitulatif des tests")
    
    # Créer un DataFrame récapitulatif
    recapitulatif = []
    
    tests = [
        ("H1: Âge → Type véhicule", "TRANCHE_AGE", "VEHICULE_TYPE"),
        ("H1: Âge → Catégorie", "TRANCHE_AGE", "VEHICULE_CATEGORIE"),
        ("H1: Âge → Financement", "TRANCHE_AGE", "FI_TYPE"),
        ("H2: Genre → Type véhicule", "GENDER", "VEHICULE_TYPE"),
        ("H2: Genre → Catégorie", "GENDER", "VEHICULE_CATEGORIE"),
        ("H2: Genre → Financement", "GENDER", "FI_TYPE"),
        ("H3: Région → Type véhicule", "REGION", "VEHICULE_TYPE"),
        ("H3: Région → Catégorie", "REGION", "VEHICULE_CATEGORIE"),
        ("H3: Région → Financement", "REGION", "FI_TYPE"),
    ]
    
    for nom_test, var1, var2 in tests:
        chi2, p, dof, v = calculer_chi2_vcramer(df, var1, var2)
        interp_p, _, _ = interpreter_pvalue(p)
        interp_v, _ = interpreter_vcramer(v)
        recapitulatif.append({
            "Test": nom_test,
            "Chi²": round(chi2, 1),
            "ddl": dof,
            "p-value": f"{p:.4f}",
            "Significativité": interp_p,
            "V de Cramér": round(v, 3),
            "Force association": interp_v
        })
    
    df_recap = pd.DataFrame(recapitulatif)
    st.dataframe(df_recap, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ============================================================
    # LÉGENDE ET INTERPRÉTATION
    # ============================================================
    
    with st.expander("📖 Légende et interprétation des indicateurs"):
        st.markdown("""
        ### 📊 Comprendre les résultats
        
        **🔬 Test du Chi²**
        - Mesure si deux variables sont indépendantes ou non
        - **p-value < 0.05** : relation significative (on rejette l'indépendance)
        - *** = p < 0.001 (très significatif), ** = p < 0.01, * = p < 0.05, ns = non significatif
        
        **📏 V de Cramér**
        - Mesure la force de l'association (entre 0 et 1)
        - **> 0.3** : association forte
        - **0.1 - 0.3** : association modérée
        - **< 0.1** : association faible
        
        **🎯 Pour vos hypothèses**
        - **Hypothèse 1 (Âge)** : ✅ CONFIRMÉE — p-values très faibles, V de Cramér modéré à fort
        - **Hypothèse 2 (Genre)** : ⚠️ PARTIELLEMENT CONFIRMÉE — significatif mais association faible
        - **Hypothèse 3 (Région)** : ⚠️ PARTIELLEMENT CONFIRMÉE — significatif mais association faible
        """)
    
    st.markdown("---")
    st.caption("Les tests Chi² et V de Cramér permettent de valider statistiquement les hypothèses marketing.")


# ============================================================
# PAGE 6 — AFDM (Analyse Factorielle de Données Mixtes)
# ============================================================

def page_afdm(df):
    """
    Page dédiée à l'AFDM — Analyse Factorielle de Données Mixtes
    """
    import numpy as np
    from scipy.stats import chi2_contingency
    
    st.title("📊 AFDM — Analyse Factorielle de Données Mixtes")
    st.markdown("""
    > L'AFDM permet d'explorer les relations entre **variables numériques et catégorielles**.
    > Elle confirme visuellement les résultats des tests Chi².
    """)
    st.markdown("---")
    
    # ============================================================
    # VARIANCE EXPLIQUÉE
    # ============================================================
    
    st.header("📈 Variance expliquée")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        | Axe | % variance | Cumulé |
        |-----|------------|--------|
        | Axe 1 | 27.6% | 27.6% |
        | Axe 2 | 20.3% | 47.9% |
        | Axe 3 | 18.2% | 66.1% |
        | Axe 4 | 17.8% | 83.9% |
        | Axe 5 | 16.2% | 100% |
        """)
    
    with col2:
        st.image("outputs/afdm_eboulis.png", use_container_width=True)
        st.caption("Éboulis des valeurs propres")
    
    st.markdown("---")
    
    # ============================================================
    # CONTRIBUTION DES VARIABLES
    # ============================================================
    
    st.header("🎯 Contribution des variables")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Axe 1 (27.6%) — Type de véhicule / Âge")
        st.markdown("""
        | Variable | Contribution |
        |----------|--------------|
        | Type véhicule | 0.557 |
        | Kilométrage | 0.457 |
        | Tranche d'âge | 0.361 |
        | Âge | 0.355 |
        | Financement | 0.307 |
        | Prix véhicule | 0.263 |
        | Catégorie | 0.202 |
        """)
        st.info("💡 **Axe 1** : oppose les **jeunes acheteurs d'occasion** (VO, km élevés) aux **seniors acheteurs de neuf**.")
    
    with col2:
        st.subheader("Axe 2 (20.3%) — Catégorie/ Genre")
        st.markdown("""
        | Variable | Contribution |
        |----------|--------------|
        | Catégorie véhicule | 0.499 |
        | Genre | 0.245 |
        | Tranche d'âge | 0.169 |
        | Groupe marque | 0.161 |
        | Région | 0.130 |
        | Financement | 0.122 |
        """)
        st.info("💡 **Axe 2** :distingue principalement les choix de carrosserie (SUV, Berlines, Citadines). Ce comportement est fortement corrélé au genre de l'acheteur**.")
    
    st.markdown("---")
    
    # ============================================================
    # GRAPHIQUE DES VARIABLES
    # ============================================================
    
    st.header("📊 Contribution graphique des variables")
    st.image("outputs/afdm_variables.png", use_container_width=True)
    st.caption("Contribution des variables sur les axes 1 et 2 (au-delà du seuil moyen = 0.091)")
    
    st.markdown("---")
    
    # ============================================================
    # NUAGE DES INDIVIDUS
    # ============================================================
    
    st.header("👥 Nuage des individus")
    st.markdown("Visualisation des individus colorés selon différentes variables.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("outputs/afdm_individus.png", use_container_width=True)
        st.caption("Nuage des individus coloré par Type véhicule, Catégorie, Financement et Tranche d'âge")
    
    with col2:
        st.markdown("""
        ### Observations clés
        
        **Type véhicule** :
        Séparation nette sur l'axe 1. Le Neuf (VN) est à gauche, 
        l'Occasion (VO) est à droite
        
        **Financement** :
        La LOA est une pratique de "gauche" sur le graphique, 
        elle est donc fortement associée aux Seniors et aux véhicules neufs.
        
        **Tranche d'âge** :
        Corrélation forte avec l'axe 1. 
        Les Seniors (60+) sont à gauche (acheteurs de Neuf), 
        tandis que les Jeunes (18-40) sont à droite (acheteurs d'Occasion).
        
        **Catégorie** :
        Les Citadines sont majoritairement en bas à droite (Jeunes / Occasion), 
        lors que les SUV se projettent plus vers le haut et la gauche.
        """)
    
    st.markdown("---")
    
    # ============================================================
    # SYNTHÈSE ET COHÉRENCE AVEC LE CHI²
    # ============================================================
    
    st.header("✅ Cohérence avec les tests Chi²")
    
    st.markdown("""
    | Variable | AFDM (contribution) | Chi² (V de Cramér) | Cohérence |
    |----------|---------------------|--------------------|-----------|
    | **Âge** | Forte (0.361) | Modéré (0.13) | ✅ |
    | **Type véhicule** | Très forte (0.557) | Modéré (0.188) | ✅ |
    | **Financement** | Modérée (0.307) | Modéré (0.101) | ✅ |
    | **Genre** | Faible (0.067) | Faible (0.06-0.22) | ✅ |
    | **Région** | Très faible (0.023) | Très faible (0.06-0.09) | ✅ |
    """)
    
    st.success("""
    **Conclusion AFDM** :
    - L'AFDM confirme que **l'âge et le type de véhicule** sont les dimensions les plus structurantes
    - **Le genre** est un facteur secondaire pour expliquer le choix Neuf/Occasion (Axe 1), 
               mais reste un facteur clé pour expliquer le choix de la catégorie de véhicule (Axe 2)
    - **La région** n'apporte quasiment aucune contribution à l'explication des choix clients
    - Les résultats sont cohérents avec les tests du Chi² et du V de Cramér
    """)
    
    st.markdown("---")
    st.caption("L'AFDM valide visuellement les conclusions statistiques des tests Chi².")




# ============================================================
# PAGE — RECOMMANDATIONS MARKETING
# ============================================================

def page_recommandations(df):
    st.title("💡 Recommandations Marketing")
    st.markdown("""
    > Sur la base des analyses réalisées (hypothèses, tests Chi², AFDM),
    > voici les recommandations marketing adressées à l'entreprise.
    """)
    st.markdown("---")

    # Recommandation 1
    st.subheader("🎯 Recommandation 1 — Cibler les jeunes sur l'occasion")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Constat :** Les clients de 18-40 ans représentent **33% de la clientèle** et achètent
        à **~70% des véhicules d'occasion**. Ils privilégient les citadines et évitent la LOA.

        **Recommandation :**
        - Créer des offres **"premier achat"** dédiées aux jeunes conducteurs
        - Mettre en avant des **citadines d'occasion à petit prix** dans les communications digitales
        - Proposer des **financements sans LOA** adaptés (crédit classique, paiement comptant facilité)
        - Cibler via les **réseaux sociaux** (Instagram, TikTok) où cette tranche est active
        """)
    with col2:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #2E86AB;'>33%</h2>
            <p>des clients ont 18-40 ans</p>
            <h2 style='color: #2E86AB;'>~70%</h2>
            <p>achètent de l'occasion</p>
            <h2 style='color: #2E86AB;'>V = 0.188</h2>
            <p>association âge × type véhicule (***)</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Recommandation 2
    st.subheader("🏆 Recommandation 2 — Cibler les seniors sur le neuf + LOA")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Constat :** Les clients de 60+ ans basculent majoritairement vers le **véhicule neuf**
        et adoptent massivement la **LOA** (jusqu'à 75% chez les 70+). Ils privilégient les SUV/4x4.

        **Recommandation :**
        - Développer des offres **LOA premium** sur SUV et 4x4 neufs
        - Mettre en avant le **confort, la sécurité et les garanties** du neuf dans les messages
        - Communiquer via des **canaux traditionnels** (presse, TV, email) adaptés à cette cible
        - Proposer un **service de livraison à domicile** renforcé (distance agence souvent élevée)
        """)
    with col2:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #2E86AB;'>~55%</h2>
            <p>des 70+ achètent du neuf</p>
            <h2 style='color: #2E86AB;'>75%</h2>
            <p>des 70+ choisissent la LOA</p>
            <h2 style='color: #2E86AB;'>V = 0.356</h2>
            <p>association type × financement (***)</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Recommandation 3
    st.subheader("👥 Recommandation 3 — Adapter la communication par genre")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Constat :** Le genre influence significativement le **choix de la catégorie de véhicule**
        (V=0.217, ***). Les femmes achètent davantage de **citadines**, les hommes plus de
        **SUV, berlines et breaks**.

        **Recommandation :**
        - Segmenter les **campagnes publicitaires** selon le genre
        - Pour les femmes : mettre en avant la **praticité, le stationnement facile, la consommation**
        - Pour les hommes : mettre en avant la **puissance, l'espace, les équipements**
        - Adapter les **visuels du site web** selon le profil de navigation détecté
        """)
    with col2:
        st.markdown("""
        <div style='background-color: #EAF4FB; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #2E86AB;'>66%</h2>
            <p>de la clientèle est masculine</p>
            <h2 style='color: #2E86AB;'>V = 0.217</h2>
            <p>association genre × catégorie (***)</p>
            <h2 style='color: #E84855;'>34%</h2>
            <p>de clientèle féminine à développer</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Synthèse
    st.subheader("📋 Synthèse des recommandations")
    st.markdown("""
    | # | Cible | Action | Priorité |
    |---|-------|--------|----------|
    | 1 | 18-40 ans | Offres occasion + citadines + financement sans LOA | 🔴 Haute |
    | 2 | 60+ ans | Offres neuf + SUV + LOA premium | 🔴 Haute |
    | 3 | Segmentation genre | Adapter visuels et messages pub | 🟠 Moyenne |
    """)


# ============================================================
# NAVIGATION (UNIQUE)
# ============================================================

def main():
    st.sidebar.title("🚗 Dashboard Clients")
    st.sidebar.markdown("**Analyse du profil clients**")
    st.sidebar.markdown("---")

    pages = {
        "🏠 Accueil":                    page_accueil,
        "📈 Vue Globale":                page_global,
        "📊 Hypothèse 1 — Âge":         page_hypothese_age,
        "📊 Hypothèse 2 — Genre":        page_hypothese_genre,
        "📊 Hypothèse 3 — Région":       page_hypothese_region,
        "📊 Tests Statistiques":         page_tests_statistiques,
        "📊 AFDM — Analyse factorielle": page_afdm,
        "💡 Recommandations":            page_recommandations,
    }

    choix = st.sidebar.radio("Navigation", list(pages.keys()))

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Projet Datamining M1**")
    st.sidebar.markdown("2025/2026")

    if choix == "🏠 Accueil":
        pages[choix]()
    else:
        with st.spinner("Chargement des données..."):
            df = charger_donnees()
        pages[choix](df)


if __name__ == "__main__":
    main()
