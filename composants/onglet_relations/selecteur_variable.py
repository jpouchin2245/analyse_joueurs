import streamlit as st


def selecteur_variable(nom_variable):
    liste_variables_numeriques = st.session_state.get("donnees").select_dtypes(include=["number"]).columns.tolist()
    st.session_state[nom_variable] = st.selectbox(
        f"Sélectionnez {nom_variable}",
        options=liste_variables_numeriques
    )