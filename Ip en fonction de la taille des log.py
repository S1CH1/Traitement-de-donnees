tab = []
def ip_taille(log_file_path = "Path File", taille = 'À remplacer par un nombre'):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == taille: 
                if not parts[0] in tab:
                    tab.append(parts[0])
                else : 
                    pass
    print(tab)
ip_taille()
