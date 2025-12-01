# even_odd.py

def check_even_odd(number):
    """Checks if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

if __name__ == "__main__":
    # Example usage
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
