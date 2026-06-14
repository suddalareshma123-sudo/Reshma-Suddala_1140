search_word = input("Enter the word to search for: ")
with open("student.txt", "r") as file:
    data = file.read()

if search_word in data:
    print(f"Yes, the word '{search_word}' exists in the file.")
else:
    print(f"No, the word '{search_word}' does not exist.")