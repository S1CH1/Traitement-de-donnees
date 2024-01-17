tab = []
def ip(log_file_path = "Path File"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                if not parts[0] in tab:
                    tab.append(parts[0])
                else : 
                    pass
    print(tab)
ip()
