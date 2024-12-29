import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+33631206262")
print(geocoder.description_for_number(phone_number, "en"))
