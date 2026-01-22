"""
Python Calculator - Main Program
A menu-driven calculator that performs basic arithmetic operations
"""

from addition import add_with_display

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("      PYTHON CALCULATOR")
    print("="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("="*40)


def get_numbers():
    """Get two numbers from the user"""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None


def main():
    """Main function to run the calculator"""
    print("Welcome to Python Calculator!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("\nThank you for using Python Calculator!")
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is not None and num2 is not None:
                # Arithmetic operations
                if choice == '1':
                    add_with_display(num1, num2)
                elif choice == '2':
                    print(f"\nResult: Subtraction feature coming soon!")
                elif choice == '3':
                    print(f"\nResult: Multiplication feature coming soon!")
                elif choice == '4':
                    print(f"\nResult: Division feature coming soon!")
        else:
            print("\nError: Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
