import pandas as pd

# Création d'un dictionnaire python
data = {
    "Colonne_1": [f"Valeur_A{i}" for i in range(1, 11)],
    "Colonne_2": [i * 10 for i in range(1, 11)],
    "Colonne_3": [f"Type_{chr(65+i)}" for i in range(10)],
    "Colonne_4": [round(i * 1.5, 2) for i in range(1, 11)],
}

df = pd.DataFrame(data)  # convertir le dictionnaire en dataframe

df.to_parquet(
    "mon_fichier.parquet"
)  # sauvegarder les données quand un fichier ".parquet"
