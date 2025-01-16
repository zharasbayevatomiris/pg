import requests

# API klíč pro OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    # Sestavení URL pro API volání
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Odeslání GET požadavku
    response = requests.get(url)
    
    # Pokud požadavek proběhl úspěšně (status kód 200)
    if response.ok:
        # Načtení JSON dat
        data = response.json()
        
        # Získání teploty v Kelvinech
        kelvin_temp = data['main']['temp']
        
        # Převod teploty na °C a zaokrouhlení na dvě desetinná místa
        celsius_temp = round(kelvin_temp - 273.15, 2)
        
        return celsius_temp
    else:
        # V případě chyby při získávání dat (např. špatné město)
        raise Exception("Failed to fetch weather data")

# Unit testy
from unittest.mock import patch, MagicMock

def test_fetch_weather_data():
    mock_response = {
        "main": {
            "temp": 293.15  # Teplota v Kelvinech
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        assert fetch_weather_data("Prague") == 20.0  # 293.15 K = 20.0 °C

if __name__ == "__main__":
    city = input("Enter city name: ")
    try:
        temperature = fetch_weather_data(city)
        print(f"Current temperature in {city}: {temperature} °C")
    except Exception as e:
        print(f"Error: {e}")