import streamlit as st

from donnees.importer_donnees import importer_donnees
from composants.sidebar.structure_sidebar import afficher_sidebar
from composants.onglet_stats_generales.structure_onglet_stats_generales import afficher_onglet_stat_generales
from composants.onglet_relations.structure_onglet_relations import afficher_onglet_relations
from composants.onglet_joueurs.structure_onglet_joueurs import afficher_onglet_joueurs
from composants.onglet_comparaison.structure_onglet_comparaison import afficher_onglet_comparaison



def afficher_application():
    configurer_page()
    charger_donnees_application()
    afficher_sidebar()
    afficher_onglets()


def configurer_page():
    st.set_page_config(page_title="Analyse des joueurs", layout="wide")
    st.title("Analyse des joueurs")

def charger_donnees_application():
    st.session_state.donnees = importer_donnees()


def afficher_onglets():
    onglet_stat_generales, onglet_joueurs, onglet_comparaison, onglet_relations = st.tabs(["Statistiques générales", "Affichage des joueurs","Comparaison des joueurs", "Relations entre statistiques"])
    with onglet_stat_generales:
        afficher_onglet_stat_generales()
    with onglet_joueurs:
        afficher_onglet_joueurs()
    with onglet_relations:
            afficher_onglet_relations()
    with onglet_comparaison:
        afficher_onglet_comparaison()

if __name__ == "__main__":
    afficher_application()
