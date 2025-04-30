from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests
import json
import time

# Change the path to your .json file
KEY_FILE_LOCATION = 'indexing.json'

SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=SCOPES)

# Refresh token
credentials.refresh(Request())

# Read urls.txt file
with open('url.txt', 'r') as file:
    urls = [line.strip() for line in file]

endpoint = 'https://indexing.googleapis.com/v3/urlNotifications:publish'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials.token}"
}

for url in urls:

    time.sleep(5) # 5 seconds

    body = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = requests.post(endpoint, headers=headers, json=body)
    print(f"Submitted {url}: {response.status_code} - {response.text}")
