from bs4 import BeautifulSoup
import requests
from datetime import datetime

# function to get songs
def get_songs():
    title_tags = soup.find_all('h3',
                               class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")

    titles = [i.getText(strip=True) for i in title_tags]
    return titles

# to validate if the input is in the correct specified format
while True:
    date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()
    try:
        # Try parsing the input
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        break

    except ValueError:
        print("Invalid format! Please enter in YYYY-MM-DD format (e.g., 2000-08-12).")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/135.0.0.0 Safari/537.36"}

URL = f'https://www.billboard.com/charts/hot-100/{date}/'

# connecting to the billboard website

response = requests.get(URL, headers=header)
response.raise_for_status()
print(response)
data = response.text

# reading the data into Beautifulsoup
soup = BeautifulSoup(data, 'html.parser')
get_songs()
