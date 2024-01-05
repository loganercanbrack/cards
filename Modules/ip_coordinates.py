import requests

def get_ip_coordinates(ip):
    """
    Get the geographical coordinates (latitude and longitude) of an IP address using the IP-API service.

    Importing the Method:
    ---------------------
    - Ensure you have the 'requests' library installed in your Python environment: `pip install requests`
    - Place this 'ip_coordinates.py' script in the 'Modules' folder within your project directory.
    - Import this function into your main application script using: `from Modules.ip_coordinates import get_ip_coordinates`.

    Args:
        ip (str): A string representing the IP address to look up. The IP address should be a valid IPv4 or IPv6 address.

    Returns:
        tuple: A tuple containing the latitude and longitude as strings, or (None, None) if unable to retrieve the information.
        For example: ('37.4224764', '-122.0842499')

    Usage Example:
    --------------
    # Import the method from the Modules folder
    from Modules.ip_coordinates import get_ip_coordinates

    # Use the method to get coordinates
    lat, lon = get_ip_coordinates("8.8.8.8")
    print(f"Latitude: {lat}, Longitude: {lon}")

    Notes:
    ------
    - The IP-API service provides free usage for non-commercial purposes and has limitations on the request rate. Please 
      adhere to their usage policies and consider their paid service for heavy or commercial use.
    - The function returns the coordinates provided by the API. Be aware that IP-based geolocation is approximate and may 
      not always accurately represent the actual geographical location of the IP address.
    """
    url = f'http://ip-api.com/json/{ip}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return (data['lat'], data['lon'])
            else:
                print(f"Error: {data['message']}")
        else:
            print(f"HTTP Error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return (None, None)
