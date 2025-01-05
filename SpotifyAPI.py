import os

import requests
import json


class SpotifyAPI:
    def __init__(self, client_id, client_secret, playlist_id, base_dump_dir='cache'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.playlist_id = playlist_id
        self.playlist_dump_file = os.path.join(base_dump_dir, f'playlist_{playlist_id}.json')
        self.access_token = None

    def get_access_token(self):
        url = "https://accounts.spotify.com/api/token"
        payload = {'grant_type': 'client_credentials'}
        auth = (self.client_id, self.client_secret)
        response = requests.post(url, data=payload, auth=auth)
        token_info = response.json()
        self.access_token = token_info['access_token']
        return self.access_token

    def get_playlist_tracks(self):
        if not self.access_token:
            self.get_access_token()

        # Check if the playlist data file exists
        if os.path.exists(self.playlist_dump_file):
            with open(self.playlist_dump_file, 'r') as file:
                return json.load(file)

        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {'limit': 100, 'offset': 0}
        all_tracks = []

        while True:
            response = requests.get(url, headers=headers, params=params)
            playlist_data = response.json()

            if 'items' not in playlist_data:
                break

            all_tracks.extend(playlist_data['items'])

            if len(playlist_data['items']) < params['limit']:
                break
            params['offset'] += params['limit']

        tracks = [{'name': track['track']['name'], 'artist': track['track']['artists'][0]['name']} for track in
                  all_tracks]
        self._dump_playlist_data(tracks)
        return tracks

    def _dump_playlist_data(self, tracks):
        if not os.path.exists(os.path.dirname(self.playlist_dump_file)):
            os.makedirs(os.path.dirname(self.playlist_dump_file))
        with open(self.playlist_dump_file, 'w') as file:
            json.dump(tracks, file, indent=4)

