from lyrics_source1 import fetch_Source1_Lyrics
from lyrics_source2 import fetch_Source2_Lyrics


def choose_source(url):
    S1 = 'gaana'
    S2 = 'lyricsgram'
    U1 = url.replace('/', '.')
    U2 = U1.split('.')
    if S2 in U2:
        title, lyrics_text = fetch_Source1_Lyrics(url)
    elif S1 in U2:
        title, lyrics_text = fetch_Source2_Lyrics(url)
    else:
        print("Use links from 'gaana.com' or 'lyricsgram.com' only !")
    return title, lyrics_text

