from bs4 import BeautifulSoup as bfs
import requests as rqs


# LYRICS Formatting
def replaceFromLyrics(lyrics: str):
    replaceables = {'<div class="lyr_data"><strong>Lyrics</strong><div class="_inner">' : "", 
                    '<p>' : "", 
                    '<br/>' : "", 
                    '</div>' : "", 
                    '</p>' : "", 
                    '[' : "", 
                    ']' : ""
                    }
    for old, new in replaceables.items():
        lyrics = lyrics.replace(old, new)
    return lyrics


def fetch_Source2_Lyrics(url : str):
    response = rqs.get(url)
    soup = bfs(response.text, 'lxml')

    # Lyrics TITLE
    title_header = str(soup.find('h1', class_ = 'title t_over'))
    title_str = title_header[32:].split("Lyrics")
    title = title_str[0].strip()

    # LYRICS
    lyrics_header = str(soup.find_all('div', class_ = 'lyr_data'))
    lyrics_str = replaceFromLyrics(lyrics_header)

    # Lyrics TEXT
    lyrics_text = f"** {title} **\n\n {lyrics_str}"
    return title, lyrics_text