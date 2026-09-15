import streamlit as st
from donnees.constantes import STATISTIQUES_PAR_POSTE


def toggle():
    if st.session_state.get("Position", None) is None:
        return STATISTIQUES_PAR_POSTE["Tout selectionner"]

    choix = st.segmented_control(
        "Statistiques de comparaison",
        options=["Générales", "Spécifiques"],
        default="Générales"
    )

    if choix == "Spécifiques":
        Position = st.session_state.get("Position", "Tout selectionner")
        return STATISTIQUES_PAR_POSTE[Position]
    else:
        return STATISTIQUES_PAR_POSTE["Tout selectionner"]