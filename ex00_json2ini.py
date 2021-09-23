import json
import configparser

config = configparser.ConfigParser()

f = open('json.json',)

data = json.load(f)
 
for i in data.keys():
    config[i]= data.get(i)

with open('example.ini', 'w') as configfile:
    config.write(configfile)

f.close()