with open("student.txt", "w") as file:
    print("Please enter the names of 5 students:")
    for i in range(1, 6):
        name = input(f"Enter name of student {i}: ")
        file.write(name + "\n")
print("\n[Success] student.txt created successfully.")