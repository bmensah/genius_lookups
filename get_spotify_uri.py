import requests
import re
from secrets import spotify_token


def get_spotify_uri(song, artist) -> str:
    """ given a song and an artist, return a uri to that song in Spotify """

    song = re.sub("['|\s]", '%20', song)
    artist = re.sub("['|\s]", '%20', artist)
    query = "https://api.spotify.com/v1/search?q=track:{}+artist:{}&type=track&offset=0&limit=20".format(
        song, artist)

    response = requests.get(query, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(spotify_token)
    })

    response_json = response.json()
    song_info = response_json['tracks']['items']
    if song_info:
        return song_info[0]['uri']
    else:
        return ''

