from pathlib import Path
import streamlit as st
import pandas as pd
from decouple import config



def importer_donnees():
    fichier = config("CHEMIN_DONNEES")
    if fichier is not None and Path(fichier).exists():
        donnees = pd.read_csv(fichier, sep=",")
        return donnees
    else:
        st.caption("erreur fichier CSV introuvable")
        return None


