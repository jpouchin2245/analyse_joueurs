import streamlit as st

def obtenir_donnees_filtrees():
    donnees = st.session_state.donnees
    for variable in ["League", "Position", "gender"]:
        donnees = filtrer_donnees_selecteurs(donnees, variable)

    for statistique in st.session_state.liste_statistiques:
        donnees = filtrer_donnees_sliders(donnees, statistique)

    donnees = filtrer_donnees_age(donnees)
    return donnees


def filtrer_donnees_selecteurs(donnees, variable):
        valeur_selectionnee = st.session_state.get(variable)
        if valeur_selectionnee and valeur_selectionnee != "Tout selectionner":
            donnees = donnees[donnees[variable] == valeur_selectionnee]
        return donnees

def filtrer_donnees_sliders(donnees, statistique):
    valeur_slider = st.session_state.get(statistique)
    if valeur_slider is not None:
        donnees = donnees[donnees[statistique] >= valeur_slider]
    return donnees

def filtrer_donnees_age(donnees):
    valeur_slider = st.session_state.get("Age")
    if valeur_slider is not None:
        donnees = donnees[donnees["Age"] <= valeur_slider]
    return donnees
