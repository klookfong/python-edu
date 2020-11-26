import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                               client_secret="YOUR CLIENT SECRET",
                                               redirect_uri= "http://localhost:8888/callback",
                                               scope="playlist-modify-public",
                                               show_dialog=True))
user = sp.current_user()['id']




date = input("What date (YYYY-MM-DD): ")
website = f"https://www.billboard.com/charts/hot-100/{date}"
web_html = requests.get(website).text

soup = BeautifulSoup(web_html, "html.parser")
songs_html = soup.find_all(name="span", class_="chart-element__information__song")
songs = [song.getText() for song in songs_html]
playlist = sp.user_playlist_create(user=user, name=f"{date} Billboard 100")
uris = []
for song in songs:
    try:
        query = sp.search(q=f"track:{song} year: {date.split('-')[0]}", type='track')
        uris.append(query['tracks']['items'][0]['uri'])
        print(f"{song} successfully added")
    except:
        print(f"{song} does not exist in spotify")
sp.playlist_add_items(playlist_id=playlist['id'],
                      items=uris)
print("Playlist successfully created")