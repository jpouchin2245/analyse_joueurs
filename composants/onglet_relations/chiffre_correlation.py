import streamlit as st


def afficher_chiffre_correlation():
    variable_x = st.session_state.get("la variable X")
    variable_y = st.session_state.get("la variable Y")
    if variable_x and variable_y and variable_x != variable_y:
        correlation = st.session_state.get("donnees")[[variable_x, variable_y]].corr().iloc[0, 1]
        st.metric(label="Correlation", value=f"{correlation:.2f}")