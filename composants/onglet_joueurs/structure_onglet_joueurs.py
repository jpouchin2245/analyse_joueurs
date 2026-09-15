import streamlit as st
from composants.onglet_joueurs.Affichage_joueurs_selectionnes import afficher_joueurs_selectionnes
from composants.onglet_joueurs.affichage_recherche_joueur import afficher_recherche_joueurs
from composants.onglet_joueurs.slider_nb_joueurs import afficher_slider_nb_joueurs
from donnees.donnees_filtrees import obtenir_donnees_filtrees
from donnees.tester_donnees import tester_donnees
from composants.onglet_joueurs.tableau import afficher_tableau
from composants.onglet_joueurs.joueurs_selectionnes import initialiser_selection_joueurs



def afficher_onglet_joueurs():
    if not tester_donnees():
            return None
    
    donnees = obtenir_donnees_filtrees()
    with st.container(border=True):
        afficher_slider_nb_joueurs(donnees.shape[0])
        afficher_recherche_joueurs(donnees)
        afficher_selection_joueurs(donnees)

def afficher_selection_joueurs(donnees):
    initialiser_selection_joueurs()
    afficher_joueurs_selectionnes()
    afficher_tableau(donnees)