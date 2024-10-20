import math

#Funkce pro kontrolu, zda je cislo prvocislo
def je_prvocislo(cislo):
    """
    Funkce oveří, zda zadané číslo je prvočíslo a vrátí True nebo False.
    Prvočíslo je takové číslo větší než 1, které není dělitelné žadným jiným číslem kromě 1 a sebe samého.
    """
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False 
    for i in range(3,int(math.sqrt(cislo)) + 1, 2):
        if cislo % i == 0:
            return False
    return True

# Funkce pro vraceni vsech prvocisel v rozsahu od 1 do maxima
def vrat_prvocisla(maximum):
    """
    Funkce spočítá všechna prvočísla v rozsahu 1 až maximum a vrátí je jako seznam.
    """
    prvocisla = []
    for num in range(2, maximum + 1):
        if je_prvocislo(num):
            prvocisla.append(num)
        return prvocisla
    
    if __name__ == "__main__":
        #Převod vstupu na celé číslo
        cislo = int(input("Zadej maximum: "))
        #Zavolání funkce pro vrácení prvočísel
        prvocisla = vrat_prvocisla(cislo)
        # Výpis výsledku
        print(prvocisla)