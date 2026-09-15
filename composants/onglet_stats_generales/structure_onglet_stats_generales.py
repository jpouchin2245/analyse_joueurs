import streamlit as st
from donnees.tester_donnees import tester_donnees
from composants.onglet_stats_generales.selecteur_variable import selecteur_variable
from composants.onglet_stats_generales.chiffres_cles import afficher_chiffres_cles
from composants.onglet_stats_generales.histogramme import afficher_histogramme


def afficher_onglet_stat_generales():
    if not tester_donnees():
        return None

    with st.container(border=True):
        selecteur_variable()

    with st.container(border=True):
        afficher_chiffres_cles()

    with st.container(border=True):
        afficher_histogramme()


