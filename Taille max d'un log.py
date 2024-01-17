def taille_max(log_file_path = "Path file"):
    tab = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if not len(parts) in tab:
                tab.append(len(parts))
            else : 
                pass
    print(max(tab))
