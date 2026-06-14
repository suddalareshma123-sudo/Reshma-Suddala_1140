with open("student.txt", "r") as file:
    data = file.read()
    words_list = data.split()
    total_words = len(words_list)
print(f"Total words in the file: {total_words}")