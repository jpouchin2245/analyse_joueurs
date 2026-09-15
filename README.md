# Analyse des joueurs

Application Streamlit en français pour explorer les statistiques de joueurs de football, rechercher des profils et comparer leurs performances. Elle propose quatre onglets reliés par une sélection commune de joueurs.

## Installation et lancement

Depuis la racine du projet, dans un environnement Python :

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Toutes les dépendances sont déclarées dans `requirements.txt`, notamment `streamlit>=1.49` pour les interactions du tableau et `streamlit-searchbox>=0.1.24` pour les suggestions de recherche.

Les bibliothèques principales sont Streamlit, Pandas, Plotly, Matplotlib, Seaborn et Streamlit Searchbox.

## Données et filtres

L'application charge le fichier local `donnees/all_players_clean.csv`. Son chemin est défini par `CHEMIN_DONNEES` dans `donnees/constantes.py`. Lancer l'application depuis la racine permet de résoudre ce chemin. Il n'y a pas de chargement de CSV depuis l'interface ni de données de remplacement automatiques.

La barre latérale permet de restreindre les données par :

- championnat (`League`) ;
- poste (`Position`) ;
- genre (`gender`) ;
- âge maximum ;
- seuils minimums de statistiques, adaptés au poste choisi.

Les filtres alimentent le tableau, la recherche, les statistiques descriptives, l'histogramme, la matrice de corrélation et le nuage de points. Ils définissent aussi la population utilisée pour calculer le joueur moyen.

## Fonctionnalités par onglet

### 1. Statistiques générales

Choisir une variable numérique pour afficher :

- le nombre de joueurs, le minimum et le maximum ;
- la moyenne, la médiane et les premier et troisième quartiles ;
- un histogramme de la répartition des valeurs en 20 classes.

**Interaction :** changer la variable ou les filtres actualise les indicateurs et l'histogramme. L'histogramme est une image statique : ses barres ne permettent pas de sélectionner des joueurs.

### 2. Affichage des joueurs

Le tableau affiche les joueurs filtrés, initialement triés par note globale (`OVR`) décroissante. Un curseur règle le nombre de lignes affichées.

Trois interactions facilitent la sélection :

- **Cliquer sur une cellule du tableau** ajoute le joueur correspondant, sans cases à cocher.
- **Saisir un nom dans la recherche** affiche jusqu'à cinq suggestions avec le nom et l'équipe. La recherche trouve aussi un fragment au milieu du nom, sans distinction de majuscules ou d'accents. Choisir une suggestion ajoute le joueur et vide la recherche.
- **Cliquer sur une vignette portant le nom d'un joueur** retire ce joueur de la sélection.

La recherche porte sur tous les joueurs correspondant aux filtres, indépendamment du nombre de lignes affichées dans le tableau. Les cinq suggestions suivent l'ordre des données.

Les vignettes sont disposées côte à côte au-dessus du tableau. Un même joueur ne peut être ajouté qu'une fois ; son URL sert d'identifiant pour distinguer les homonymes. La sélection reste disponible entre les onglets et lors des changements de filtres, pendant la session.

### 3. Comparaison des joueurs

L'onglet présente deux fiches et un graphique radar :

- **Un joueur sélectionné :** comparaison avec le « Joueur Moyen », calculé sur les données filtrées.
- **Deux joueurs sélectionnés :** comparaison de leurs profils.
- **Plus de deux joueurs :** comparaison des deux premiers dans l'ordre d'ajout, avec un message d'information.

Les fiches affichent notamment l'âge, la nationalité, l'équipe, le genre, la note globale et les six statistiques générales : vitesse (`PAC`), tir (`SHO`), passe (`PAS`), dribble (`DRI`), défense (`DEF`) et physique (`PHY`).

**Interactions du radar :** survoler les points permet de lire les valeurs. Le contrôle « Générales / Spécifiques » change les axes du radar : les statistiques spécifiques dépendent du poste choisi dans la barre latérale. L'échelle va de 0 à 100. Cliquer sur le radar n'ajoute pas de joueur à la sélection.

### 4. Relations entre statistiques

Cet onglet rassemble une matrice de corrélation et un nuage de points interactif (*scatterplot*).

**Matrice de corrélation :** ouvrir le panneau « Matrice de corrélation » pour visualiser les corrélations entre les variables numériques des données filtrées. Cette figure est statique ; cliquer sur une case ne déclenche aucune sélection.

**Interactions du scatterplot :**

- Choisir deux variables numériques distinctes pour les axes X et Y.
- Survoler un point pour afficher le nom du joueur et ses valeurs.
- Cliquer sur un point pour ajouter le joueur à la sélection commune. Une notification confirme : « Le joueur XX a été ajouté à la sélection. »
- Les joueurs sélectionnés sont mis en couleur ; les autres restent en gris et plus transparents. Un joueur déjà présent n'est pas ajouté une seconde fois.
- Utiliser les outils Plotly pour zoomer, déplacer la vue ou rétablir les axes. Cliquer sur une entrée de légende masque ou réaffiche le groupe correspondant, sans modifier la liste des joueurs sélectionnés.

Seuls les joueurs correspondant aux filtres apparaissent dans le nuage. Un joueur sélectionné peut donc rester dans la liste tout en étant absent du graphique.

**Périmètre de l'indicateur :** le chiffre « Correlation » est actuellement calculé sur l'ensemble des données chargées, alors que le scatterplot et la matrice utilisent les données filtrées.

## Exemple de parcours

1. Choisir un championnat et un poste dans la barre latérale.
2. Rechercher un joueur dans « Affichage des joueurs » et sélectionner une suggestion.
3. Explorer deux statistiques dans « Relations entre statistiques », puis cliquer sur un autre joueur intéressant.
4. Ouvrir « Comparaison des joueurs » pour comparer les deux profils.
5. Retirer un joueur en cliquant sur sa vignette pour comparer le joueur restant à la moyenne filtrée.

## Organisation du projet

- `app.py` : point d'entrée et organisation des quatre onglets.
- `composants/` : filtres, tableaux, recherche, fiches et graphiques.
- `donnees/` : CSV, chargement, filtrage et constantes.
- `composants/onglet_joueurs/rechercher_joueur.py` : recherche des correspondances et ajout du joueur choisi.
- `composants/onglet_joueurs/affichage_recherche_joueur.py` : barre de recherche et menu de suggestions, intégrés à l'onglet joueurs.
- `requirements.txt` : dépendances nécessaires à l'installation.

La sélection commune est conservée dans `st.session_state.joueurs_selectionnes`, sous forme de lignes Pandas complètes, utilisables par les fiches et les graphiques.
