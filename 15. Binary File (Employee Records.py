import pickle

employee_records = [
    {"EmpID": "E101", "Name": "Alice", "Dept": "HR"},
    {"EmpID": "E102", "Name": "Bob", "Dept": "IT"},
    {"EmpID": "E103", "Name": "Charlie", "Dept": "Finance"}
]

with open("employee.dat", "wb") as bin_file:
    pickle.dump(employee_records, bin_file)

search_id = input("Enter Employee ID to search (e.g., E102): ").strip()

with open("employee.dat", "rb") as bin_file:
    loaded_records = pickle.load(bin_file)

found = False
for emp in loaded_records:
    if emp["EmpID"].upper() == search_id.upper():
        print(f"Match Found! Name: {emp['Name']}, Department: {emp['Dept']}")
        found = True
        break

if not found:
    print("Record not found.")