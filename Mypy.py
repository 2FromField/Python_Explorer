# pip install mypy
# Utilisation: mypy PROGRAM.py

"""
Mypy est un vérificateur de type statique pour Python.
Les vérificateurs de type aident à vous assurer que vous utilisez correctement les variables et les fonctions dans votre code.
Avec mypy, ajoutez des indices de type à vos programmes Python, et mypy vous avertira lorsque vous utilisez ces types de manière incorrecte.
Python est un langage dynamique, donc généralement vous ne verrez des erreurs dans votre code que lorsque vous essayez de l'exécuter.
Mpypy est un vérificateur statique, il trouve donc des bogues dans vos programmes sans même les éxécuter !

# Exemple outputs: 

# Mypy.py:7: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
# OR
# Success: no issues found in 1 source file
"""

def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

add("1", 2)  # Utilisation incorrecte
