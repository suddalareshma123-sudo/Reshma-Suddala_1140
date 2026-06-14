with open("language.txt", "w") as file:
    file.write("Python is simple.\nLearning Python is highly recommended.")

with open("language.txt", "r") as file:
    original_data = file.read()

modified_data = original_data.replace("Python", "Programming")

with open("language.txt", "w") as file:
    file.write(modified_data)

print("[Success] Replacement complete. New File Content:")
print(modified_data)