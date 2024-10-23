# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
def temperature():
    temp = int(input("Enter the temperature: "))
    if temp < 0 :
        print("The temperature is freezing.")
    elif 0 <= temp <= 10: 
        print("The temperature is cold.")
    elif 11 <= temp <= 20:
        print("The temperature is moderate.")
    elif 21 <= temp <= 30:
        print("The temperature is warm.")
    else:
        print("The temperature is hot.")        
temperature()

# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
import math
def volume_of_sphere():
    r = float(input("Enter the radius: ")) # r is radius
    pie = math.pi
    volume = (4/3) * pie * r**2
    print(f"The volume of a sphere with radius {r} is {volume:.1f}")
volume_of_sphere()