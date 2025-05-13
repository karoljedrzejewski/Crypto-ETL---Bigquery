import requests


def extract_data(url, api_key):
    """
    Extracts data from a given URL.

    Args:
        url (str): The URL to extract data from.

    Returns:
        dict: The extracted data in JSON format.
    """
    response = requests.get(add_api_key_to_url(url, api_key))
    return response.json()

def add_api_key_to_url(url, api_key):
    """
    Adds the API key to the URL as a query parameter.

    Args:
        url (str): The base URL.
        api_key (str): The API key.

    Returns:
        str: The URL with the API key added as a query parameter.
    """
    if url.endswith('/'):
        url = url[:-1]
    return f'{url}?x_cg_demo_api_key={api_key}'