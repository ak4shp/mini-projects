import os

def getAllLinks():
    current_url = []
    this_dir = str(os.getcwd())
    file_dir = f"{this_dir}\\Lyrics_links\\links.txt"
    file = open(file_dir, "r")
    for line in file:
        line = line.replace('\n', '')
        current_url.append(line)
    # print(current_url)
    file.close()
    return current_url

