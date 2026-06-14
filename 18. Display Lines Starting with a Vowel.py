with open("sentences.txt", "w") as file:
    file.write("Apple is a sweet fruit.\nBanana is yellow.\nOrange has vitamin C.\n")

vowels = "aeiouAEIOU"
print("Lines starting with a vowel:")

with open("sentences.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line and cleaned_line[0] in vowels:
            print(cleaned_line)