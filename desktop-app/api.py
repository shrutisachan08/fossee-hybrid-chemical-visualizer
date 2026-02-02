import requests
BASE_URL = "http://127.0.0.1:8000/api"
TOKEN = None 

def login(username, password):
    global TOKEN
    res = requests.post(
        f"{BASE_URL}/token/",
        json={"username": username, "password": password}
    )
    res.raise_for_status()
    TOKEN = res.json()["access"]

def upload_csv(file_path):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    with open(file_path, "rb") as f:
        files = {"csv_file": f}
        res = requests.post(f"{BASE_URL}/upload/", headers=headers, files=files)
    res.raise_for_status()
    return res.json()

def fetch_dataset_history():
    if not TOKEN:
        raise Exception("Not logged in")

    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{BASE_URL}/history/", headers=headers)
    response.raise_for_status()
    return response.json()
