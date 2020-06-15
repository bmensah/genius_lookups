import browserhistory as bh


def get_genius_lookups() -> list:
    """
    Search browser history for hits to Genius.com. Isolate lyric lookups.
    Return a list of links to lyrics.
    """
    # get dictionary with full browser history
    dict_obj = bh.get_browserhistory()
    links = []
    # isolate chrome history and find searches for lyrics on genius.com
    # will add same functionality for other browsers soon
    for value in dict_obj['chrome']:
        if 'genius.com' in value[0] and value[0][-6:] == 'lyrics':
            links.append(value[0])

    return links
