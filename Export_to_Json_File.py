import json
#ici nous devons définir un tableau qui contiendra d'autres tableaux
#[[ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...], 
# [ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# ... ]
"""tab = []
with open("Path_File", 'r') as file:
        for line in file:
            parts = line.split()
            tab.append(parts)

#print(tab)
a=tab       """
#Cette fonction demande en paramètre une liste de listes de données ici nommé a par le pregramme ci dessus
#Elle demande aussi un nom de fichier de destination
def exportToJSONFile(liste = a, fileNameDest = "Path_File"):
    IP = 0
    DATE = 3
    UTC = 4             #on définit la position de chaque donnée dans la liste
    METHOD = 5
    URL = 6
    PROTOCOL = 7
    CODE = 8
    SIZE = 9
    DOMAIN = 10
    SYSTEM = 11
    ENGINE = 12
    BROWSER = 13

    json_log = []
    jsonTxt = '[\n'

    for i in range(len(liste)):
        if liste[i][IP] not in json_log and liste[i][IP] not in ["127.0.0.1"]:
            json_log.append(liste[i][IP])
            if len(liste[i]) >= 14:
                if i == 0:
                    jsonTxt += '{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code": "' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '", \n\t\t\t"domain": "' + str(
                        liste[i][DOMAIN]).replace('"', "") + '", \n\t\t\t"system": "' + str(
                        liste[i][SYSTEM]).replace('"', "") + '", \n\t\t\t"engine": "' + str(
                        liste[i][ENGINE]).replace('"', "") + '",\n\t\t\t"browser": "' + str(
                        liste[i][BROWSER]).replace('"', "") + '" }'
                else:
                    jsonTxt += ',{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code":" ' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '", \n\t\t\t"domain": "' + str(
                        liste[i][DOMAIN]).replace('"', "") + '", \n\t\t\t"system": "' + str(
                        liste[i][SYSTEM]).replace('"', "") + '", \n\t\t\t"engine": "' + str(
                        liste[i][ENGINE]).replace('"', "") + '", \n\t\t\t"browser": "' + str(
                        liste[i][BROWSER]).replace('"', "") + '" }'
            else:
                if i == 0:
                    jsonTxt += '{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code": "' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '" }'
                else:
                    jsonTxt += ',{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code":" ' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '" }'

        else:
            continue

    jsonTxt += "\n]"

    # Ecriture fichier GeoJson
    jsonFile = open(fileNameDest, "a")
    jsonFile.write(jsonTxt)
    jsonFile.close()
exportToJSONFile()
