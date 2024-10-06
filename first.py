# funkce vypise "Cislo X je sude" pokud je cislo sude a "Cislo X je liche"pokud je cislo liche
def  sudy_nebo_lichy(číslo):
    if číslo % 2 == 0:
        print(f"Cislo {číslo} je sudé ")
    else:
        print(f"Number {číslo} je liché")

#Zavolání funkce s příklady
sudy_nebo_lichy(5)
"Cislo 5 je liche"
sudy_nebo_lichy(1000000)
"Cislo 1000000 je sude"