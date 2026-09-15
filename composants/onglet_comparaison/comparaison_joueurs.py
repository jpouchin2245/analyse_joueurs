import re

import streamlit as st
from composants.onglet_comparaison.calculer_joueur_moyen import calculer_joueur_moyen
from composants.onglet_comparaison.fiche_joueur import afficher_fiche_joueur
from composants.onglet_comparaison.radarplot import afficher_radarplot
from composants.onglet_comparaison.toggle_statistiques import toggle


def afficher_comparaison_joueurs(donnees):
    joueur1, joueur2 = extraire_donnees_joueurs(donnees)
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


def extraire_donnees_joueurs(donnees):
    event = st.session_state.get("selection_tableau", None)
    donnees_tableau = st.session_state.get("donnees_tableau", None)
    if event is None :
        return None

    lignes = event.selection.rows
    joueur0 = None
    joueur1 = None
    
    if len(lignes) > 0:
        joueur0 = donnees_tableau.iloc[lignes[0]]

    if len(lignes) == 1:
        joueur1 = calculer_joueur_moyen()

    if len(lignes) > 1:
        joueur1 = donnees_tableau.iloc[lignes[1]]

    if len(lignes) >2:
        st.info(f"Vous avez selectionné {len(lignes)} joueurs, mais ne pouvez en comparer que 2")

    return joueur0, joueur1

