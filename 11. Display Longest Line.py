with open("student.txt", "r") as file:
    lines = file.readlines()

longest_line = ""
for line in lines:
    if len(line.strip()) > len(longest_line.strip()):
        longest_line = line
print(f"The longest line is: '{longest_line.strip()}'")