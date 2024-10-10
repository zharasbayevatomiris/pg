# funkce vypise "Cislo X je sude" pokud je cislo sude a "Cislo X je liche"pokud je cislo liche
def  sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print("Cislo", cislo, "je sudé ")
    else:
        print("Cislo", cislo, "je liché")

#Zavolání funkce s příklady
cislo = int(input('Zadejte číslo:'))
sudy_nebo_lichy(cislo)



