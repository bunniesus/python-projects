import requests #library to send HTTPS reqs 

def getCoordinates(city):
    pass

def getWeather(latitude, longitude):
    pass

def displayWeather(weather):  # doesn't create weather onnly displays it

    print("\nToday's Weather " )
    print("City: ", weather["city"])
    print("Temperature: ", weather["temperature"])
    print("Humidity: ", weather["humidity"])
    print("Wind: ", weather["wind"])
    print("Condition: ", weather["condition"])


def main():
    city = input("Enter city: ")
    latitude, longitude = getCoordinates(city) # a func can return 2 things

    weather = getWeather(latitude, longitude)

    displayWeather(weather)


    pass

main()
    