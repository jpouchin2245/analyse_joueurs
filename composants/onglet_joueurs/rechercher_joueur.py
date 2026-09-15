import streamlit as st
import unicodedata
from composants.onglet_joueurs.joueurs_selectionnes import ajouter_joueur



def rechercher_joueurs(texte, donnees):
    recherche = normaliser_nom(texte)
    if not recherche:
        return []
    noms = donnees["Name"].fillna("").map(normaliser_nom)
    resultats = donnees[noms.str.contains(recherche, regex=False)].head(5)
    return [
        (f"{joueur['Name']} ({joueur['Team']})", joueur["url"])
        for _, joueur in resultats.iterrows()
    ]


def normaliser_nom(texte):
    texte = unicodedata.normalize("NFKD", str(texte).strip().casefold())
    return "".join(lettre for lettre in texte if not unicodedata.combining(lettre))

def ajouter_joueur_recherche(url_joueur, donnees):
    correspondances = donnees[donnees["url"] == url_joueur]
    if not correspondances.empty:
        ajouter_joueur(correspondances.iloc[0])
    st.session_state.version_recherche_joueurs += 1