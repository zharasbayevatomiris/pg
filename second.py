def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    return "dvacet pět"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
#ukol 2
def cislo_text(cislo):
    cisla = {
        "0": "nula",
        "1": "jedna",
        "2": "dva",
        "3": "tři",
        "4": "čtyři",
        "5": "pět",
        "6": "šest",
        "7": "sedm",
        "8": "osm",
        "9": "devět",
        "10": "deset",
        "11": "jedenáct",
        "12": "dvanáct",
        "13": "třináct",
        "14": "čtrnáct",
        "15": "patnáct",
        "16": "šestnáct",
        "17": "sedmnáct",
        "18": "osmnáct",
        "19": "devatenáct",
        "20": "dvacet",
        "30": " třicet",
        "40": "čtyřicet",
        "50": "padesát",
        "60": "šedesát",
        "70": "sedmdesát",
        "80": "osmdesát",
        "90": "devadesát",
        "100": "sto"
        }

    if cislo in cisla:
            return cisla[cislo]
    else:  
        #Pro čísla od 21 do 99
        if 21 <= int(cislo) < 100:
            desitky = int(cislo) // 10 * 10     #Ziskani desitky
            jednotky = int(cislo) % 10          #Ziskani jednotky
            if jednotky == 0: 
                return cisla[str(desitky)]
            else:
                return cisla[str(desitky)] + " " + cisla[str(jednotky)]
        return "Neznámé číslo"                  #Pokud číslo není platné

#přiklad použití 
if __name__ == "__main__":
    cislo = input ("Zadejte číslo:  ")          #User zadá číslo
    text = cislo_text(cislo)                    #Volání funkce
    print(text)                                 #Výstup textové reprezentace čísla 
                          


            
