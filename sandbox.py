"""Recherche de joueurs avec suggestions pendant la frappe.

Installation : python -m pip install streamlit-searchbox
Lancement : python -m streamlit run sandbox.py

Intégration : copier les fonctions de recherche dans
composants/onglet_joueurs/recherche_joueurs.py, avec leurs imports.
Dans afficher_onglet_joueurs(), appeler afficher_recherche_joueurs(donnees)
AVANT les vignettes et le tableau. Passer st.session_state.donnees pour
chercher dans tous les joueurs, ou les données filtrées pour limiter la recherche.
Ajouter streamlit-searchbox à requirements.txt lors de l'intégration.
Les fonctions existantes gèrent la liste de Series pandas et les doublons.
Documentation : https://github.com/m-wrzr/streamlit-searchbox
"""

from functools import partial
from pathlib import Path
import unicodedata

import pandas as pd
import plotly.express as px
import streamlit as st

from composants.onglet_joueurs.joueurs_selectionnes import (
    ajouter_joueur,
    extraire_donnees_joueurs_selectionnes,
    initialiser_selection_joueurs,
)
from composants.onglet_joueurs.Affichage_joueurs_selectionnes import (
    afficher_joueurs_selectionnes,
)


# Uniformise le texte pour rechercher sans tenir compte des accents et majuscules.
# À placer dans composants/onglet_joueurs/recherche_joueurs.py.
def normaliser_nom(texte):
    texte = unicodedata.normalize("NFKD", str(texte).strip().casefold())
    return "".join(lettre for lettre in texte if not unicodedata.combining(lettre))


# Renvoie au maximum cinq correspondances, même au milieu du nom.
# Chaque suggestion contient un libellé et une URL identifiant le joueur.
# L'équipe distingue les homonymes ; l'ordre des données est conservé.
# À placer dans composants/onglet_joueurs/recherche_joueurs.py.
def rechercher_joueurs(texte, donnees):
    recherche = normaliser_nom(texte)
    if not recherche:
        return []
    noms = donnees["Name"].fillna("").map(normaliser_nom)
    resultats = donnees[noms.str.contains(recherche, regex=False)].head(5)
    return [
        (f"{joueur['Name']} ({joueur['Team']})", joueur["url"])
        for _, joueur in resultats.iterrows()
    ]


# Ajoute la ligne complète à joueurs_selectionnes via la fonction existante.
# Renouvelle la recherche pour pouvoir resélectionner le même joueur après retrait.
# À placer dans composants/onglet_joueurs/recherche_joueurs.py.
def ajouter_joueur_recherche(url_joueur, donnees):
    correspondances = donnees[donnees["url"] == url_joueur]
    if not correspondances.empty:
        ajouter_joueur(correspondances.iloc[0])
    st.session_state.version_recherche_joueurs += 1


# Affiche une barre unique avec un menu de suggestions actualisé pendant la frappe.
# Seule une sélection dans le menu ajoute un joueur ; une simple saisie ne suffit pas.
# À appeler dans structure_onglet_joueurs.py, avant les vignettes et le tableau.
def afficher_recherche_joueurs(donnees):
    from streamlit_searchbox import st_searchbox

    initialiser_selection_joueurs()
    st.session_state.setdefault("version_recherche_joueurs", 0)
    st_searchbox(
        search_function=partial(rechercher_joueurs, donnees=donnees),
        submit_function=partial(ajouter_joueur_recherche, donnees=donnees),
        label="Rechercher un joueur",
        placeholder="Tapez tout ou partie du nom…",
        clear_on_submit=True,
        debounce=200,
        key=f"recherche_joueurs_{st.session_state.version_recherche_joueurs}",
    )


# Ajoute le joueur identifié par son URL et affiche une confirmation temporaire.
# À insérer dans scatterplot.py ; réutilise les fonctions de joueurs_selectionnes.py.
def ajouter_joueur_du_graphique(url_joueur, donnees):
    joueurs = extraire_donnees_joueurs_selectionnes()
    if any(joueur["url"] == url_joueur for joueur in joueurs):
        return
    correspondances = donnees[donnees["url"] == url_joueur]
    if correspondances.empty:
        return
    joueur = correspondances.iloc[0]
    ajouter_joueur(joueur)
    st.toast(f"Le joueur {joueur['Name']} a été ajouté à la sélection.")


# Traite uniquement un nouvel événement du graphique, avant le réaffichage.
# À insérer dans scatterplot.py. Les URL évitent de confondre traces et homonymes.
def detecter_clic_scatterplot(cle_graphique, donnees):
    initialiser_selection_joueurs()
    evenement = st.session_state.get(cle_graphique, {})
    for point in evenement.get("selection", {}).get("points", []):
        identifiants = point.get("customdata")
        if identifiants:
            ajouter_joueur_du_graphique(identifiants[0], donnees)


# Prépare les couleurs sans modifier les données sources.
# À insérer dans scatterplot.py ; remplace la préparation actuelle pour ce prototype.
def preparer_couleurs_scatterplot(donnees):
    tableau = donnees.copy()
    tableau["hue"] = "Autres"
    for joueur in extraire_donnees_joueurs_selectionnes():
        tableau.loc[tableau["url"] == joueur["url"], "hue"] = joueur["Name"]
    return tableau


# Affiche un nuage cliquable et transmet les lignes complètes au callback.
# Proposition pour scatterplot.py : appeler avec les données filtrées COMPLÈTES,
# avant de réduire les colonnes, pour conserver toutes les statistiques du joueur.
# Si tu gardes ton graphique actuel, ajouter customdata=autres[["url"]].to_numpy()
# à go.Scatter et custom_data=["url"] à px.scatter, puis reprendre le st.plotly_chart.
def afficher_scatterplot_cliquable(donnees, variable_x, variable_y):
    initialiser_selection_joueurs()
    tableau = preparer_couleurs_scatterplot(donnees)
    figure = px.scatter(
        tableau, x=variable_x, y=variable_y, color="hue",
        hover_name="Name", custom_data=["url"],
        color_discrete_map={"Autres": "lightgrey"},
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    for trace in figure.data:
        trace.marker.opacity = 0.3 if trace.name == "Autres" else 0.8
    figure.update_layout(clickmode="event+select", hovermode="closest", height=600)
    version = st.session_state.get("version_tableau_joueurs", 0)
    cle = f"scatterplot_sandbox_{variable_x}_{variable_y}_{version}"
    st.plotly_chart(
        figure, width="stretch", key=cle, selection_mode="points",
        on_select=partial(detecter_clic_scatterplot, cle, donnees),
    )


# Démonstration autonome avec recherche, vignettes et graphique cliquable.
# À garder uniquement dans sandbox.py, sans l'intégrer à l'application principale.
def afficher_sandbox():
    st.set_page_config(page_title="Recherche de joueurs", layout="wide")
    st.title("Recherche de joueurs")
    chemin = Path(__file__).parent / "donnees" / "all_players_clean.csv"
    donnees = pd.read_csv(chemin)
    afficher_recherche_joueurs(donnees)
    afficher_joueurs_selectionnes()
    afficher_scatterplot_cliquable(donnees, "PAC", "SHO")


if __name__ == "__main__":
    afficher_sandbox()
