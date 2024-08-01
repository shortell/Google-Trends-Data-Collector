import os
import requests
from dotenv import load_dotenv


def send_post_request(resource, data=None):
    """
    Send an HTTP POST request with optional form data.

    Args:
        resource (str): The resource path to send the POST request to.
        data (dict, optional): A dictionary of key-value pairs representing the form data. Default is None.

    Returns:
        requests.Response: The response object.
    """
    try:
        load_dotenv()
        url = 'http://' + os.getenv('IP_ADDRESS') + ':5000'
        response = requests.post(url + resource, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f'Error sending POST request: {e}')
        return None


def send_get_request(resource, data=None):
    """
    Send an HTTP GET request with optional form data.

    Args:
        resource (str): The resource path to send the GET request to.
        data (dict, optional): A dictionary of key-value pairs representing the form data. Default is None.

    Returns:
        requests.Response: The response object.
    """
    try:
        load_dotenv()
        url = 'http://' + os.getenv('IP_ADDRESS') + ':5000'
        if data is None:
            response = requests.get(url + resource)
        else:
            response = requests.get(url + resource, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f'Error sending GET request: {e}')
        return None
