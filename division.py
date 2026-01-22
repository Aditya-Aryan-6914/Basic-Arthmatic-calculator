"""
Division Module
Provides division functionality for the calculator with zero-division error handling
"""

def divide(num1, num2):
    """
    Divide num1 by num2 and return the result
    
    Args:
        num1 (float): Dividend (number to be divided)
        num2 (float): Divisor (number to divide by)
    
    Returns:
        float: Quotient of num1 divided by num2
        
    Raises:
        ZeroDivisionError: If num2 is zero
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2


def divide_with_display(num1, num2):
    """
    Divide two numbers and display the result with formatting
    Includes error handling for division by zero
    
    Args:
        num1 (float): Dividend (number to be divided)
        num2 (float): Divisor (number to divide by)
    """
    try:
        result = divide(num1, num2)
        print(f"\n{'='*40}")
        print(f"  {num1} ÷ {num2} = {result}")
        print(f"{'='*40}")
        return result
    except ZeroDivisionError as e:
        print(f"\n{'='*40}")
        print(f"  Error: {e}")
        print(f"  Please enter a non-zero divisor.")
        print(f"{'='*40}")
        return None
