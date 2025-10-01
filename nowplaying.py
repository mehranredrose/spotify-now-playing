import requests
import base64
import os

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")

def get_access_token():
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Authorization": f"Basic {auth_header}"},
        data={
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
        },
    ).json()
    return response["access_token"]

def get_now_playing():
    token = get_access_token()
    response = requests.get(
        "https://api.spotify.com/v1/me/player/currently-playing",
        headers={"Authorization": f"Bearer {token}"},
    )
    if response.status_code == 204:
        return "Not playing anything 🎧"
    song = response.json()
    return f"🎶 [{song['item']['name']}]({song['item']['external_urls']['spotify']}) — {', '.join([a['name'] for a in song['item']['artists']])}"

if __name__ == "__main__":
    track = get_now_playing()
    with open("spotify.txt", "w", encoding="utf-8") as f:
        f.write(track)
