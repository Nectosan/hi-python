import csv, json


f = open('sample.json',)

data = json.load(f)
isArray=False

#on regarde si le json qu'on reçoit est un array ou un objet, si c'est un objet on effectue les opérations nécessaires afin de récupérer les clés et valeurs
if isinstance(data, dict):
    for key in data.keys() :
        list=data[key]
        header=data[key][0].keys()
        
#on récupére les clés si le json est un array
else:
    header = data[0].keys()
    isArray=True

with open('csv.csv', 'w', encoding='UTF8', newline='') as f:

    writer = csv.writer(f,delimiter=";")

    # write the header
    writer.writerow(header)

    # write the data
    if (isArray is False):
        for i in range(len(list)):
            writer.writerow(data[key][i].values())
    else:
        for i in (data):
            writer.writerow(i.values())