with open("student.txt", "r") as file:
    print("Reading file line-by-line:")
    while True:
        line = file.readline()
        if line == "":
            break
        print(line, end="")