import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne stránku zadanou v parametru url pomocí volání response = requests.get(),
    zkontroluje návratový kód response.status_code, který musí být 200, 
    pokud ano, najde ve staženém obsahu stránky response.content všechny výskyty 
    <a href="url">odkaz</a> a z nich načte URL, které vrátí jako seznam pomocí return.
    """
    hrefs = []
    
    try:
        # Stáhneme stránku
        response = requests.get(url)
        
        # Zkontrolujeme, zda je odpověď úspěšná (status code 200)
        if response.status_code == 200:
            # Vytvoříme objekt BeautifulSoup pro analýzu HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Najdeme všechny <a> tagy s atributem href
            for link in soup.find_all('a', href=True):
                hrefs.append(link['href'])
        else:
            print(f"Chyba při stahování stránky: {response.status_code}")
    
    except Exception as e:
        print(f"Došlo k chybě při načítání URL: {e}")
    
    # Vrátíme seznam nalezených odkazů
    return hrefs

if __name__ == "__main__":
    try:
        # Přečteme URL z argumentů příkazové řádky
        url = sys.argv[1]
        # Zavoláme funkci a uložíme nalezené odkazy
        hrefs = download_url_and_get_all_hrefs(url)
        # Vytiskneme všechny nalezené odkazy
        for href in hrefs:
            print(href)
    
    except Exception as e:
        print(f"Program skončil chybou: {e}")
