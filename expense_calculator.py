
business = input("Business: ")  # Get business name

expense = float(input("Expense: "))  # Get cost

tax_rate = float(input("Tax %: "))  # Get tax rate

tax = expense * tax_rate / 100  # Calculate tax

total = expense + tax  # Calculate total

print("Business:", business)  # Show business

print("Expense:", expense)  # Show expense

print("Tax:", tax)  # Show tax

print("Total:", total)  # Show total cost
