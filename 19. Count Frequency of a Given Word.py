with open("essay.txt", "w") as file:
    file.write("Python is simple. Python is versatile. Learning python is fun.")

target = input("Enter word to analyze frequency: ").strip().lower()

with open("essay.txt", "r") as file:
    content = file.read().lower()
    words = content.split()

cleaned_words = [word.strip(".,!?;:") for word in words]
word_frequency = cleaned_words.count(target)

print(f"The word '{target}' appears exactly {word_frequency} times.")