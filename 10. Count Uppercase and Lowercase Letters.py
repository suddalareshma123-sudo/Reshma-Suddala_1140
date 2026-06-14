with open("student.txt", "r") as file:
    data = file.read()

upper_count = 0
lower_count = 0

for char in data:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"Uppercase characters: {upper_count}")
print(f"Lowercase characters: {lower_count}")