# Python_Explorer

_Try anything and everything new in python_

## Librairies:

- Colorama: <br>
  Notes: <br>

  - "Fore": couleur de premier plan
  - "Back": couleur d'arrière plan
  - "Style": permet de changer le style

## Lois & Thérorèmes:

- Loi Faible des Grands Nombres: <br>
  Principe: Quand la taille de votre échantillon augmente, la moyenne empirique (observée) converge en probabilité vers la moyenne réelle de la population. <br>
  Utilité: Cela garantit que les estimations basées sur des données échantillionnées deviennent fiables à mesure que le volume de données augmente. <br>
  <br>
- Loi Forte des Grands Nombres: <br>
  Principe: Plus forte que la loi faible des grands nombres, elle assure que la moyenne empirique converge presque sûrement vers la moyenne réelle, et ce pour presque toutes les réalisations possibles. <br>
  Utilité: Vous êtes sûr que vos calculs sur des données répétées (ou simulées) reflèteront la réalité à long terme. <br>
  <br>
- Théroème Central Limite: <br>
  Principe: Peu importe la distribution d'origine de vos données, la moyenne d'un grand nombre d'échantillons suit une distribution normale. <br>
  Utilité: C'est la raison pour laquelle la normalité est si omniprésente en statistiques; elle permet de faire des ests et des intervalles de confiance, même si les données ne sont pas initialement normales. <br>

## Stats:

- Standardisation: <br>
  Objectif: Transformer les données pour qu'elles aient une moyenne nulle et une variance égale à 1. <br>
  Méthode: Chaque valeur de la donnée est transformée en soustrayant la moyenne de la variable et en divisant par l'écart-type de cette variable. <br>
  Utilisation: utilisée lorsque _les données suivent une distribution normale ou gaussienne_. Particulièrement utile pour les algorithmes basés sur les distances (comme les SVM, KNN) et ceux qui utilisent des régularisations (régressions linéaires et logistiques).
- Normalisation: <br>
  Objectif: Redimensionner les données pour qu'elles se situent dans un intervalle spécifique, souvent [0,1] ou [-1,1]. <br>
  Méthode: Chaque valeur de la donnée est transformée en soustrayant la vzaleur minimale et en divisant par l'intervalle de la variable (la différence entre la valeur maximale et minimale). <br>
  Utilisation: Utilisée lorsque _les données ne suivent pas une distribution gaussienne_ et ont des écarts significatifs en termes d'échelle. Particulièrement utile pour les réseaux de neurones et les algorithmes qui utiisent des distances (comme KNN).
-

- Interprétation d'une ACP: <br>
  PC1 = première composante principale <br>
  PC2 = deuxième composante principale <br>
  Dans l'espace PC1-PC2, LS a pour coordonnées (0.5, 0.85): la composante de PC1 est de 0.5 et celle de PC2 de 0.85 <br>
  0.85 étant supérieur à 0.5 (en absolu), cela signifie que la LS est plus importante pour PC2. <br>
  La longueur du vecteur reflète l'importance de la contribution de LS à la variance des données. Plus le vecteur est long, plus LS contribue à la variance des données dans les deux directions principales. <br>
  La direction du vecteur indique où LS contribue le plus à la variance des données. <br>

## OpenData links:

- Kaggle [https://www.kaggle.com/datasets]
- Data Gouv [https://www.data.gouv.fr/fr/datasets/]
- Google Data Search [https://datasetsearch.research.google.com]
- UCI ML Repository [https://archive.ics.uci.edu]
- Amazon Public Datasets [https://aws.amazon.com/marketplace/search/results?trk=868d8747-614e-4d4d-9fb6-fd5ac02947a8&sc_channel=el&FULFILLMENT_OPTION_TYPE=DATA_EXCHANGE&CONTRACT_TYPE=OPEN_DATA_LICENSES&filters=FULFILLMENT_OPTION_TYPE%2CCONTRACT_TYPE]

## Liens:

- Aquarel : https://medium.com/@alexroz/matplotlib-makeover-6-python-styling-libraries-for-amazing-plots-5152f16992f5
- Marimo : https://marimo.io - https://github.com/marimo-team/marimo (jupyter notebook in real time)
- Taipy : https://taipy.io (web application)

## Mémo technique:

`pip freeze > requirements.txt` : génerer le fichier requirements avec les dépendances et leur version. <br>
`python3 -m venv pyenv` : créer un environnement virtuel (macOS) <br>
`source pyenv/bin/activate` : activer l'environnement virtuel (macOS) <br>
`pip install -r requirements.txt` : importer les dépendances dans l'environnement depuis le fichier requirements
