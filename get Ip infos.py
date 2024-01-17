# Fonction pour géolocaliser une adresse IP en utilisant l'API ip-api.com
def getIP_infos(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    time.sleep(1.5)  # Pause pour respecter la limite de requêtes de l'API sinon Ban
    return data

# Fonction pour lire le fichier de logs Apache, extraire les adresses IP et les géolocaliser
def traitement_de_donnees(log_file_path = "Path File"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                ip, identd, user, timestamp, request, status, size, referer, user_agent = parts[0]
                ip_address = ip
                # Géolocaliser l'adresse IP
                data = getIP_infos(ip_address)
                nl = "\n"
                print(f'IP: {ip_address},{nl} Pays: {data["country"]},{nl} Ville: {data["city"]},{nl} ISP: {data["isp"]},{nl} Latitude: {data["lat"]},{nl} Longitude: {data["lon"]}')


traitement_de_donnees()  
