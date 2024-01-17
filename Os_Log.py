def ostqt(log_file_path = "Path File"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                os = parts[12:17]
                print(f"Os: {os}.")
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
ostqt()
