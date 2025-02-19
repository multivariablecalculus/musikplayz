import requests

access_token = '7ea657c58334b4a92a8fbf3c108607c7cd409a38'  # Replace with your Bitly access token
bitlink_id = 'bit.ly/muzikplayz-main-page'  # Ensure this includes 'bit.ly/'
ngrok_url = 'https://87a4-2409-40e0-fb-d393-9d41-9c85-7bd0-37cb.ngrok-free.app'  # Replace with your current ngrok URL

def update_bitly_link():
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'long_url': ngrok_url
    }
    
    print(f"Attempting to update Bitly link: {ngrok_url} with ID: {bitlink_id}")
    
    try:
        response = requests.patch(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}', json=data, headers=headers)
        print(f"Response Status Code: {response.status_code}")  # Debugging output
        if response.status_code == 200:
            print(f'Updated Bitly link: {response.json()["link"]}')
        else:
            print('Error updating Bitly link:', response.json())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_bitly_link()
