"""
Addition Module
Provides addition functionality for the calculator
"""

def add(num1, num2):
    """
    Add two numbers and return the result
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Sum of num1 and num2
    """
    return num1 + num2


def add_with_display(num1, num2):
    """
    Add two numbers and display the result with formatting
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    """
    result = add(num1, num2)
    print(f"\n{'='*40}")
    print(f"  {num1} + {num2} = {result}")
    print(f"{'='*40}")
    return result
