import streamlit as st
from donnees.donnees_filtrees import obtenir_donnees_filtrees

def afficher_chiffres_cles():
    donnees_filtrees = obtenir_donnees_filtrees()
    variable = st.session_state.variable_selectionnee
    indicateurs = calculer_indicateurs(donnees_filtrees, variable)
    st.markdown("Chiffres clés")
    afficher_indicateur(indicateurs)

def afficher_indicateur(indicateurs):
    for colonne, (nom, valeur) in zip(st.columns(7), indicateurs.items()):
        with colonne.container(border=True):
            st.metric(nom, valeur)

    
def calculer_indicateurs(donnees, variable):
    return {
        "Nombre de joueurs": str(donnees[variable].size),
        "Min": f"{donnees[variable].min():.2f}",
        "Q1": f"{donnees[variable].quantile(0.25):.2f}",
        "Mediane": f"{donnees[variable].median():.2f}",
        "Moyenne": f"{donnees[variable].mean():.2f}",
        "Q3": f"{donnees[variable].quantile(0.75):.2f}",
        "Max": f"{donnees[variable].max():.2f}",
    }