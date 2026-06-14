with open("results.txt", "w") as file:
    file.write("Amit,85,90,92\nSumit,78,82,80\nKiran,95,91,96\nRohit,88,84,89\n")

topper_name = ""
highest_total = -1

with open("results.txt", "r") as file:
    for line in file:
        if line.strip():
            parts = line.strip().split(",")
            name = parts[0]
            total_score = int(parts[1]) + int(parts[2]) + int(parts[3])
            
            if total_score > highest_total:
                highest_total = total_score
                topper_name = name

print("--- Academic Report ---")
print(f"Top Performer: {topper_name}")
print(f"Highest Score: {highest_total} / 300")