import json
import os
import re
import requests
from ytmusicapi import YTMusic
from Functions import calculate_tfidf_similarity

PLAYLIST_LINK = 'https://www.youtube.com/watch_videos?video_ids={video_ids}'

class YouTubeMusicFetcher:
    def __init__(self, playlist_json):
        self.playlist_json = playlist_json
        self.ytmusic = YTMusic()
        self.THRESHOLD = 70

    def get_youtube_music_url(self, song, artist):
        query = f"{song} {artist}"
        search_results = self.ytmusic.search(query)
        if search_results:
            filtered_results = []
            for vid in search_results:
                if vid.get('videoType') == 'MUSIC_VIDEO_TYPE_ATV':
                    vid['title_similarity'] = calculate_tfidf_similarity(vid.get('title', '').lower(), song.lower())
                    if vid.get('artists'):
                        vid['artist_similarity'] = calculate_tfidf_similarity(vid['artists'][0].get('name', '').lower(),
                                                                       artist.lower())
                        vid['total_similarity'] = vid['artist_similarity'] + vid['title_similarity']
                        filtered_results.append(vid)

            filtered_results = [vid for vid in filtered_results if vid['total_similarity'] >= self.THRESHOLD]
            filtered_results.sort(key=lambda x: x['total_similarity'], reverse=True)

            if filtered_results:
                video_id = filtered_results[0].get('videoId')
            else:
                video_id = [vid['videoId'] for vid in search_results if 'videoId' in vid][0]
            if video_id:
                return f"https://music.youtube.com/watch?v={video_id}"
        return None


class PlaylistManager:
    def __init__(self, playlist_json):
        self.playlist_json = playlist_json
        self.songs = self.load_songs()
        self.counter = 0

    def load_songs(self):
        with open(self.playlist_json, 'r') as file:
            return json.load(file)

    def fetch_and_update_youtube_urls(self):
        fetcher = YouTubeMusicFetcher(self.playlist_json)
        for index, song_info in enumerate(self.songs):
            song = song_info.get("name")
            artist = song_info.get("artist")
            if "YoutubeURL" not in song_info:  # Add YoutubeURL if it doesn't exist
                url = fetcher.get_youtube_music_url(song, artist)
                if url:
                    self.counter += 1
                    song_info["YoutubeURL"] = url  # Update the URL directly
                    print(f"{song} by {artist}: {song_info.get('YoutubeURL')}")
                else:
                    song_info["YoutubeURL"] = "Not found"

            # Write the updated song back to the file after modification
            with open(self.playlist_json, 'r') as file:
                existing_songs = json.load(file)
            existing_songs[index] = song_info
            with open(self.playlist_json, 'w') as file:
                json.dump(existing_songs, file, indent=4)


    def batch_seperate_to_playlist_urls(self, PLAYLIST_JSON):
        batch_urls = {}  # Dictionary to hold batch mappings

        # Load JSON data
        if os.path.exists(PLAYLIST_JSON):
            with open(PLAYLIST_JSON, 'r') as file:
                all_songs = json.load(file)
                chunk_size = 49
                total_songs = len(all_songs)
                num_chunks = (total_songs + chunk_size - 1) // chunk_size  # Calculate total chunks

                print(f'Successfully exported {self.counter}/{total_songs} songs.')

                for i in range(num_chunks):
                    # Get the current chunk of songs
                    start_idx = i * chunk_size
                    end_idx = min((i + 1) * chunk_size, total_songs)
                    songs = all_songs[start_idx:end_idx]

                    # Extract YouTube URLs and format them
                    songs_list = '\n'.join([song['YoutubeURL'] for song in songs])
                    song_regex = r'v=([^&]+)'
                    songs_id_format = ','.join(
                        [re.search(song_regex, song['YoutubeURL']).group(1) for song in songs if
                         re.search(song_regex, song['YoutubeURL'])]
                    )

                    # Make the playlist request
                    response = requests.get(PLAYLIST_LINK.format(video_ids=songs_id_format))
                    if response.status_code == 200:
                        music_url = re.sub(r'www', 'music', response.url, 1)
                        # Map the current chunk to the response URL
                        batch_key = f"{start_idx}-{end_idx - 1}"
                        batch_urls[batch_key] = music_url
                        print(f'Generated songs {batch_key}.\n Url: {music_url}')

            # Save the batch URLs to the playlist JSON file
            with open(PLAYLIST_JSON, 'r') as file:
                existing_data = json.load(file)
            existing_data.append(batch_urls)
            with open(PLAYLIST_JSON, 'w') as file:
                json.dump(existing_data, file, indent=4)
        else:
            print(f"Error: The file '{PLAYLIST_JSON}' does not exist.")