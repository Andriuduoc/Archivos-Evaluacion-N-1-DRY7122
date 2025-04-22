import json

#Abrimos el archivo myfile.json
json_file = open('myfile.json',)

#Usamos el metodo json.load para cargar el archivo JSON en un string.
ourjson = json.load(json_file)

#Imprimimos los datos solicitados.
print(f'ACCESS TOKEN: {ourjson["access_token"]}')
print(f'Expira en: {ourjson["expires_in"]}')
print('')
print(f'REFREST TOKEN: {ourjson["refresh_token"]}')
print(f'Expira en: {ourjson["refreshtokenexpires_in"]}')

#Cerramos el archivo myfile.json
json_file.close()
