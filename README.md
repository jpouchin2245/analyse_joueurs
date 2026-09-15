# Analyse des joueurs

Application Streamlit en français avec trois onglets : **Statistiques**, **Corrélations** et **Comparaison des joueurs**. La barre latérale permet de charger un CSV, de choisir les colonnes et de filtrer les équipes, joueurs et indicateurs.

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Sans fichier chargé, l'application utilise `constants/joueurs_exemple.csv`, un jeu de données fictif. Un CSV personnel doit contenir une colonne identifiant les joueurs et au moins une colonne numérique. Une colonne d'équipe est facultative. Les noms des colonnes se choisissent dans la barre latérale.
