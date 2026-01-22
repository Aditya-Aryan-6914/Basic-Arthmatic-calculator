"""
Multiplication Module
Provides multiplication functionality for the calculator
"""

def multiply(num1, num2):
    """
    Multiply two numbers and return the result
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Product of num1 and num2
    """
    return num1 * num2


def multiply_with_display(num1, num2):
    """
    Multiply two numbers and display the result with formatting
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    """
    result = multiply(num1, num2)
    print(f"\n{'='*40}")
    print(f"  {num1} × {num2} = {result}")
    print(f"{'='*40}")
    return result
