import re

# Diviser des chaônes selon des motifs
text = "pommes,bananes;cerises,dates;figues"
fruits = re.split(r"[,;]", text)
print(fruits)

# Remplacer des motifs
text = "Trop      d'espaces entre    les mots"
clean = re.sub(r"\s+", " ", text)
print(clean)

# Extraire des motifs spécifiques
text = "Contactez-nous à support@example.com ou info@compagny.org"
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
print(emails)

# Supprimer des caractères indésirables
text = "Contacts: (+33) 6 12 34 56 78, +33 1 23 45 67 78"  # numéro de téléphone FR
clean = re.sub(r"[() ]", "", text)  # nettoie les numéros en conservant le "+33"
clean = re.sub(r"\+33(\d)", r"0\1", clean)  # remplace le "+33" par "0" au début
print(clean)


# Valider des formats de données
def validate_email(email):
    pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"
    return bool(re.match(pattern, email))


print(validate_email("user@example.com"))
print(validate_email("invalid_email"))
