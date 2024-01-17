def navtqt(log_file_path = "Path File"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                nav = parts[11:12]
                nav2 = parts[20:21]
                nav3 = parts[22:23]
                if "Mozilla/5.0" in nav or "Firefox" in nav2 or "Chrome/95.0.4638.74" in nav2 or "Safari/537.36" in nav3:
                    print(f"nav: {nav} & {nav2} & {nav3}.")
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
                
navtqt()
