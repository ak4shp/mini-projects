from bs4 import BeautifulSoup as bfs
import requests as rqs


# Title :
def getTitle(title: str):
    title_str = title[4:]    # slices the title's Name 
    title_list = title_str.split("lyrics")
    return title_list[0]


# LYRICS :
def replaceFromLyrics(lyrics):
    replaceables = {'<div class="lyric-text">' : "", 
                    '<blockquote>' : "", 
                    '<p>' : " ", 
                    '<br/>' : "\n", 
                    '</p>' : "", 
                    '</blockquote> </div>' : "", 
                    '</div>' : "", 
                    '[' : "", 
                    ']' : ""
                    }
    for old, new in replaceables.items():
        lyrics = lyrics.replace(old, new)
    return lyrics


def fetch_Source1_Lyrics(url):
    response = rqs.get(url)
    soup = bfs(response.text, 'lxml')

    title_header = str(soup.find('h1'))
    title = getTitle(title_header).strip()

    lyrics_header = str(soup.find_all('div', class_ = 'lyric-text'))
    lyrics_str = replaceFromLyrics(lyrics_header)
    lyrics_text = f"** {title} ** {lyrics_str}"
    return title, lyrics_text

