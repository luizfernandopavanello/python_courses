import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato +5511123456789: ' )
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))