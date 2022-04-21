import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
phone_number=phonenumbers.parse("+6281389166337")
print(geocoder.description_for_number(phone_number,"en"))
print(carrier.name_for_number(phone_number,"en"))