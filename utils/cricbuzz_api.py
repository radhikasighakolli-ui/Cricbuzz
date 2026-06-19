<<<<<<< HEAD
import requests

API_KEY = "460e4a0318msh2fc5f4e0c52edf3p17817ajsn524e27ca28dc"
API_HOST = "cricbuzz-cricket.p.rapidapi.com"
BASE_URL = f"https://{API_HOST}"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

def get_live_matches():
    url = f"{BASE_URL}/matches/v1/live"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
=======
import requests

API_KEY = "460e4a0318msh2fc5f4e0c52edf3p17817ajsn524e27ca28dc"
API_HOST = "cricbuzz-cricket.p.rapidapi.com"
BASE_URL = f"https://{API_HOST}"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

def get_live_matches():
    url = f"{BASE_URL}/matches/v1/live"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
>>>>>>> e001a984a07ce756997db40c52bcf4d921037760
    return response.json()