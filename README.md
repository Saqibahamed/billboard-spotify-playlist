# Billboard Top 100 → Spotify Playlist 🎶

This Python project scrapes the **Billboard Hot 100** songs for a given date and automatically creates a **Spotify playlist** with those songs.  

It combines **BeautifulSoup** for web scraping with the **Spotify Web API** (via `spotipy`) to bring your favorite hits from the past into your Spotify library.

---

## 🚀 Features
- Scrape **Billboard Hot 100** songs for any given date (YYYY-MM-DD).
- Automatically create a **public playlist** in your Spotify account.
- Skips unavailable songs gracefully if they don’t exist on Spotify.
- Uses environment variables for secure Spotify API credentials.

---

## 📂 Project Structure

```
├── main.py                # Main script to authenticate with Spotify & create playlist
├── Billboard_Scraping.py  # Script to scrape Billboard Hot 100 songs
├── .venv/.env             # Environment file (contains Spotify API credentials)
├── requirements.txt       # Python dependencies (optional but recommended)
```


## 🛠️ Requirements
- Python 3.8+
- Spotify Developer Account
- Dependencies:
  - [spotipy](https://spotipy.readthedocs.io/)
  - [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
  - [requests](https://docs.python-requests.org/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)

Install them with:
```bash
pip install -r requirements.txt
```
---

## 🔑 Setup
- Clone the repository

git clone https://github.com/your-username/billboard-to-spotify.git
cd billboard-to-spotify


- Update .env file inside .venv/ and add your Spotify API credentials:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URL=http://localhost:8888/callback
```
- Get these credentials from the Spotify Developer Dashboard
- Run the script:
```
python main.py
```
---

📌 Usage

When prompted, enter a date in the format:

```
YYYY-MM-DD
Example: 2000-08-12
```

The script will:
- Scrape the Billboard Hot 100 songs for that date.
- Authenticate with your Spotify account.
- Create a playlist named:
    Top 100 songs - <YEAR>
- Add all available songs.
---

## ⚠️ Notes

Songs not available on Spotify will be skipped automatically.

Make sure your Spotify app is set up correctly in the Developer Dashboard with the same redirect URI.

Playlist will always be public by default (you can modify this in the code).
---

## 🙌 Credits

Billboard
 for charts

Spotipy
 for Spotify API integration

BeautifulSoup
 for scraping
