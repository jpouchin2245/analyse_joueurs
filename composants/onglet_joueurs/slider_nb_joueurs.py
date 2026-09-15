import streamlit as st



def afficher_slider_nb_joueurs(max):
    st.session_state.nb_joueurs = st.slider("Nombre de joueurs", min_value=1, max_value=max, value=50)