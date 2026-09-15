import streamlit as st


def tester_donnees():
    if "donnees" not in st.session_state:
        st.sidebar.caption("Les données ne sont pas encore chargées.")
        return False
    return True