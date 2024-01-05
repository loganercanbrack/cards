import math

def calculate_distance(lat1, lon1, lat2, lon2, unit='nm'):
    """
    Calculate the distance between two points on the earth (specified in decimal degrees) in nautical miles,
    but return the result in kilometers or nautical miles labeled as 'miles'.
    
    Args:
        lat1, lon1: Latitude and longitude of the first point.
        lat2, lon2: Latitude and longitude of the second point.
        unit: 'km' for kilometers, 'mi' for nautical miles labeled as miles.

    Returns:
        Distance between the two points in the specified unit.
    """
    R_nm = 3440.065  # Radius of the Earth in nautical miles

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_nm = R_nm * c  # distance in nautical miles

    # Convert to the desired unit
    if unit == 'km':
        return distance_nm * 1.852  # 1 nautical mile is approximately 1.852 kilometers
    else:  # if 'mi' is selected, return nautical miles but label it as 'miles'
        return distance_nm  # return nautical miles

# Rest of the module remains unchanged
