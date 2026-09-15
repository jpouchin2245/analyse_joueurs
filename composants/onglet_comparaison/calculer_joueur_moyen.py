import streamlit as st
from donnees.donnees_filtrees import obtenir_donnees_filtrees


def calculer_joueur_moyen():
    donnees_filtrees = obtenir_donnees_filtrees()
    joueur_moyen = donnees_filtrees.mean(numeric_only=True)
    joueur_moyen["Name"] = "Joueur Moyen"
    joueur_moyen['Nation'] = ' '
    joueur_moyen['Team'] = ' '
    joueur_moyen['gender'] = ' '
    return joueur_moyen
