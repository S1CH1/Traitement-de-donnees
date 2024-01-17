#Code à modifier en fonction de ce que l'on souhaite
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

def courbes(log_file_path = "Path File"):
    # Initialiser un dictionnaire pour compter le nombre de requêtes par date
    requetes_par_date = defaultdict(int)

    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                timestamp = parts[3][1:]  # Supprimer le premier caractère '['
                date = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")  # Convertir la chaîne de caractères en date
                requetes_par_date[date.date()] += 1  # Incrémenter le compteur pour cette date

    # Créer une liste de dates et une liste de nombres de requêtes
    dates = sorted(requetes_par_date.keys())
    requetes = [requetes_par_date[date] for date in dates]

    # Créer un graphique
    plt.plot(dates, requetes)
    plt.xlabel('Date')
    plt.ylabel('Nombre de requêtes')
    plt.title('Nombre de requêtes par date')
    plt.show()

courbes()  
