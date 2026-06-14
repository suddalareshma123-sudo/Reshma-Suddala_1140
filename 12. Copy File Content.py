with open("student.txt", "r") as source:
    content = source.read()

with open("student_backup.txt", "w") as destination:
    destination.write(content)
print("[Success] Content copied successfully to student_backup.txt.")