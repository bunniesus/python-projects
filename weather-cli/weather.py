import requests  #library to send HTTPS reqs 

def getCoordinates(city):

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

    response = requests.get(url)
    data = response.json()

    if "results" not in data or not data["results"]: #prevent crash
        return None

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    return latitude, longitude

def getWeather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"

    response = requests.get(url)
    data = response.json()

    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    wind = data["current"]["wind_speed_10m"]
    condition = weatherCodeToText(data["current"]["weather_code"] )

    weather = {
        "temperature" : temperature,
        "humidity" : humidity,
        "wind" : wind,
        "condition" : condition
    }
    return weather

def displayWeather(weather):  # doesn't create weather onnly displays it

    print("\n======================" )
    print("Weather Report " )
    print("======================" )
    print(f"📍 City        : {weather['city']}")
    print(f"🌡 Temperature : {weather['temperature']}°C")
    print(f"💧 Humidity    : {weather['humidity']}%")
    print(f"💨 Wind Speed  : {weather['wind']} km/h")
    print(f"☁ Condition   : {weather['condition']}")
    print("======================\n" )

def weatherCodeToText(code):

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast"
    }

    return weather_codes.get(code, "Unknown")

def main():
    city = input("Enter city: ")

    coordinates = getCoordinates(city) # a func can return 2 things
    if coordinates is None:
        print("City not found.")
        return

    latitude, longitude = coordinates

    weather = getWeather(latitude, longitude)
    weather["city"] = city

    displayWeather(weather)

def Menu():
    print("1. Select another city"
        "\n2. Exit")
    
while True:
    main()
    Menu()
    choice = int(input("Choose an option : "))
    if choice == 1:
        pass
    elif choice == 2:
        print("Exiting... ")
        break
    else : 
        print("Invalid choice!")
