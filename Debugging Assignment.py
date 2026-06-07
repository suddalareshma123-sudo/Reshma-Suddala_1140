def main():
    marks = []

    print("Enter the marks for 5 students:")
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for student {i}: "))
                if mark < 0:
                    print("Marks cannot be negative. Please try again.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)

    print("\n" + "="*30)
    print("        PROGRAM OUTPUT        ")
    print("="*30)
    print(f"1 Total Marks   : {total_marks:.2f}")
    print(f"2 Average Marks : {average_marks:.2f}")
    print(f"3 Highest Marks : {highest_marks:.2f}")
    print(f"4 Lowest Marks  : {lowest_marks:.2f}")
    print("="*30)

if __name__ == "__main__":
    main()