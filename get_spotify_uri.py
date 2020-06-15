import requests
from secrets import spotify_user_id, spotify_token
from scrape_song_info import scrape_song_info
from get_genius_lookups import get_genius_lookups


def get_spotify_uri(song, artist) -> str:
    """ given a song and an artist, return a uri to that song in Spotify """

    query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
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
