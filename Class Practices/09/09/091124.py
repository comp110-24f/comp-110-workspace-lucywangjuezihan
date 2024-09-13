def get_weather_report() -> str:
    """Use input weather to prompt actions"""
    # use the "data_name: data_type = value" format
    # after conditional statements, use parentheses to put in the value
    weather: str = input("What is the weather? ")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())
