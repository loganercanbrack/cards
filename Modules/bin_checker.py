import re
import requests

# Configuration
USER_ID = 'your_neutrino_user_id'
API_KEY = 'your_neutrino_api_key'
API_URL = 'https://neutrinoapi.net/bin-lookup'


class BinChecker:
    """
    Retrieve card BIN (Bank Identification Number) information using the Neutrino API.

    Importing the Module:
    ---------------------
    - Ensure you have the 'requests' library installed in your Python environment: `pip install requests`
    - Place this 'bin_checker.py' script in the 'Modules' folder within your project directory.
    - Import this class into your main application script using: `from Modules.bin_checker import BinChecker`.

    Args:
        card_number (str): A string representing the card number whose BIN you want to look up. The card number should be digits only, typically 16 digits for most cards.
        ip_address (str): A string representing the IP address of the customer for fraud prevention purposes. This should be in the standard IPv4 or IPv6 format.

    Returns:
        dict: A dictionary containing various information about the card's BIN number, such as the issuer, card brand, card type, and more. In case of an error or failure, the dictionary will contain an 'error' key with a descriptive message.

    Usage Example:
    --------------
    # Import the BinChecker class from the Modules folder
    from Modules.bin_checker import BinChecker

    # Create an instance of the BinChecker
    checker = BinChecker()

    # Use the instance to get BIN information
    result = checker.get_bin_info('1234567890123456', '192.168.1.1')
    print(result)

    Notes:
    ------
    - The Neutrino API used in this module requires a user ID and API key. Ensure that these are correctly set in the USER_ID and API_KEY variables at the top of the module.
    - The Neutrino API is a third-party service and has its own set of usage policies and limitations. Be sure to understand and adhere to these policies, especially if you plan to use this module for commercial purposes.
    - The module is designed to return the first result provided by the API. Some card numbers might return multiple possible issuers; consider implementing additional logic to handle such cases as needed.
    """


    @staticmethod
    def sanitize_card_number(card_number):
        """Remove spaces, dashes, and plus signs from the card number."""
        return re.sub(r'[ -+]', '', card_number)

    def get_bin_info(self, card_number, ip_address):
        """Retrieve BIN information for a given card number and IP address."""
        card_number = self.sanitize_card_number(card_number)

        if len(card_number) >= 6:
            bin_number = card_number[:6]
            return self.call_api(bin_number, ip_address)
        else:
            return {'error': 'Please enter a valid card number.'}

    def call_api(self, bin_number, ip_address):
        """Call the Neutrino API to fetch BIN information."""
        headers = {'User-ID': USER_ID, 'API-Key': API_KEY}
        params = {'bin-number': bin_number, 'customer-ip': ip_address}
        
        try:
            response = requests.post(API_URL, headers=headers, data=params)
            response.raise_for_status()
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            return {'error': f"Error fetching API information: {e}"}


# Example usage:
if __name__ == '__main__':
    bin_checker = BinChecker()
    result = bin_checker.get_bin_info('123456789012', '192.168.1.1')
    print(result)
