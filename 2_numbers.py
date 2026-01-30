# Numbers Task
print("=== Numbers Task ===")

# 1. Format function with 145 and 'o'
def format_number(num, format_char):
    return format(num, format_char)

result = format_number(145, 'o')
print(f"format(145, 'o') = {result}")
print("Representation: Octal (base 8)")

# 2. Circular pond area and water calculation
print("\n--- Circular Pond Calculation ---")
radius = 84
pi = 3.14
area = pi * radius ** 2
print(f"Pond area: {area} square meters")

water_per_sqm = 1.4
total_water = area * water_per_sqm
print(f"Total water: {int(total_water)} liters")

# 3. Speed calculation
print("\n--- Speed Calculation ---")
distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print(f"Speed: {int(speed)} meters per second")