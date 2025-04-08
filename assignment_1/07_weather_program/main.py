import requests
from datetime import datetime

def get_weather(location):
    """Fetch weather data from a free API endpoint"""
    try:
        # Using a free weather API that doesn't require keys
        response = requests.get(f"https://goweather.herokuapp.com/weather/{location}")
        response.raise_for_status()
        data = response.json()
        
        # Check if we got valid data
        if 'temperature' not in data or 'description' not in data:
            print(f"Weather data not available for {location}")
            print("Try major world cities like: London, Paris, Tokyo")
            return
            
        print(f"\nWeather for {location} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("----------------------------------")
        print(f"Temperature: {data['temperature']}")
        print(f"Wind: {data['wind']}")
        print(f"Description: {data['description']}")
        print("----------------------------------")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        print("Please check your internet connection")

def main():
    print("🌦️ Weather Information Program 🌦️")
    print("----------------------------------")
    print("Works for most major world cities\n")
    
    while True:
        try:
            location = input("Enter city name (or 'quit'): ").strip().title()
            
            if location.lower() == 'quit':
                print("Goodbye! 👋")
                break
                
            if not location.replace(" ", "").isalpha():
                print("Please enter a valid city name (letters only)")
                continue
                
            get_weather(location)
            
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            break

if __name__ == "__main__":
    main()