
import streamlit as st


def initialiser_selection_joueurs():
    st.session_state.setdefault("joueurs_selectionnes", [])
    st.session_state.setdefault("version_tableau_joueurs", 0)

def ajouter_joueur(joueur):
    joueurs = st.session_state.joueurs_selectionnes
    if not any(selection["url"] == joueur["url"] for selection in joueurs):
        joueurs.append(joueur.copy())

def supprimer_joueur(url_joueur):
    st.session_state.joueurs_selectionnes = [
        joueur for joueur in st.session_state.joueurs_selectionnes
        if joueur["url"] != url_joueur
    ]
    st.session_state.version_tableau_joueurs += 1

def extraire_donnees_joueurs_selectionnes():
    return st.session_state.get("joueurs_selectionnes", [])

def detecter_clic_tableau(donnees_tableau, cle_tableau):
    cellules = st.session_state[cle_tableau]["selection"]["cells"]
    if not cellules:
        return
    position, _ = cellules[0]
    if 0 <= position < len(donnees_tableau):
        ajouter_joueur(donnees_tableau.iloc[position])





