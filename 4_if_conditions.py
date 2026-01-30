# If Conditions Task
print("=== If Conditions Task ===")

# 1. BMI Calculator
print("--- BMI Calculator ---")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    category = "Obesity"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")

# 2. City to Country mapping
print("\n--- City to Country ---")
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in our database")

# 3. Compare two cities
print("\n--- Compare Two Cities ---")
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

def get_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found in database")