def main_task1():
   
    n = int(input("Enter the value of n: "))
    print("-" * 30)

    print("1. Right triangle of stars:")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
    print("-" * 30)

    print("2. Inverted triangle of numbers:")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print("-" * 30)

    print("3. Pascal's triangle first n rows:")
    pascal_accumulator = []
    for i in range(n):
        
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal_accumulator[i - 1][j - 1] + pascal_accumulator[i - 1][j]
        pascal_accumulator.append(row)
        
      
        print(" ".join(map(str, row)))
    print("-" * 30)

   
    print(f"4. Prime numbers up to {n}:")
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  
        else:
            
            print(num, end=" ")
    print("\n" + "-" * 30)

if __name__ == "__main__":
    main_task1()