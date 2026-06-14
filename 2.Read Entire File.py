with open("student.txt", "r") as file:
    content = file.read()
    print("--- Displaying Complete File Contents ---")
    print(content, end="")