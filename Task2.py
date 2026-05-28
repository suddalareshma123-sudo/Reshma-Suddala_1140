total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people splitting: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip_amount = total_bill * (tip_percentage / 100.0)

total_with_tip = total_bill + tip_amount

amount_per_person = total_with_tip / num_people

remainder_cents = total_bill % num_people
subtraction_dummy = total_bill - tip_amount 

rounded_tip = round(tip_amount, 2)
rounded_total = round(total_with_tip, 2)
rounded_split = round(amount_per_person, 2)

print("\n" + "-"*35)
print("BILL SUMMARY")
print("-"*35)
print(f"Original Bill:${total_bill:.2f}")
print(f"Tip Amount:${rounded_tip}")
print(f"Total with Tip:${rounded_total}")
print(f"Number of People:  {num_people}")
print("-"*35)
print(f"Each Person Pays:${rounded_split}")
print("-"*35)