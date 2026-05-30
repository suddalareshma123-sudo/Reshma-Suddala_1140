def calculate_income_tax(income):
    tax = 0.0
    breakdown = {}
    
    if income <= 300000:
        breakdown['Slab 1 (0%)'] = 0.0
    elif income <= 700000:
        taxable_amount = income - 300000
        tax = taxable_amount * 0.05
        breakdown['Slab 2 (5%)'] = tax
    elif income <= 1000000:
        tax = (400000 * 0.05)  
        taxable_amount = income - 700000
        slab3_tax = taxable_amount * 0.10
        tax += slab3_tax
        breakdown['Slab 2 (5%)'] = 20000.0
        breakdown['Slab 3 (10%)'] = slab3_tax
    else:
        tax = (400000 * 0.05) + (300000 * 0.10)  
        taxable_amount = income - 1000000
        slab4_tax = taxable_amount * 0.20
        tax += slab4_tax
        breakdown['Slab 2 (5%)'] = 20000.0
        breakdown['Slab 3 (10%)'] = 30000.0
        breakdown['Slab 4 (20%)'] = slab4_tax
        
    return tax, breakdown

annual_income = 1200000.0  

total_tax, tax_breakdown = calculate_income_tax(annual_income)

print(f"--- Income Tax Report ---")
print(f"Total Annual Income: ₹{annual_income:,.2f}")
print("\nTax Breakdown by Slab:")
for slab, amount in tax_breakdown.items():
    print(f" * {slab}: ₹{amount:,.2f}")
print(f"-------------------------")
print(f"Total Tax Payable:   ₹{total_tax:,.2f}")