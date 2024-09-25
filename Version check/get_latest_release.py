import requests

def get_latest_release_info():
    api_url = "https://api.github.com/repos/markhen2/Stock-review-app/releases/latest"
    response = requests.get(api_url)
    release_data = response.json()
    return release_data
