from functools import partial
import streamlit as st
from streamlit_searchbox import st_searchbox
from composants.onglet_joueurs.rechercher_joueur import rechercher_joueurs, ajouter_joueur_recherche
from composants.onglet_joueurs.joueurs_selectionnes import initialiser_selection_joueurs


def afficher_recherche_joueurs(donnees):
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