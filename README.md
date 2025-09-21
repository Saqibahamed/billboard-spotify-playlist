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
1️⃣ Open Project in PyCharm

Launch PyCharm.

Go to File → Open.

Select your project folder (the one containing main.py and Billboard_Scraping.py) and click OK.

2️⃣ Create a Virtual Environment

Go to File → Settings → Project: YourProjectName → Python Interpreter.

Click the gear icon → Add.

Select Virtualenv Environment:

New environment (recommended)

Location: leave default (e.g., .venv)

Base interpreter: choose your Python 3.x installation

Click OK to create the virtual environment.

3️⃣ Install Dependencies

Open Terminal in PyCharm (bottom of IDE).

Run:
```
pip install spotipy beautifulsoup4 requests python-dotenv
```

Or, if you want, you can create a requirements.txt file (with these 4 libraries) and run:
```
pip install -r requirements.txt
```

4️⃣ Set Up .env File

Inside your project, create a folder .venv (if not already there).

Create a file called .env inside .venv/.

Add your Spotify API credentials:
```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URL=http://localhost:8888/callback
```

5️⃣ Configure Run in PyCharm

Go to Run → Edit Configurations → + → Python.

Name it: Run Billboard Playlist.
```
Script path: main.py.
```
Python interpreter: select the virtualenv you created.

Working directory: project root.

Click OK.

6️⃣ Run the Project

Click the green Run button (top right) or press Shift + F10.

---
## 📌 Usage

The program will ask:

Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
```
Enter a date, e.g., 2000-08-12.
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

Playlist will always be public by default (you can modify this in the code)

---

## 🙌 Credits

Billboard
 for charts

Spotipy
 for Spotify API integration

BeautifulSoup
 for scraping
