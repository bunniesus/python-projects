def getCoordinates(city):

    return latitude, longitude
    pass

def getWeather(latitude, longitude):
    pass

def displayWeather(weather):  # doesn't create weather onnly displays it
    pass

def main():
    city = input("Enter city: ")
    latitude, longitude = getCoordinates(city) # a func can return 2 things

    weather = getWeather(latitude, longitude)

    displayWeather(weather)


    pass

main()
    