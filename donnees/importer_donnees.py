from pathlib import Path
import streamlit as st
import pandas as pd
from donnees.constantes import CHEMIN_DONNEES



def importer_donnees():
    if CHEMIN_DONNEES is not None and Path(CHEMIN_DONNEES).exists():
        donnees = pd.read_csv(CHEMIN_DONNEES, sep=",")
        return donnees
    else:
        st.caption("erreur fichier CSV introuvable")
        return None


