import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+91730092896")
phone_number2 = phonenumbers.parse("+919994428968")
phone_number3 = phonenumbers.parse("+919842602896")
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));

#LETS TRACK PHONE NUMBER
