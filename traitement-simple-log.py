def traitement_de_donnees(log_file_path = "/Users/sachaveillon/Desktop/IUT/prog/controltower_access.log"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                ip, identd, user, date, utc, method, url, protocol, code, size = parts[:10]
                print(f"IP: {ip} {nl} Date: {date}{nl} UTC: {utc}{nl} method: {method}{nl} Url: {url}{nl} Protocol: {protocol},{nl} Code: {code},{nl} size: {size}")
                time.sleep(15)  # import time
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
#traitement_de_donnees()   """ ici on a un exemple d'utilisation de la fonction, il suffit
