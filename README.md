# spotify-now-playing

Display your currently playing Spotify track in your GitHub profile README automatically using GitHub Actions and Spotify API.

# Spotify Now Playing on GitHub Profile

Display your currently playing Spotify track in your GitHub profile README automatically using GitHub Actions and the Spotify API.

---

## Features

- Shows your currently playing Spotify track in your README.
- Automatically updates every 5 minutes.
- Handles “Not playing anything” if nothing is currently playing.
- Secure — Spotify credentials are stored as GitHub Secrets.

---

## Repository Structure

Your repository should look like this:

your-repo/
├── README.md
├── nowplaying.py # Python script that fetches current track
└── .github/
└── workflows/
└── spotify.yml

# GitHub Actions workflow

- **`nowplaying.py`**: Fetches your currently playing song from Spotify and writes it to `spotify.txt`.
- **`.github/workflows/spotify.yml`**: Defines the GitHub Actions workflow that runs the script every 5 minutes and updates your README.
- **`README.md`**: Contains a placeholder that will be replaced by your current song.

---

## Setup Instructions

### 1. Register a Spotify App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Click **Create an App**.
3. Copy **Client ID** and **Client Secret**.
4. Add a **Redirect URI**: `http://127.0.0.1:8080/callback`.
5. Generate a **Refresh Token** using the authorization code flow.
   - You can use the Python script or Django flow from this repo to obtain it.

---

### 2. Add GitHub Secrets

Go to your repository → **Settings → Actions → Secrets and variables → Actions** and add:

- `SPOTIFY_CLIENT_ID` → your Spotify Client ID
- `SPOTIFY_CLIENT_SECRET` → your Spotify Client Secret
- `SPOTIFY_REFRESH_TOKEN` → your Spotify refresh token

---

### 3. Add Placeholder in README

Add this placeholder in your `README.md` where you want your current song to appear:

```md
<!-- SPOTIFY -->Loading...<!-- END_SPOTIFY -->

- <!-- SPOTIFY --> → start marker

- Loading... → default text

- <!-- END_SPOTIFY --> → end marker

Example:

## Currently Listening To:

<!-- SPOTIFY -->Loading...<!-- END_SPOTIFY -->

4. Place the Python Script and Workflow

Upload nowplaying.py to the root of your repository.

Upload .github/workflows/spotify.yml to the workflow folder:

.github/
└── workflows/
└── spotify.yml
```

5. Test Locally (Optional)

Before pushing to GitHub:

export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
export SPOTIFY_REFRESH_TOKEN="your_refresh_token"
python nowplaying.py
cat spotify.txt

- This should show your currently playing track.

6. Run Workflow on GitHub

   1. Commit and push all files (nowplaying.py, .yml, README.md).

   2. Go to Actions tab → Update Spotify Now Playing → Run workflow.

   3. After it runs, your README placeholder will be replaced with your current song.

7. Example Output

After workflow runs, your README will show:

🎶 Blinding Lights — The Weeknd

or if nothing is playing:

🎧 Not playing anything

Notes

Make sure your GitHub Actions secrets are correct — otherwise the workflow will fail.

Workflow runs every 5 minutes automatically.

No sensitive information is exposed in your README — only your currently playing track.
