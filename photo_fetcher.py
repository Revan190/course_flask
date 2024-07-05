# photo_fetcher.py

import requests

# Function to fetch a dog photo URL
def fetch_dog_photo():
    # Replace 'DOG_API_URL' with the actual API URL you are using
    response = requests.get('DOG_API_URL')
    if response.status_code == 200:
        data = response.json()
        # Adjust the key according to the API response to get the photo URL
        return data['photo_url']
    else:
        # Handle the case where the API call fails
        return None

# Function to fetch a cat photo URL
def fetch_cat_photo():
    # Replace 'CAT_API_URL' with the actual API URL you are using
    response = requests.get('CAT_API_URL')
    if response.status_code == 200:
        data = response.json()
        # Adjust the key according to the API response to get the photo URL
        return data['photo_url']
    else:
        # Handle the case where the API call fails
        return None