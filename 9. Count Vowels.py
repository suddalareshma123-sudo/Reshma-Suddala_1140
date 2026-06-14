with open("student.txt", "r") as file:
    data = file.read()

vowel_count = 0
vowels_reference = "aeiouAEIOU"

for char in data:
    if char in vowels_reference:
        vowel_count += 1
print(f"Total vowels present in the file: {vowel_count}")