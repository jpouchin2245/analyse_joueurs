import streamlit as st
from donnees.donnees_filtrees import obtenir_donnees_filtrees
import seaborn as sns



def afficher_heatmap():
    donnees_filtrees = obtenir_donnees_filtrees()
    generer_heatmap(donnees_filtrees)

def generer_heatmap(donnees):
    donnees_numeric = donnees.select_dtypes(include=["number"])
    corr = donnees_numeric.corr()
    heatmap = sns.heatmap(
    corr,
    annot=False,
    cmap="coolwarm",
    xticklabels=1,
    yticklabels=1, 
    cbar_kws={"shrink": 0.5})

    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=4)

    heatmap.tick_params(axis="x", labelsize=4)
    heatmap.tick_params(axis="y", labelsize=4)

    st.pyplot(heatmap.get_figure())