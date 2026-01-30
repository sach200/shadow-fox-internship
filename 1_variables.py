# Variables Task
print("=== Variables Task ===")

# 1. Create pi variable and check data type
pi = 22/7
print(f"pi = {pi}")
print(f"Data type of pi: {type(pi)}")

# 2. Create variable named 'for' (will cause error)
print("\n--- Trying to create variable named 'for' ---")
try:
    # for = 4  # This will cause SyntaxError
    exec("for = 4")
except SyntaxError as e:
    print(f"Error: {e}")
    print("Reason: 'for' is a reserved keyword in Python")

# 3. Simple Interest calculation
print("\n--- Simple Interest Calculation ---")
principal = 10000
rate = 5
time = 3
simple_interest = (principal * rate * time) / 100
print(f"Principal: {principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: {simple_interest}")