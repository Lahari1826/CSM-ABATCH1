# simple_script.py

def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}! Welcome to Python.")

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    # Example usage
    greet("World")
    result = add_numbers(5, 7)
    print(f"The sum of 5 and 7 is {result}")
