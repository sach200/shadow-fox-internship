# List Task - Justice League
print("=== Justice League List Operations ===")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Count members
print(f"1. Number of members: {len(justice_league)}")
print(f"Current list: {justice_league}")

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print(f"\n2. After adding Batgirl and Nightwing: {justice_league}")

# 3. Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"\n3. Wonder Woman as leader: {justice_league}")

# 4. Move Superman between Aquaman and Flash
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
justice_league.remove("Superman")
if aquaman_index < flash_index:
    justice_league.insert(aquaman_index + 1, "Superman")
else:
    justice_league.insert(flash_index + 1, "Superman")
print(f"\n4. Superman between Aquaman and Flash: {justice_league}")

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"\n5. New team: {justice_league}")

# 6. Sort alphabetically
justice_league.sort()
print(f"\n6. Sorted alphabetically: {justice_league}")
print(f"New leader (0th index): {justice_league[0]}")
print("BONUS: The new leader will be 'Cyborg' (first alphabetically)")