import sys
inventory = {
    "101": {"name": "Laptop", "category": "Electronics", "qty": 15, "price": 800.0, "supplier": "TechCorp"},
    "102": {"name": "Desk Chair", "category": "Furniture", "qty": 3, "price": 120.0, "supplier": "OfficeMax"},
    "103": {"name": "Notebook", "category": "Stationery", "qty": 0, "price": 2.5, "supplier": "PaperCo"}
}
categories = {"Electronics", "Furniture", "Stationery"}
snapshots_log = []
def add_product():
    print("\n--- Add Product ---")
    p_id = input("Enter Product ID: ").strip()
    if p_id in inventory:
        print("❌ Error: Product ID already exists!")
        return
    
    name = input("Enter Name: ").strip()
    category = input("Enter Category: ").strip()
    try:
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
    except ValueError:
        print("❌ Invalid input! Quantity and Price must be numbers.")
        return
    supplier = input("Enter Supplier: ").strip()
    
    inventory[p_id] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }
    
    categories.add(category)
    print(f"✅ Product '{name}' added successfully!")
def update_inventory():
    print("\n--- Update Inventory ---")
    p_id = input("Enter Product ID to update: ").strip()
    if p_id not in inventory:
        print("❌ Product not found!")
        return
        
    print("Leave field blank to keep current value.")
    new_qty = input(f"New Quantity (Current: {inventory[p_id]['qty']}): ").strip()
    new_price = input(f"New Price (Current: ${inventory[p_id]['price']}): ").strip()
    
    if new_qty:
        inventory[p_id]['qty'] = int(new_qty)
    if new_price:
        inventory[p_id]['price'] = float(new_price)
    print("✅ Inventory updated successfully!")

def search_product():
    print("\n--- Search Product ---")
    query = input("Enter Product ID or Name to search: ").strip().lower()
    results = [] 
    
    for p_id, details in inventory.items():
        if query == p_id.lower() or query in details['name'].lower():
            results.append((p_id, details))
            
    if not results:
        print("No matching products found.")
    else:
        print(f"\nFound {len(results)} match(es):")
        for p_id, det in results:
            print(f"ID: {p_id} | Name: {det['name']} | Qty: {det['qty']} | Price: ${det['price']}")

def display_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'ID':<8} {'Name':<15} {'Category':<15} {'Qty':<8} {'Price':<10} {'Supplier':<15}")
    print("-" * 75)
    for p_id, det in inventory.items():
        print(f"{p_id:<8} {det['name']:<15} {det['category']:<15} {det['qty']:<8} ${det['price']:<9.2f} {det['supplier']:<15}")

def check_alerts():
    print("\n--- Stock Alerts ---")
    threshold = 5
    out_of_stock = []
    low_stock = []
    
    for p_id, det in inventory.items():
        if det['qty'] == 0:
            out_of_stock.append(f"{det['name']} (ID: {p_id})")
        elif det['qty'] <= threshold:
            low_stock.append(f"{det['name']} (ID: {p_id}, Qty: {det['qty']})")
            
    print("⚠️ Out of Stock Alert (Quantity = 0):")
    if out_of_stock:
        for item in out_of_stock: print(f"  - {item}")
    else:
        print("  None")
        
    print(f"⚠️ Low Stock Alert (Quantity <= {threshold}):")
    if low_stock:
        for item in low_stock: print(f"  - {item}")
    else:
        print("  None")
def manage_categories():
    print("\n--- Category Management ---")
    print("Tracked unique product categories (Stored in a Set):")
    for cat in categories:
        print(f" - {cat}")
def generate_report():
    print("\n--- Inventory Report Summary ---")
    total_items = 0
    total_value = 0.0
    cat_summary = {} 
    
    for p_id, det in inventory.items():
        qty = det['qty']
        val = qty * det['price']
        total_items += qty
        total_value += val
        
        cat = det['category']
        cat_summary[cat] = cat_summary.get(cat, 0) + qty
        snapshot = (p_id, det['name'], qty, val)
        snapshots_log.append(snapshot)
        
    print(f"Total Items in Stock: {total_items}")
    print(f"Total Inventory Value: ${total_value:,.2f}")
    print("\nCategory-wise Breakdown:")
    for cat, count in cat_summary.items():
        print(f" - {cat}: {count} items")
def delete_product():
    print("\n--- Delete Product ---")
    p_id = input("Enter Product ID to remove: ").strip()
    if p_id in inventory:
        removed = inventory.pop(p_id)
        print(f"✅ Product '{removed['name']}' removed from inventory.")
    else:
        print("❌ Error: Product ID not found.")
def main():
    while True:
        print("\n========================================")
        print(" Smart Inventory Management System Menu ")
        print("========================================")
        print("1. Add Product")
        print("2. Update Inventory")
        print("3. Search Product")
        print("4. Display Inventory")
        print("5. Check Stock Alerts (Low & Out)")
        print("6. View Product Categories")
        print("7. Generate Summary Report")
        print("8. Delete Product")
        print("9. Exit")
        
        choice = input("\nEnter your selection (1-9): ").strip()
        
        if choice == '1': add_product()
        elif choice == '2': update_inventory()
        elif choice == '3': search_product()
        elif choice == '4': display_inventory()
        elif choice == '5': check_alerts()
        elif choice == '6': manage_categories()
        elif choice == '7': generate_report()
        elif choice == '8': delete_product()
        elif choice == '9':
            print("\nExiting application. Bye!")
            sys.exit()
        else:
            print("❌ Invalid menu choice. Please select 1 through 9.")

if __name__ == "__main__":
    main()