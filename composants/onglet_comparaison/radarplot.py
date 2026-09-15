import plotly.graph_objects as go
import streamlit as st







def afficher_radarplot(joueur1, joueur2, variables):
    valeurs1 = [joueur1[stat] for stat in variables]
    valeurs2 = [joueur2[stat] for stat in variables]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=valeurs1,
            theta=variables,
            fill="toself",
            opacity=0.5,
            fillcolor="rgba(255, 0, 0, 0.5)"

        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=valeurs2,
            theta=variables,
            fill="toself",
            opacity=0.5, 
            fillcolor="rgba(0, 255, 0, 0.5)"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)