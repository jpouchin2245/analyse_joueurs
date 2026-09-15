from functools import partial

import streamlit as st
from donnees import tester_donnees
from donnees.donnees_filtrees import obtenir_donnees_filtrees
from composants.onglet_joueurs.joueurs_selectionnes import ajouter_joueur

def afficher_tableau(donnees):
    limite = st.session_state.get("nb_joueurs", 50)
    donnees_tableau = donnees.sort_values("OVR", ascending=False).head(limite)
    cle_tableau = obtenir_cle_tableau(donnees_tableau)
    with st.container(border=True):
        st.dataframe(
            donnees_tableau,
            width="stretch",
            hide_index=True,
            key=cle_tableau,
            selection_mode="single-cell",
            on_select=partial(detecter_selection_joueur_clic, donnees_tableau, cle_tableau),
        )


def detecter_selection_joueur_clic(donnees_tableau, cle_tableau):
    cellules = st.session_state[cle_tableau]["selection"]["cells"]
    if not cellules:
        return
    position, _ = cellules[0]
    if 0 <= position < len(donnees_tableau):
        ajouter_joueur(donnees_tableau.iloc[position])


def obtenir_cle_tableau(donnees_tableau):
    identifiants = tuple(donnees_tableau["url"])
    if st.session_state.get("identifiants_tableau_joueurs") != identifiants:
        st.session_state.identifiants_tableau_joueurs = identifiants
        st.session_state.version_tableau_joueurs += 1
    return f"tableau_joueurs_{st.session_state.version_tableau_joueurs}"