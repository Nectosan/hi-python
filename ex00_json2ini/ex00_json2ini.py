import json
import configparser
import os

config = configparser.ConfigParser()

file = "jsons.json"

if (os.path.exists(file)):

    f = open('json.json',)

    data = json.load(f)
 
    for i in data.keys():
        config[i]= data.get(i)

    with open('example.ini', 'w') as configfile:
        config.write(configfile)

    f.close()

else :
    print("le fichier n'existe pas")