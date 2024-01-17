#ici nous devons définir un tableau qui contiendra d'autres tableaux
#[[ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...], 
# [ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# ... ]
tab = []
with open("Path_File", 'r') as file:
        for line in file:
            parts = line.split()
            tab.append(parts)

#print(tab)
a=tab[0:10]   #ici pour les test j'ai pris une petite partie des log car c'est long 
              #mais si je veux tt il suffit de remplacer par a = tab[]

def exportToCSVFile(ipliste = a, fileNameDest = "Path_File"):
    csvContent = ""
    for i in range(len(ipliste)):
        for j in range(len(ipliste[i])):
            csvContent += '"' + str(ipliste[i][j]).replace('"', '""') + '",'
        csvContent = csvContent.rstrip(',') + "\n"  # Retirez la virgule à la fin de chaque ligne
    
    # Ecriture du fichier CSV
    with open(fileNameDest, "w") as csvFile:  # Utilisation de "w" pour créer un nouveau fichier
        csvFile.write(csvContent)
exportToCSVFile()
