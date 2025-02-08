# Compter le nombre d'itérations de chaque lettres dans un string
sentence = "hello my name is tim"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

# ------------------------------------------------------------------------------------


# Ressortir le top 3 des lettres les plus représentées dans un string
from collections import Counter

normalized_words = sentence.lower().replace(" ", "")
counter = Counter(normalized_words)
top_three = counter.most_common(3)
print(top_three)

# ------------------------------------------------------------------------------------


# Add a tabs in string
print("This string \thas a tab")

# ------------------------------------------------------------------------------------

# Utiliser GrouBy avec la création d'une nouvelle colonne nommée
import pandas as pd
import numpy as np

df = pd.DataFrame()
df["sales"] = np.random.randint(1, 100, (1000,))
df["price"] = np.random.randint(1, 100, (1000,))
df["Month"] = np.random.randint(1, 12, (1000,))
df["product"] = np.random.choice(["A", "B", "C"], (1000,))

new_df = df.groupby("Month").agg(
    vente_moyenne=("sales", "mean"),
    vente_max=("sales", "max"),
    prix_moyen=("price", "mean"),
    nb_product_disinct=("product", "nunique"),
)

print(new_df)

# ------------------------------------------------------------------------------------
from collections import defaultdict

d = defaultdict(list)
d["Fruits"].append("Kiwi")
d["Cars"].append("Peugeot")
print(d)
print(d["Fruits"])
print(d["Cars"])
print(d["Legumes"])

# ------------------------------------------------------------------------------------
# Les validations intelligentes
sentence = "Les biquettes sont roses, dans le pays du soleil"
print(sentence.isprintable())  # vérifiez si le texte est affichable sans surprise
print(sentence.isascii())  # identifiez les caractères spéciaux sans regex

# Les transformations puissantes
print(sentence.casefold())  # plus puissant que lower() pour l'international
# table = str.maketrans("e","3") # créer une table de traduction (1)
table = str.maketrans({"e": "3", "i": "1"})  # créer une table de traduction (2)
translated = sentence.translate(table)  # appliquer la traduction
print(translated)

# Manipulation intelligente
name = "Alice"
age = 30
result = "My name is {name} and I am {age} years old.".format_map(
    vars()
)  # iniection magique de toutes vos variables locales
print(result)

print(sentence.partition(", "))  # split intelligent qui garde le séparateur

# Remplacer les strips()
text = "prefix_example_suffix"
print(text.removeprefix("prefix_"))  # retirer un prefix
print(text.removesuffix("_suffix"))  # retirer un suffix

# ------------------------------------------------------------------------------------

# Mesurer et afficher le temps d'exécution d'une fonction Python
import time


# Définition du décorateur
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Début du chronométrage
        result = func(*args, **kwargs)  # Exécuter la fonction
        end_time = time.time()  # Fin du chronométrage
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result

    return wrapper


# Utilisation du décorateur
@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


# Appeler la fonction décorée
result = example_function(1000000)
print(f"Result: {result}")

# ------------------------------------------------------------------------------------

# Le décorateur @auth est souvent utilisé pour gérer l'authentification ou la vérification d'accès à une fonction
# Variable simulant l'état d'authentification
current_user = {"authenticated": False}  # Changez à True pour tester


# Définition du décorateur
def auth(func):
    def wrapper(*args, **kwargs):
        if current_user.get("authenticated"):
            print("User is authenticated. Access granted.")
            return func(*args, **kwargs)
        else:
            print("User is not authenticated. Access denied.")
            return None  # Ou lever une exception si nécessaire

    return wrapper


# Utilisation du décorateur
@auth
def sensitive_action():
    print("Performing a sensitive action!")


# Tester la fonction
sensitive_action()

# ------------------------------------------------------------------------------------
# Le décorateur @cache est utilisé pour optimiser les performances en mémorisant les résultats de fonctions coûteuses afin qu'elles ne soient pas recalculées pour les mêmes arguments

from functools import lru_cache


# Application du décorateur
@lru_cache(maxsize=128)  # maxsize limite le nombre de résultats mis en cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Utilisation de la fonction
print(fibonacci(10))  # Calcul initial
print(fibonacci(10))  # Récupéré depuis le cache


# ------------------------------------------------------------------------------------
# Walrus operator

users = [
    {"name": "Jason", "password": None},
    {"name": "Kevin", "password": "123"},
    {"name": "Dylan"},
]

for user in users:
    if secret_password := user.get("password"):
        print(f"Password found for user {user['name']} ! {secret_password}")


# ------------------------------------------------------------------------------------
# Dataclasses -> Permet de créer des classes rapidement sans initialisation
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


if __name__ == "__main__":
    user = User("Kevin", 21)
    print(f"Hey, {user.name}, what's up ?!")

# ------------------------------------------------------------------------------------
# Fusion de dictionnaires
user_info = {"name": "Alice", "age": 30}
user_prefs = {"age": 30, "theme": "dark"}

merged = {**user_info, **user_prefs}
print(merged)


# ------------------------------------------------------------------------------------
# Inverser un string
string = "lapin"
print(string[::-1])

# ------------------------------------------------------------------------------------
# Ajouter une nouvelle colonne à un dataframe avec la méthode .assign()
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# Ajouter une colonne C en fonction des valeurs de la colonne A
df2 = df.assign(Cheval=df["A"] * 2)

print(df2)

# ------------------------------------------------------------------------------------
# Filtrer avec la méthode .query()
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 15, 10, 5, 10]})

# Filtrer les lignes où A > 2
result = df.query("A > 2")
print(result)


# Libraries pyjanitor
import janitor as pj

df = pd.DataFrame(
    {
        "First Name": [1, 2],
        "Last Name ": [3, 4],
        "Birth Year": [1990, 1991],
        "B": [None, 2],
        "size": ["small", "large"],
    }
)
df_clean = df.clean_names()  # Nettoyage des noms de colonnes
