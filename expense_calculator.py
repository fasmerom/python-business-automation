
business = input("Business: ")  # Get business name

while True:  # Keep repeating this block
    try:  # Attempt to get a valid number
        expense = float(input("Expense: "))
        break  # Exit loop when input is valid
    except ValueError:  # Handle invalid input
        print("Please enter a valid number.")


while True:  # Keep repeating this block
    try:  # Attempt to get a valid number
        tax_rate = float(input("Tax %: "))
        break  # Exit loop when input is valid
    except ValueError:  # Handle invalid input
        print("Please enter a valid number.")


tax = expense * tax_rate / 100  # Calculate tax

total = expense + tax  # Calculate total

print("Business:", business)  # Show business

print("Expense:", expense)  # Show expense

print("Tax:", tax)  # Show tax

print("Total:", total)  # Show total cost








