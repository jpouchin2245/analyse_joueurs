import streamlit as st
from donnees.donnees_filtrees import obtenir_donnees_filtrees
import seaborn as sns
import matplotlib.pyplot as plt

def afficher_histogramme():
    donnees_filtrees = obtenir_donnees_filtrees()
    variable = st.session_state.variable_selectionnee
    
    fig, ax = plt.subplots(figsize=(15, 6))
    sns.histplot(donnees_filtrees[variable], bins=20, kde=False, ax=ax)
    ax.set_title(f"Histogramme de {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Fréquence")
    st.pyplot(fig)