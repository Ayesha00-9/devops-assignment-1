def get_weather_advice(temperature):
    advice = []

    if temperature < 10:
        advice.append("Wear warm clothes.")
        advice.append("Drink hot beverages.")
    elif 10 <= temperature < 20:
        advice.append("Carry a light jacket.")
        advice.append("Weather is pleasant.")
    elif 20 <= temperature < 30:
        advice.append("Wear comfortable clothes.")
        advice.append("Stay hydrated.")
    elif 30 <= temperature < 40:
        advice.append("Stay hydrated.")
        advice.append("Wear light clothes.")
        advice.append("Avoid direct sunlight.")
    else:
        advice.append("Extreme heat warning!")
        advice.append("Drink plenty of water.")
        advice.append("Stay indoors if possible.")

    return advice


def main():
    print("=" * 40)
    print("      Weather Advice Generator")
    print("=" * 40)

    try:
        temperature = float(input("Enter temperature (°C): "))

        print("\nWeather Report")
        print("-" * 40)
        print(f"Temperature : {temperature}°C")
        print("Advice:")

        for item in get_weather_advice(temperature):
            print(f"- {item}")

    except ValueError:
        print("Please enter a valid temperature.")


if __name__ == "__main__":
    main()