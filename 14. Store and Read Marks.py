with open("marks.txt", "w") as file:
    file.write("Rahul,82\nAman,67\nSneha,91\nPriyan,74\nVikram,88\nAnanya,60\nRaj,79\nKaran,72\nDivya,95\nAditi,69\n")

print("Students scoring more than 75:")
with open("marks.txt", "r") as file:
    for line in file:
        if line.strip():
            name, marks_str = line.strip().split(",")
            if int(marks_str) > 75:
                print(f"- {name} (Marks: {marks_str})")