import sys
import csv



def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data.append(row)
    return data 


def spoj_data(*data):
    vysledek = {}
    for d in data:
        for i, v in enumerate(d):
            if i == 0:
                continue
            if v[1] not in vysledek:
                vysledek[v[1]] = v 
            else: 
                vysledek[v[1]].extend(v)
    return vysledek
   


def zapis_csv(soubor, data):
    pass


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledny_exel.csv)
    except IndexError:
        print("Zadej 2 vstupni soubory typu csv")