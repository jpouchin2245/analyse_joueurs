import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from donnees.donnees_filtrees import obtenir_donnees_filtrees


def afficher_scatterplot():
    variable_x = st.session_state.get("la variable X")
    variable_y = st.session_state.get("la variable Y")
    if tester_variables(variable_x, variable_y):
        donnees = obtenir_donnees_filtrees()[[variable_x, variable_y]]
        creer_scatterplot(donnees, variable_x, variable_y)
        return donnees

def tester_variables(variable_x, variable_y):
    if variable_x and variable_y and variable_x != variable_y:
        return True
    st.warning("Veuillez sélectionner deux variables distinctes.")
    return False

def creer_scatterplot(donnees, variable_x, variable_y):
    fig, ax = plt.subplots(figsize=(15, 6))
    sns.regplot(ax=ax, data=donnees, x=variable_x, y=variable_y, scatter_kws={"alpha": .3}, line_kws={"color": "red"})
    ax.set_xlabel(variable_x)
    ax.set_ylabel(variable_y)
    st.pyplot(fig)
 