import json
import requests
from get_genius_lookups import get_genius_lookups
from scrape_song_info import scrape_song_info
from get_spotify_uri import get_spotify_uri
from secrets import spotify_user_id, spotify_token


def create_playlist():
    """ Create a Spotify Playlist. Return playlist iD. """

    # make spotify playlist
    request_body = json.dumps({
        "name": "Genius Lookups",
        "description": "playlist of songs looked up on Genius.com",
        "public": False,
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token),
        }
    )

    response_json = response.json()
    # playlist id
    return response_json["id"]