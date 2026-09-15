import re

import streamlit as st
from composants.onglet_joueurs.joueurs_selectionnes import extraire_donnees_joueurs_selectionnes
from composants.onglet_comparaison.calculer_joueur_moyen import calculer_joueur_moyen
from composants.onglet_comparaison.fiche_joueur import afficher_fiche_joueur
from composants.onglet_comparaison.radarplot import afficher_radarplot
from composants.onglet_comparaison.toggle_statistiques import toggle


def afficher_comparaison_joueurs(donnees):
    joueurs_selectionnes = extraire_donnees_joueurs_selectionnes()
    joueur1, joueur2 = lignes_comparaison(joueurs_selectionnes)

    if joueur1 is None or joueur2 is None:  
        st.info("Selectionner 2 joueurs à comparer")
        return
    
    colonnes = st.columns(3)
    with colonnes[0]:
        afficher_fiche_joueur(joueur1, "1F534")
    with colonnes[1]:
        statistiques_radar = toggle()
        afficher_radarplot(joueur1, joueur2, statistiques_radar)
    with colonnes[2]:
        afficher_fiche_joueur(joueur2, "1F7E2")





def lignes_comparaison(joueurs_selectionnes):
    joueur0 = None
    joueur1 = None
    if joueurs_selectionnes is None:
        return None, None
    
    if len(joueurs_selectionnes) > 0:
        joueur0 = joueurs_selectionnes[0]

    if len(joueurs_selectionnes) == 1:
        joueur1 = calculer_joueur_moyen()

    if len(joueurs_selectionnes) > 1:
        joueur1 = joueurs_selectionnes[1]

    if len(joueurs_selectionnes) >2:
        st.info(f"Vous avez selectionné {len(joueurs_selectionnes)} joueurs, mais ne pouvez en comparer que 2")

    return joueur0, joueur1



