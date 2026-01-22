"""
Subtraction Module
Provides subtraction functionality for the calculator
"""

def subtract(num1, num2):
    """
    Subtract num2 from num1 and return the result
    
    Args:
        num1 (float): First number (minuend)
        num2 (float): Second number (subtrahend)
    
    Returns:
        float: Difference of num1 and num2
    """
    return num1 - num2


def subtract_with_display(num1, num2):
    """
    Subtract two numbers and display the result with formatting
    
    Args:
        num1 (float): First number (minuend)
        num2 (float): Second number (subtrahend)
    """
    result = subtract(num1, num2)
    print(f"\n{'='*40}")
    print(f"  {num1} - {num2} = {result}")
    print(f"{'='*40}")
    return result
