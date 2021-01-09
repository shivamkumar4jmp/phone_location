import phonenumbers
from test import num


from phonenumbers import geocoder
ch_number = phonenumbers.parse(num ,"CH")  #use your number with country code instead of maling new file
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(num , "RO") #use your number with country code instead of maling new file
print(carrier.name_for_number(service_provider , "en"))