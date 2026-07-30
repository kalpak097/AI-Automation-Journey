import calculator_utils as calc

def run_calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1 Add")
        print("2 Subtract")
        print("3 Multiply")
        print("4 Divide")
        print("5 Square")
        print("6 Cube")
        print("7 Factorial")
        print("8 Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        # Single number operations
        if choice in ("5", "6", "7"):
            try:
                num = float(input("Enter number: "))
                
                if choice == "5":
                    print(f"Result: {calc.square(num)}")
                elif choice == "6":
                    print(f"Result: {calc.cube(num)}")
                elif choice == "7":
                    print(f"Result: {calc.factorial(int(num))}")
            except ValueError:
                print("Error: Invalid number input!")

        # Two number operations
        elif choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Result: {calc.add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {calc.subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {calc.multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {calc.divide(num1, num2)}")
            except ValueError:
                print("Error: Invalid number input!")

        else:
            print("Invalid option! Please select a number between 1 and 8.")

if __name__ == "__main__":
    run_calculator()