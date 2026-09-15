from functools import partial
import streamlit as st
from composants.onglet_joueurs.joueurs_selectionnes import ajouter_joueur, extraire_donnees_joueurs_selectionnes, initialiser_selection_joueurs
import plotly.express as px
from donnees.donnees_filtrees import obtenir_donnees_filtrees

def afficher_scatterplot():
    variable_x = st.session_state.get("la variable X")
    variable_y = st.session_state.get("la variable Y")
    if tester_variables(variable_x, variable_y):
        donnees = obtenir_donnees_filtrees()
        creer_scatterplot(donnees, variable_x, variable_y)
        return donnees

def tester_variables(variable_x, variable_y):
    if variable_x and variable_y and variable_x != variable_y:
        return True
    st.warning("Veuillez sélectionner deux variables distinctes.")
    return False

def preparer_couleurs_scatterplot(donnees):
    tableau = donnees.copy()
    tableau["hue"] = "Autres"
    for joueur in extraire_donnees_joueurs_selectionnes():
        tableau.loc[tableau["url"] == joueur["url"], "hue"] = joueur["Name"]
    return tableau

def creer_scatterplot(donnees, variable_x, variable_y):
    initialiser_selection_joueurs()
    tableau = preparer_couleurs_scatterplot(donnees)
    figure = px.scatter(
        tableau, 
        x=variable_x, 
        y=variable_y, 
        color="hue",
        hover_name="Name", 
        custom_data=["url"],
        color_discrete_map={"Autres": "lightgrey"},
        color_discrete_sequence=px.colors.qualitative.Set1,
    )

    for trace in figure.data:
        trace.marker.opacity = 0.3 if trace.name == "Autres" else 0.8
    figure.update_layout(clickmode="event+select", hovermode="closest", height=600)
    version = st.session_state.get("version_tableau_joueurs", 0)
    cle = f"scatterplot_{variable_x}_{variable_y}_{version}"

    ## curseur normal
    st.html("""
        <style>
        .js-plotly-plot .nsewdrag,
        .js-plotly-plot .scatterlayer .point {
            cursor: default !important;
        }
        </style>
        """)
    
    st.plotly_chart(
        figure, width="stretch", key=cle, selection_mode="points",
        on_select=partial(detecter_clic_scatterplot, cle, donnees),
    )

def detecter_clic_scatterplot(cle_graphique, donnees):
    initialiser_selection_joueurs()
    evenement = st.session_state.get(cle_graphique, {})
    for point in evenement.get("selection", {}).get("points", []):
        identifiants = point.get("customdata")
        if identifiants:
            ajouter_joueur_du_graphique(identifiants[0], donnees)

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