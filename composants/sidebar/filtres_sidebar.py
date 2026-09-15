import streamlit as st
from donnees.constantes import STATISTIQUES_PAR_POSTE

def afficher_filtres():
    selecteur("League")
    selecteur("Position")
    selecteur("gender")
    slider_age()
    sliders_statistiques()


def selecteur(variable): 
    liste_valeurs = st.session_state.donnees[variable].unique().tolist()
    liste_valeurs.insert(0, "Tout selectionner")
    st.session_state[variable] = st.sidebar.selectbox(f"Sélectionnez {variable}", liste_valeurs)

def sliders_statistiques():
    st.session_state.liste_statistiques = STATISTIQUES_PAR_POSTE.get(st.session_state.Position, [])
    for statistique in st.session_state.liste_statistiques:
        slider(statistique)

def slider_age():
    slider("Age", min_value=17, max_value=50, value=50, label="Âge maximum")



def slider(statistique, min_value=0, max_value=100, value=0, label=None):
    if label is None:
        label = statistique
        
    st.session_state[statistique] = st.sidebar.slider(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value
    )