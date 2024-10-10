# funkce vrati treti prvek ze seznamu
#def vrat_treti(seznam):
 #   if len(seznam) < 3:
  #      return None 
 # else:
 #   return seznam[2]

# funkce spocita prumer z hodnot v seznamu
 def udelej_prumer(seznam):
    return sum(seznam) / len(seznam)
  

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    jmeno = slovnik["jmeno"]
    prijmeni = slovnik["primeni"]
    vek = slovnik["vek"]

    znamky = slovnik["znamky"]
    znamky = round(udelej_prumer(znamky))
    return f"Jmeno: {jmeno},primeni: {primeni},Vek:{vek}Prumerna znamka:{znamky}"




if __name__ == "__main__":
 #    vysledek = vrat_treti(seznam)
   # print(vysledek)


 # obvalka = [9,8,7,6,5]
 # vysledek = udelej_prumer(obalka)
 # print(vysledek)


    #print(udelej_prumer([9,8,7,6,5]))     #vrati 7
    student = {
        "jmeno": "Matej",
        "prijmeni": "Dvorak",
        "vek" : 21,
        "znamky" : [1,2,1,1,3,2]

    }

    vysledek = naformatuj_text(student)
    print(vysledek)


    student["vek"] # -> 21
    student["znamky"] # -> [1,2,1,1,3,2]
    student["znamky"] # -> 1

     a = 1
     f"Naformatovany retezes s hodnotou {a}" # "Naformatovany retezes s hodnotou 1"
    print(udelej_prumer(["a"]))  
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))