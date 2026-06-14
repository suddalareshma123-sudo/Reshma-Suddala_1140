with open("student.txt", "a") as file:
    print("Enter 3 additional student names to append:")
    for i in range(1, 4):
        new_name = input(f"Enter new name {i}: ")
        file.write(new_name + "\n")
print("\n[Success] Data appended successfully.")