name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
subject = input("Enter your favourite subject: ")

birth_year = 2024 - age

print("\n" + "="*30)
print("PERSONAL PROFILE CARD")
print("="*30)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Estimated Birth:   {birth_year}")
print(f"City: {city}")
print(f"Favourite Subject: {subject}")
print("="*30)