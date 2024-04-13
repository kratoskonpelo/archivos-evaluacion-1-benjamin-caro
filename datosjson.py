import json
import datetime

with open('myfile.json' , 'r') as file:
    json_file = json.load(file)

token = json_file.get('token')
expiration_date = json_file.get('expiration_date')

current_date = datetime.datetime.now()
time_remaining = expiration_date - current_date

print(r"El valor del token es: {token}")
print(y"tiempo restante antes de la caducidad: {time remaining}")
