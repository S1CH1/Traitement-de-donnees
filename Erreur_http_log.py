tab = []
a, b, c, d, e, f, g, h, i, j = ['200'], ['301'], ['400'], ['304'], ['500'], ['302'], ['404'], ['206'], ['401'], ['403']
A1 = B1 = C1 = D1 = E1 = F1 = G1 = H1 = I1 = J1 = 0
import time
def http(log_file_path = "Path_File"):
    
    global A1, B1, C1, D1, E1, F1, G1, H1, I1, J1
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                nav = parts[8:9]
                print(f"nombre d'erreur http: {nav}.")
                if nav == a :
                    A1 += 1
                if nav == b :
                    B1 += 1
                if nav == c :
                    C1 += 1
                if nav == d :
                    D1 += 1
                if nav == e :
                    E1 += 1
                if nav == f :
                    F1 += 1
                if nav == g :
                    G1 += 1
                if nav == h :
                    H1 += 1
                if nav == i :
                    I1 += 1
                if nav == j :
                    J1 += 1
                
                
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
        print(f"{a} : {A1} {nl} {b} : {B1} {nl} {c} : {C1} {nl} {d} : {D1} {nl} {e} : {E1} {nl} {f} : {F1} {nl} {g} : {G1} {nl} {h} : {H1} {nl} {i} : {I1} {nl} {j} : {J1}")
                
http()  
