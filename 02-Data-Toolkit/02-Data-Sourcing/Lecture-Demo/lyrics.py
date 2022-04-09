import requests


def fetch_lyrics(artists, title):
    """
    Get lyrics from Seeds Lyrics API. Returns empty string if song not found
    """
    url = f'https://lyrics.lewagon.ai/search?artist={artists}&title={title}'
    response = requests.get(url)
    if response.status_code != 200:
        return ''
    data = response.json()
    return data['lyrics']
