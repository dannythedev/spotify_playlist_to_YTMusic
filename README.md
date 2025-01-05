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
   
2. **Python Environment**  
   - Install Python 3.6+.
   - Install required libraries using `pip install -r requirements.txt`.