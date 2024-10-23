# Question 2(i)
# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi(weight, height):
    BMI = weight/height
    if BMI < 18.5:
        print("You are underweight")
    elif 18.5 <= BMI <+ 24.9:
        print("You have normal weight")
    elif 25 <= BMI <= 29.9:
        print("You are overweight")
    else:
        print("You are obsese")
        
weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in meters: "))
calculate_bmi(weight, height)

# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)
import math
def volume_of_a_cylinder(r, h):
    volume = math.pi * r**2 * h
    print(f"The volume of the cylinder of radius {r} and height {h} is {volume:.3f}")

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
volume_of_a_cylinder(r, h)
    
