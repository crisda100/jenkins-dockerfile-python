import requests

def get_weather(api_key, city):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make the GET request to the API
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        temp_celsius = data['main']['temp']
        return temp_celsius
    else:
        print(f"Error getting data for {city}. Status code: {response.status_code}")
        return None

def main():
    # API key OpenWeatherMap
    api_key = "2a9777d4b8013f50a7505792808b21ca"

    # Cities to consult
    cities = ["New York", "Madrid", "Paris", "Medellin"]

    # Get and display the temperature in Celsius for each city
    for city in cities:
        temp = get_weather(api_key, city)
        if temp is not None:
            print(f"La temperatura en {city} is {temp}°C")

if __name__ == "__main__":
    main()
