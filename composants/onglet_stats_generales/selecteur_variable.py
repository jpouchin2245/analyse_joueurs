import streamlit as st


def selecteur_variable():
    donnees = st.session_state.get("donnees")
    colonnes = donnees.select_dtypes(include="number").columns.tolist()
    st.session_state.variable_selectionnee = st.selectbox("Choisir une variable", colonnes)