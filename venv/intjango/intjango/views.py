from django.http import HttpResponse

# def hi(request):
#     return HttpResponse("Hello World")

# def hello(request):
#     return HttpResponse("Welcome to Django")


# def blog_port(request, port_id):
#     return HttpResponse(f"PORT ID {port_id}")


# def greet_user(request, first_name, age):
#     return HttpResponse(f"Hello {first_name}, you are {age} years old!")

# def city_weather(request, city):
#     city = city.capitalize()  # Make it look nice
#     # Example weather messages (normally you'd get from an API)
#     weather_data = {
#         "Delhi": "Delhi is sunny with a high of 35°C.",
#         "Mumbai": "Mumbai has light rain and 28°C temperature.",
#         "Chennai": "Chennai is hot and humid at 33°C.",
#     }
    
#     message = weather_data.get(city, f"Sorry, no weather data available for {city}.")
#     return HttpResponse(message)
# # 8931964303

# def profile(request, name):
#     return HttpResponse(f"Profile for user {name}")
#     re_path(r'^user/(?P<name>[a-z][A-Z]+)/$', user, name='user') 


# def odd(request, n):
#     if n % 2 == 0:
#         return HttpResponse(f"Even number {n}")
#     else:
#         return HttpResponse(f"Odd number {n}")

# def reverse_string(request, s):  

# def diamond_pattern(request):
#     # Get the size from query parameter or use default
#     size = int(request.GET.get('size', 5))
    
#     # Generate diamond pattern
#     pattern = []
    
#     # Upper half of diamond
#     for i in range(size):
#         spaces = ' ' * (size - i - 1)
#         stars = '*' * (2 * i + 1)
#         pattern.append(spaces + stars)
    
#     # Lower half of diamond
#     for i in range(size - 2, -1, -1):
#         spaces = ' ' * (size - i - 1)
#         stars = '*' * (2 * i + 1)
#         pattern.append(spaces + stars)
    
#     # Convert pattern to HTML format
#     html_pattern = '<br>'.join(pattern)
    
#     return HttpResponse(f'''
#         <html>
#         <head>
#             <title>Diamond Pattern Generator</title>
#             <style>
#                 body {{ 
#                     font-family: monospace; 
#                     text-align: center; 
#                     margin: 50px; 
#                     background-color: #f0f0f0;
#                 }}
#                 .container {{ 
#                     background: white; 
#                     padding: 20px; 
#                     border-radius: 10px; 
#                     box-shadow: 0 0 10px rgba(0,0,0,0.1);
#                     display: inline-block;
#                 }}
#                 .pattern {{ 
#                     font-size: 20px; 
#                     line-height: 1.2;
#                     color: #333;
#                 }}
#                 .form {{ 
#                     margin: 20px 0; 
#                 }}
#                 input[type="number"] {{
#                     padding: 8px;
#                     border: 1px solid #ddd;
#                     border-radius: 4px;
#                 }}
#                 input[type="submit"] {{
#                     padding: 8px 16px;
#                     background: #007bff;
#                     color: white;
#                     border: none;
#                     border-radius: 4px;
#                     cursor: pointer;
#                 }}
#             </style>
#         </head>
#         <body>
#             <div class="container">
#                 <h1>🌟 Diamond Pattern Generator 🌟</h1>
                
#                 <div class="form">
#                     <form method="get">
#                         <label for="size">Enter diamond size:</label>
#                         <input type="number" id="size" name="size" value="{size}" min="1" max="20">
#                         <input type="submit" value="Generate">
#                     </form>
#                 </div>
                
#                 <div class="pattern">
#                     {html_pattern}
#                 </div>
                
#                 <p><small>Try different sizes from 1 to 20!</small></p>
#             </div>
#         </body>
#         </html>
#     ''')




# def home(request):
#     student = [        
#         {'name': 'John', 'is_active:' True},
#         {'name': 'Jane', 'is_active:' False},   
#     ]
#     body ={
#         'name': 'aka', 
#         'date' :date.today(),
#         'age': 20,
#         'items' :[1,2,3,4,5],
#         'all_student': student
#     }

#     return render(request, 'home.html', body)


from django.http import HttpResponse

# def user_profile(request, username):
#     return HttpResponse(f"Welcome, {username}!")


from django.http import HttpResponse

# Predefined student list (no database)
students = [
    {"id": 1, "name": "Akanksha", "age": 21},
    {"id": 2, "name": "Sidd", "age": 20},
]

def student_list(request):
    data = "<br>".join([f"{s['id']} - {s['name']}" for s in students])
    return HttpResponse(data)

def student_detail(request, id):
    for s in students:
        if s["id"] == id:
            return HttpResponse(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}",)
    return HttpResponse("Student not found!")
