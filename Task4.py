def get_weather_advice(temperature):
   
    if temperature < 0:
        return "Freezing! Stay indoors and wear heavy clothing"
    elif 0 <= temperature <= 15:
        return "Cold. A jacket is recommended"
    elif 16 <= temperature <= 25:
        return "Pleasant weather! Great for outdoor activities"
    elif 26 <= temperature <= 35:
        return "Hot. Stay hydrated and use sunscreen"
    else: 
        return "Extreme heat! Avoid going outside"

if __name__ == "__main__":
    print("\n--- Smart Temperature Advisor ---")
    try:
        user_temp = float(input("Enter temperature in °C: "))
        advice = get_weather_advice(user_temp)
        print(f"Advice: {advice}")
    except ValueError:
        print("Please enter a valid numerical value.")