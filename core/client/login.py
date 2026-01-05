import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import quote

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"

def login_via_growid(url, username, password):
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}, status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    token_input = soup.find('input', {'name': '_token'})
    if not token_input:
        print("_token not found on the login page.")
        return

    response = session.post(
        "https://login.growtopiagame.com/player/growid/login/validate",
        data={
            "growId": username,
            "password": password,
            "_token": token_input['value']
        }
    )

    if response.status_code != 200:
        print(f"Login request failed, status code: {response.status_code}")
        return
    
    try:
        data = response.json()
    except ValueError:
        soup = BeautifulSoup(response.text, "html.parser")
        error_div = soup.find("div", class_="text-danger-wrapper")

        if error_div:
            print(error_div.get_text(strip=True))

        return

    if data.get("status") == "success":
        print("Login successful.")
        return data.get("token")

def fetch_login_urls(login_data):
    url = "https://login.growtopiagame.com/player/login/dashboard?valKey=40db4045f2d8c572efe8c4a060605726"
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print("Fetching login URLs...")
    try:
        response = requests.post(url, headers=headers, data=quote(login_data.strip()))
        
        if response.status_code != 200:
            print(f"Failed to fetch login URLs, status code: {response.status_code}")
            time.sleep(5)
            return fetch_login_urls(login_data)

        soup = BeautifulSoup(response.text, "html.parser")

        apple_link = soup.find('a', onclick="optionChose('Apple');")
        apple_href = apple_link['href'] if apple_link else None
        google_link = soup.find('a', onclick="optionChose('Google');")
        google_href = google_link['href'] if google_link else None
        growtopia_link = soup.find('a', onclick="optionChose('Grow');")
        growtopia_href = growtopia_link['href'] if growtopia_link else None

        return {
            "apple": apple_href,
            "google": google_href,
            "growtopia": growtopia_href
        }
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        time.sleep(5)
        return fetch_login_urls(login_data)