import streamlit as st
from composants.onglet_joueurs.slider_nb_joueurs import afficher_slider_nb_joueurs
from donnees.donnees_filtrees import obtenir_donnees_filtrees
from donnees.tester_donnees import tester_donnees
from composants.onglet_joueurs.tableau import afficher_tableau
from composants.onglet_comparaison.comparaison_joueurs import afficher_comparaison_joueurs



def afficher_onglet_joueurs():
    if not tester_donnees():
            return None
    
    donnees = obtenir_donnees_filtrees()
    with st.container(border=True):
        afficher_slider_nb_joueurs(donnees.shape[0])
        afficher_tableau(donnees)

