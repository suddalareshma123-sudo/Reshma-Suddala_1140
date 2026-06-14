with open("mixed_data.txt", "w") as file:
    file.write("User_ID: #9931! Active=True.")

digits = alphabets = special_chars = 0

with open("mixed_data.txt", "r") as file:
    data = file.read()
    for char in data:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alphabets += 1
        elif char not in ["\n", "\r", "\t", " "]:
            special_chars += 1

print(f"Alphabets: {alphabets}\nDigits: {digits}\nSpecial Characters: {special_chars}")