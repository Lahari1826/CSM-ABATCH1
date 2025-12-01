# count_vowels.py

def count_vowels(text):
    """Counts the number of vowels in the given text."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

if __name__ == "__main__":
    user_input = input("Enter some text: ")
    result = count_vowels(user_input)
    print(f"The text contains {result} vowels.")
