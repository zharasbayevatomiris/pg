#ukol 2
def cislo_text(cislo):
    cislo_input = str(cislo)
    cislo_int = int(cislo)
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

    if cislo_input in cisla:
            return cisla[cislo_input]
    else:  
        #Pro čísla od 21 do 99
        if 21 <= cislo_int < 100:
            desitky = cislo_int // 10 * 10     #Ziskani desitky
            jednotky = cislo_int % 10          #Ziskani jednotky
            if jednotky == 0: 
                return cisla[str(desitky)]
            else:
                return cisla[str(desitky)] + " " + cisla[str(jednotky)]
        return None                             #Pokud číslo není platné

#přiklad použití 
if __name__ == "__main__":
    cislo = 100                                 #User input
    string_cislo = ('100')                      #User input (same but  to test string input in "cislo_text" function)
    text = cislo_text(cislo)                    #Volání funkce
    print(text)                                 #Výstup textové reprezentace čísla 

            
