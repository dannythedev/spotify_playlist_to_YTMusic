# Spotify to YouTube Music Playlist Converter

## Overview
This repository provides a Python-based tool to convert Spotify playlists into YouTube Music batch URLs. By providing a Spotify playlist ID or URL, the script fetches track information from Spotify and fetches corresponding YouTube Music URLs. The results are divided into batches of 49 songs, with each batch represented by a unique YouTube Music playlist URL.

## Features
- Converts Spotify playlist by ID or URL into YouTube Music batch URLs.
- Supports fetching track details from Spotify API.
- Splits the playlist into manageable chunks of 49 songs each.
- Saves batch URLs directly into a JSON file for future use.
- Manually adding 980 songs to a YouTube Music playlist now became much easier, with only 20 clicks.

## Prerequisites
1. **Spotify API Credentials**  
   You need to have the following credentials:
   - `SPOTIFY_CLIENT_ID`: Your Spotify API client ID.
   - `SPOTIFY_CLIENT_SECRET`: Your Spotify API client secret. 
   - To get your own Spotify API Key, [Spotify Developer Dashboard](https://developer.spotify.com/dashboard), press the 'Create app' button, and you'll find the required credentials.


2. **Python Environment**  
   - Install Python 3.6+.
   - Install required libraries using `pip install -r requirements.txt`.

## **Usage**
   - Once the program finishes running, a `cache` folder will be created in the project directory root. 
   - Navigate to the end of the `.json` file corresponding to the Spotify ID. 
   - You will find the batch YouTube Music URLs listed there.
### Example:
When using the tool and providing a Spotify URL or ID such as:
[https://open.spotify.com/playlist/1LTlRP0hzDdpsnTSevIaMz](https://open.spotify.com/playlist/1LTlRP0hzDdpsnTSevIaMz)

A `1LTlRP0hzDdpsnTSevIaMz.json` file will be generated inside the `cache` folder.
This file will contain all the songs from the Spotify Playlist, albeit in the corresponding YouTube Music URL format:
```json
    [
    {
        "name": "Long Train Runnin'",
        "artist": "The Doobie Brothers",
        "YoutubeURL": "https://music.youtube.com/watch?v=m4tJSn0QtME"
    },
    {
        "name": "5-7-0-5",
        "artist": "City Boy",
        "YoutubeURL": "https://music.youtube.com/watch?v=AHm3w-50Vwc"
    },
    {
        "name": "More Than a Feeling",
        "artist": "Boston",
        "YoutubeURL": "https://music.youtube.com/watch?v=t4QK8RxCAwo"
    },
    {
        "name": "China Grove",
        "artist": "The Doobie Brothers",
        "YoutubeURL": "https://music.youtube.com/watch?v=RX7iHsAIw9o"
    },
```
At the bottom of the JSON file, batch YouTube Music URLs for easy playlist import are added:
```json
    {
        "0-48": "https://music.youtube.com/watch?v=m4tJSn0QtME&list=TLGGXM-hdX72TC8wNTAxMjAyNQ",
        "49-62": "https://music.youtube.com/watch?v=55xQu9eIPIA&list=TLGGhfKmaUp1PQ0wNTAxMjAyNQ"
    }
```
Instead of saving each song manually (63 songs), only (63//49) 2 actions are required to import the entire playlist into YouTube Music.

Open the URLs in your browser, press ![youtube_save_Button](https://github.com/user-attachments/assets/56308220-4536-4ba1-b5c1-4c8c81bc177e) once to batch-save 49 songs, and then select the YouTube Music playlist of your choice!

