import json
import requests

from get_genius_lookups import get_genius_lookups
from scrape_song_info import scrape_song_info
from get_spotify_uri import get_spotify_uri
from create_playlist import create_playlist
from secrets import spotify_token


def add_songs():
    # get links to genius lyrics searches from browser history
    links = get_genius_lookups()
    uris = []
    for link in links:
        # extract song title and artist. get uri
        info = scrape_song_info(link)
        uri = get_spotify_uri(info[0], info[1])
        if uri:
            uris.append(uri)

    # create a new playlist
    playlist_id = create_playlist()

    # add all songs into new playlist
    request_data = json.dumps(uris)
    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
    response = requests.post(
        query,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

    response_json = response.json()
    return response_json


add_songs()
