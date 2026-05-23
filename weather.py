import requests

API_KEY = "YOUR_API_KEY_HERE" 

city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    main = data["main"]
    weather = data["weather"][0]
    print(f"\n--- Weather in {city.title()} ---")
    print(f"Temperature: {main['temp']}°C")
    print(f"Feels like: {main['feels_like']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Condition: {weather['description'].title()}")
else:
    print("\nError:", data["message"])
