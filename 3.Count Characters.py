with open("student.txt", "r") as file:
    data = file.read()
    total_chars = len(data)
print(f"Total characters present in the file: {total_chars}")