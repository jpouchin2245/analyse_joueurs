import streamlit as st
from composants.sidebar.filtres_sidebar import afficher_filtres
from donnees.tester_donnees import tester_donnees

def afficher_sidebar():
    if tester_donnees():
        entete_sidebar()
        afficher_filtres()


def entete_sidebar():
    st.sidebar.title("Filtres")
    st.sidebar.divider()
    


