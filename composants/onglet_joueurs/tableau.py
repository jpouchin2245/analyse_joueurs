import streamlit as st
from donnees import tester_donnees
from donnees.donnees_filtrees import obtenir_donnees_filtrees


def afficher_tableau(donnees):
    donnees = donnees.sort_values(by="OVR", ascending=False)
    limite = st.session_state.get("nb_joueurs", 50)
    st.session_state.donnees_tableau = donnees.head(limite)
    with st.container(border=True):
        st.session_state.selection_tableau = st.dataframe(
            st.session_state.donnees_tableau,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="multi-row"
            )

