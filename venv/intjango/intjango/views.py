from django.http import HttpResponse

def hi(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("Welcome to Django")


def blog_port(request, port_id):
    return HttpResponse(f"PORT ID {port_id}")


def greet_user(request, first_name, age):
    return HttpResponse(f"Hello {first_name}, you are {age} years old!")

def city_weather(request, city):
    city = city.capitalize()  # Make it look nice
    # Example weather messages (normally you'd get from an API)
    weather_data = {
        "Delhi": "Delhi is sunny with a high of 35°C.",
        "Mumbai": "Mumbai has light rain and 28°C temperature.",
        "Chennai": "Chennai is hot and humid at 33°C.",
    }
    
    message = weather_data.get(city, f"Sorry, no weather data available for {city}.")
    return HttpResponse(message)
# 8931964303