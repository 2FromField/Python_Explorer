# Compter le nombre d'itérations de chaque lettres dans un string
sentence = "hello my name is tim"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

# Ressortir le top 3 des lettres les plus représentées dans un string
from collections import Counter

normalized_words = sentence.lower().replace(" ", "")
counter = Counter(normalized_words)
top_three = counter.most_common(3)
print(top_three)

# Add a tabs in string
print("This string \thas a tab")
