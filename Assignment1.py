def calculate_emi(principal, annual_rate, tenure_years):
    
    monthly_rate = annual_rate / (12 * 100)
    
    tenure_months = tenure_years * 12
    
    numerator = principal * monthly_rate * ((1 + monthly_rate) ** tenure_months)
    denominator = ((1 + monthly_rate) ** tenure_months) - 1
    emi = numerator / denominator
    
    return emi, tenure_months

loan_amount = 500000.0 
interest_rate = 8.5     
duration = 5            

monthly_instalment, total_months = calculate_emi(loan_amount, interest_rate, duration)
total_payable = monthly_instalment * total_months
interest_payable = total_payable - loan_amount


print(f"--- EMI Loan Summary ---")
print(f"Principal Amount:     ₹{loan_amount:,.2f}")
print(f"Monthly EMI:          ₹{monthly_instalment:,.2f}")
print(f"Total Repayment:      ₹{total_payable:,.2f}")
print(f"Total Interest Paid:  ₹{interest_payable:,.2f}")