def check_loan_eligibility(age, salary, employment_type):
  
    employment = employment_type.strip().lower()
    
    if age < 21 or age > 60:
        return "Rejected: Age must be between 21 and 60."
        
    if salary < 25000:
        return "Rejected: Salary must be at least ₹25,000."
        
    if employment not in ["salaried", "self employed", "self-employed"]:
        return "Rejected: Invalid employment type. Must be salaried or self employed."
    
    if 21 <= age <= 30 and salary < 30000:
        return "Needs guarantor"
        
    if age > 55 and (employment == "self employed" or employment == "self-employed"):
        return "High risk, senior review needed"
        
    return "Approved"

if __name__ == "__main__":
    print("--- Loan Eligibility System ---")
    try:
        user_age = int(input("Enter age: "))
        user_salary = float(input("Enter monthly salary: "))
        user_employment = input("Enter employment type (salaried/self employed): ")
        
        result = check_loan_eligibility(user_age, user_salary, user_employment)
        print(f"Decision: {result}")
    except ValueError:
        print("Please enter numeric digits for age and salary.")