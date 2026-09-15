import streamlit as st
from composants.onglet_joueurs.joueurs_selectionnes import supprimer_joueur, extraire_donnees_joueurs_selectionnes

def afficher_joueurs_selectionnes():
    joueurs = extraire_donnees_joueurs_selectionnes()
    if not joueurs:
        st.caption("Cliquez sur une cellule du tableau pour ajouter un joueur.")
        return
    with st.container(horizontal=True, gap="small"):
            for joueur in joueurs:
                afficher_vignette_joueur(joueur)

def afficher_vignette_joueur(joueur):
    st.button(
            label=joueur["Name"],
            key=f"supprimer_joueur_{joueur['url']}",
            help=f"Retirer {joueur['Name']}",
            on_click=supprimer_joueur,
            args=(joueur["url"],),
        )