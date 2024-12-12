# ninth.py

def dev_to_bin(cislo):
    # Převod vstupního čísla na celé číslo (pokud je vstup ve formě řetězce)
    cislo = int(cislo)
    
    # Pokud je číslo 0, vrátíme "0"
    if cislo == 0:
        return "0"
    
    # Funkce pro převod na binární číslo
    vysledek = ""
    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek
        cislo = cislo // 2
    
    return vysledek
