import streamlit as st
from composants.onglet_comparaison.radarplot import afficher_radarplot

def afficher_fiche_joueur(joueur,bouton_couleur):
    with st.container(border=True):
        emoji = chr(int(bouton_couleur, 16))
        st.markdown(
            f"<div style='text-align: center; font-size: 30px; font-weight: bold;'>{emoji} {joueur['Name']}</div>",
            unsafe_allow_html=True)
        stats = joueur[["Age", "Nation","Team", "gender", "OVR","PAC","SHO","PAS","DRI","DEF","PHY"]]
        st.write(stats)