# For Loop Task
import random

print("=== For Loop Task ===")

# 1. Die Rolling Simulation
print("--- Die Rolling Simulation ---")
rolls = 20
count_six = 0
count_one = 0
count_double_six = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_six += 1
        if previous_roll == 6:
            count_double_six += 1
    
    if roll == 1:
        count_one += 1
    
    previous_roll = roll

print(f"\nStatistics after {rolls} rolls:")
print(f"Number of 6s: {count_six}")
print(f"Number of 1s: {count_one}")
print(f"Number of consecutive 6s: {count_double_six}")

# 2. Jumping Jacks Workout
print("\n--- Jumping Jacks Workout ---")
total_jacks = 100
completed_jacks = 0

for set_num in range(1, 11):  # 10 sets of 10 jumping jacks each
    print(f"\nSet {set_num}: Do 10 jumping jacks!")
    completed_jacks += 10
    
    if completed_jacks >= total_jacks:
        print("Congratulations! You have done it!")
        break
    
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {completed_jacks} jumping jacks.")
            break
    
    remaining = total_jacks - completed_jacks
    print(f"Jumping jacks remaining: {remaining}")

if completed_jacks >= total_jacks:
    print("Congratulations! You have done it!")