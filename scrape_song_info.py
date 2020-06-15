import requests
import html
from bs4 import BeautifulSoup
from unicodedata import normalize


def scrape_song_info(url) -> list:
    """ Scrape Genius.com lyrics searches for artist and song and return as a list """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = html.unescape(str(soup.title))

    # get artist name substring, strip off whitespace, and normalize any unicode chars
    start = title.find('<title>') + len('<title>')
    end = title.find(chr(8211))
    artist_name = normalize('NFKD', title[start:end].strip())

    # get song name substring, strip off whitespace, and normalize any unicode chars
    start = title.find(chr(8211)) + len(chr(8211))
    end = title.find("Lyrics |")
    song_name = normalize('NFKD', title[start:end].strip())

    # add artist name and song name to a list, return list
    info = [artist_name, song_name]
    return info
