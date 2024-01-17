import folium

# Fonction pour géolocaliser une adresse IP en utilisant l'API ip-api.com
def getIP_infos(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    time.sleep(1.5)  # Pause pour respecter la limite de requêtes de l'API
    return data

# Fonction pour lire le fichier de logs Apache, extraire les adresses IP et les géolocaliser
#le programme est bad long dcp j'ai créé un autre fichier log plus court log.log pour tester
def traitement_de_donnees(log_file_path = "/Users/sachaveillon/Desktop/IUT/prog/log.log"):
    tab1 = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                ip = parts[0]
                ip_address = ip
                # Géolocaliser l'adresse IP
                data = getIP_infos(ip_address)
                nl = "\n"
                print(f'IP: {ip_address},{nl} Pays: {data["country"]},{nl} Ville: {data["city"]},{nl} ISP: {data["isp"]},{nl} Latitude: {data["lat"]},{nl} Longitude: {data["lon"]}')
                tab1.append([ip_address, data["lat"], data["lon"]])
    return tab1

aba = traitement_de_donnees()


#Créer une carte centrée sur les coordonnées GPS indiquée
carte= folium.Map(location=[43.920044, 5.051804])

for i in range(len(aba)):
    folium.Marker([aba[i][1], aba[i][2]],popup= aba[i][0],icon=folium.Icon(color='green')).add_to(carte)
#Sauvegarder cette carte dans un fichier HTML
carte.save('Carte1.html')
