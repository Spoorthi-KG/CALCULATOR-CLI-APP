"""
CLI Calculator App

"""

# ---- Operation Functions ----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


# ---- CLI Main Loop ----
def main():
    print("🔢 Welcome to CLI Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("⚠️ Invalid choice! Please select 1-5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print(f"✅ Result: {result}")


# ---- Entry Point ----
if __name__ == "__main__":
    main()


