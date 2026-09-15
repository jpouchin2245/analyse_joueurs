import streamlit as st
import matplotlib.pyplot as plt
from composants.onglet_relations.scatterplot import afficher_scatterplot
from donnees.tester_donnees import tester_donnees
from composants.onglet_relations.heatmap import afficher_heatmap
from composants.onglet_relations.selecteur_variable import selecteur_variable
from composants.onglet_relations.chiffre_correlation import afficher_chiffre_correlation
from donnees.donnees_filtrees import obtenir_donnees_filtrees

def afficher_onglet_relations():
    if not tester_donnees():
        return None

    with st.expander("Matrice de corrélation"):
        afficher_heatmap()

    with st.container(border=True):
        afficher_selecteurs_relation()

    with st.container(border=True):
        afficher_scatterplot()




def afficher_selecteurs_relation():
    colonnes = st.columns(3)
    with colonnes[0]:
        selecteur_variable("la variable X")
    with colonnes[1]:
        selecteur_variable("la variable Y")
    with colonnes[2]:
        afficher_chiffre_correlation()