# luhn_module.py

def digits_of(n):
    """
    Convert a number into a list of its digits.
    
    Args:
        n (str or int): The number to be split into digits.

    Returns:
        list: A list of integers representing each digit of the input number.
    """
    return [int(d) for d in str(n)]

def luhn_check(card_number):
    """
    Check if the card number is valid according to Luhn's algorithm.

    Importing the Method:
    ---------------------
    - Place this 'luhn_module.py' script in the 'Modules' folder within your project directory.
    - Import this function into your main application script using: `from Modules.luhn_module import luhn_check`.

    Args:
        card_number (str): A string representing the card number to validate.

    Returns:
        bool: True if the card number is valid according to Luhn's algorithm, False otherwise.

    Usage Example:
    --------------
    # Import the method from the Modules folder
    from Modules.luhn_module import luhn_check

    # Use the method to check a card number
    card_number = "1234567890123456"
    is_valid = luhn_check(card_number)
    print(f"Card number {card_number} is {'valid' if is_valid else 'invalid'}.")

    Notes:
    ------
    - Luhn's algorithm is a simple checksum formula used to validate a variety of identification numbers, mainly credit card numbers.
    - This implementation is meant for educational purposes and may not cover all aspects of payment processing.
    """
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0

# Add a main block to allow standalone testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        card_number = sys.argv[1]
        is_valid = luhn_check(card_number)
        print(f"Card number {card_number} is {'valid' if is_valid else 'invalid'} according to Luhn's algorithm.")
    else:
        print("Please provide a card number to check.")
