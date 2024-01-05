import requests

def get_address_coordinates(address):
    """
    Get the geographical coordinates (latitude and longitude) of an address using the OpenStreetMap Nominatim API.

    Importing the Method:
    ---------------------
    - Ensure you have the 'requests' library installed in your Python environment: `pip install requests`
    - Place this 'geocode.py' script in the 'Modules' folder within your project directory.
    - Import this function into your main application script using: `from Modules.geocode import get_address_coordinates`.

    Args:
        address (str): A string representing the address to look up. This can be any human-readable address, such as
        "1600 Amphitheatre Parkway, Mountain View, CA" or "Eiffel Tower". The address should be URL-encoded if it 
        contains special characters.

    Returns:
        tuple: A tuple containing the latitude and longitude as strings, or (None, None) if unable to retrieve the information.
        For example: ('37.4224764', '-122.0842499')

    Usage Example:
    --------------
    # Import the method from the Modules folder
    from Modules.geocode import get_address_coordinates

    # Use the method to get coordinates
    lat, lon = get_address_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")
    print(f"Latitude: {lat}, Longitude: {lon}")

    Notes:
    ------
    - The Nominatim service is provided for free by OpenStreetMap and has usage policies including a custom User-Agent 
      header (which is set in the 'headers' variable) and limitations on the request rate. Please adhere to these policies 
      and consider using a paid service for heavy or commercial use.
    - The function returns the first result provided by the API. Some addresses might return multiple possible locations; 
      consider implementing additional logic to handle such cases as needed.
    """
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    headers = {'User-Agent': 'YourAppName'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                return (data[0]['lat'], data[0]['lon'])
            else:
                print("No results found.")
        else:
            print(f"HTTP Error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return (None, None)
