# 🚗 Dashboard — Analyse du profil clients d'un leader de la vente automobile en ligne

Projet Datamining M1 Marketing 2025/2026

🔗 **[Accéder à l'application](https://dashboardprofilclient-e2r7w8kzb3pdkvcvuufopb.streamlit.app/)**

---

## 📋 Présentation du projet

Ce projet s'inscrit dans le cadre du cours de Datamining de M1 Marketing. L'objectif est d'analyser les données internes d'une **entreprise leader européen de la vente en ligne de voitures d'occasion reconditionnées** afin de mieux comprendre le profil de ses clients et leurs comportements d'achat.

L'analyse porte sur **plus de 4 000 commandes** réalisées sur une période de 5 mois, issues de 5 tables de données internes.

> ⚠️ Les données présentes dans ce repo sont des **données synthétiques** générées pour illustration. Elles reproduisent la structure et les tendances des données réelles sans en divulguer le contenu.

---

## 🗂️ Structure de l'application

| Page | Contenu |
|------|---------|
| 🏠 Accueil | Présentation de l'entreprise et du projet |
| 📈 Vue Globale | KPIs, âge, genre, saisonnalité, villes, financement |
| 📊 Hypothèse 1 — Âge | L'âge impacte-t-il les choix des clients ? |
| 📊 Hypothèse 2 — Genre | Le genre impacte-t-il les choix des clients ? |
| 📊 Hypothèse 3 — Région | La région influence-t-elle le type de véhicule ? |
| 📊 Tests Statistiques | Chi² et V de Cramér — validation statistique des hypothèses |
| 📊 AFDM | Analyse Factorielle de Données Mixtes |
| 💡 Recommandations | Recommandations marketing à destination de l'entreprise |

---

## 📊 Données

Les 5 tables analysées :

- `table_client.csv` — profil des clients (âge, genre, localisation)
- `table_commande_reprise.csv` — commandes et reprises
- `table_vehicule.csv` — caractéristiques des véhicules (type, marque, catégorie, kilométrage, équipements)
- `table_financement.csv` — type de financement (crédit, LOA, sans financement)
- `table_nearest_agency.csv` — distance à l'agence la plus proche

---

## 🔍 Principaux résultats

- **L'âge** est le facteur le plus discriminant : les jeunes (18-40 ans) achètent de l'occasion, les seniors (60+) du neuf en LOA
- **Le genre** influence significativement le choix de la catégorie : les femmes privilégient les citadines, les hommes les SUV/berlines (V de Cramér = 0.217 ***)
- **La région** n'a pas d'influence significative sur le type de véhicule acheté (V = 0.052, ns)
- **L'association la plus forte** est entre le type de véhicule et le financement (V = 0.356 ***)

---

## 🛠️ Stack technique

- **Python**
- **Streamlit** — application interactive
- **Pandas / NumPy** — manipulation des données
- **Plotly** — visualisations interactives
- **Prince** — AFDM (Analyse Factorielle de Données Mixtes)
- **SciPy** — tests Chi² et V de Cramér

---

## 🚀 Lancement en local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run streamlit_app.py
```

---

## 👤 Auteur

**Romain Cariou** — M1 Marketing 2025/2026
