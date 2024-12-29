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
d["Cas"].append("Peugeot")
print(d)
print(d["Fruits"])
print(d["Cars"])
print(d["Legumes"])

# ------------------------------------------------------------------------------------
