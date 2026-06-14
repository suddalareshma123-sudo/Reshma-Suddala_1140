with open("document.txt", "w") as file:
    file.write("Line 1 text.\n\nLine 3 text.\n\n\nLine 6 text.")

blank_line_count = 0
with open("document.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            blank_line_count += 1
print(f"Total number of blank lines: {blank_line_count}")