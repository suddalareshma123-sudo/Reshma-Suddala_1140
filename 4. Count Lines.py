with open("student.txt", "r") as file:
    lines_list = file.readlines()
    total_lines = len(lines_list)
print(f"Total number of lines in the file: {total_lines}")