def exportToXMLFile(ipliste = a, balisesName = ["ip", "rien", "rien", "date", "fuseau_horaire", "method", "url", "protocol", "return_code", "size", "rien","domain", "system", "engine", "browser"], fileNameDest = "/Users/sachaveillon/Desktop/IUT/prog/tqtmongarsthierry15.xml" ):
    xmlContent = "<ROOT>\n"
    for i in range(len(ipliste)):
        xmlContent += "\t<ADDRESS>\n"
        for j in range(len(balisesName)):
            # Assurons-nous que l'index j existe dans la liste balisesName
            if j < len(ipliste[i]):
                xmlContent += '\t\t<' + balisesName[j] + '>' + str(ipliste[i][j]).replace("&", "&amp;") + '</' + balisesName[j] + '>\n'
        xmlContent += "\t</ADDRESS>\n"
    xmlContent += "</ROOT>\n"
    
    # Ecriture du fichier XML
    with open(fileNameDest, "w") as xmlFile:  # Utilisation de "w" pour créer un nouveau fichier
        xmlFile.write(xmlContent)
exportToXMLFile()
