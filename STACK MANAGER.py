# Stock Manager Program

update_list = []
stock_list = []

def insert_stock():
    sku = input("Enter Stock ID (unique): ")
    for stock in stock_list:
        if stock["id"] == sku:
            print("Error: Stock ID already exists!")
            return
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    exp_date = input("Enter Expiry Date (dd-mm-yyyy): ")
    stock = {"id": sku, "name": name, "quantity": quantity, "price": price, "expiry": exp_date}
    stock_list.append(stock)
    # Keep sorted by name for easy review
    stock_list.sort(key=lambda x: x["name"])
    print("Stock inserted successfully!\n")

def sales_update():
    sku = input("Enter stock ID (unique): ")
    qt = int(input("Enter the quantity: "))
    a = (sku, qt)
    update_list.append(a)
    sku_found = False
    for stock in stock_list:
        if stock["id"] == sku:
            sku_found = True
            if stock["quantity"] >= qt:
                stock["quantity"] -= qt
                print(f"Sale processed: {qt} units of '{sku}'. New stock: {stock['quantity']}")
                if stock["quantity"] == 0:
                    print(f"Item '{sku}' is now out of stock.")
            else:
                print(f"Insufficient stock for '{sku}'. Available: {stock['quantity']}")
            break
    if not sku_found:
        print(f"SKU '{sku}' not found.")

def search_stock():
    sku = input("Enter stock ID to search: ")
    for stock in stock_list:
        if stock["id"] == sku:
            print("Stock Details:")
            for key, value in stock.items():
                print(f"{key}: {value}")
            return
    print("Stock ID not found.")

def delete_stock():
    sku = input("Enter stock ID to delete: ")
    for stock in stock_list:
        if stock["id"] == sku:
            stock_list.remove(stock)
            print("Stock deleted successfully.")
            return
    print("Stock ID not found.")

def identify_zero_stock():
    zero_stock = [s for s in stock_list if s["quantity"] == 0]
    if zero_stock:
        print("--- Out of Stock Items ---")
        for s in zero_stock:
            print(f"ID: {s['id']}, Name: {s['name']}, Expiry: {s['expiry']}")
    else:
        print("No items are out of stock.")

while True:
    print("\n===== Stock Manager =====")
    print("1. Insert Stock")
    print("2. Delete Stock by ID")
    print("3. Search Stock by ID")
    print("4. Process Sale (sales_update)")
    print("5. Identify Zero Stock")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_stock()
    elif choice == "2":
        delete_stock()
    elif choice == "3":
        search_stock()
    elif choice == "4":
        sales_update()
    elif choice == "5":
        identify_zero_stock()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
