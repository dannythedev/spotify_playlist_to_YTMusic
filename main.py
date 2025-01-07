import os
import re
from SpotifyAPI import SpotifyAPI
from YouTubeMusicFetcher import PlaylistManager

# Configuration
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

spotify_playlist_id = input('Enter spotify playlist ID or URL:')
if spotify_playlist_id.startswith('http'):
    spotify_playlist_id = re.search(r"playlist/([a-zA-Z0-9]+)|playlist/([^?&]+)", spotify_playlist_id).group(1)

PLAYLIST_JSON = 'cache/playlist_{playlist_id}.json'.format(playlist_id=spotify_playlist_id)

# Convert and create playlist
if not os.path.exists(PLAYLIST_JSON):
    converter = SpotifyAPI(spotify_client_id, spotify_client_secret, spotify_playlist_id)
    converter.get_playlist_tracks()
    playlist_manager = PlaylistManager(PLAYLIST_JSON)
    playlist_manager.fetch_and_update_youtube_urls()
    playlist_manager.batch_seperate_to_playlist_urls(PLAYLIST_JSON)
