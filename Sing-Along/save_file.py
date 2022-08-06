from sources import choose_source
import os


def makeFolder():
    ...

def makeDIR():
    current_dir = os.getcwd()
    new_dir = os.path.join(current_dir, r"Lyrics_data")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)


def select_save_format():
    val = input("Output Format - (1) txt\n\t\t(2) src -> ")
    try:
        val = int(val)
    except ValueError:
        print("PLEASE ENTER INTEGER ONLY !!")

    if val == 1:
        save_type = '.txt'
    elif val == 2:
        save_type = '.src'
    else:
        save_type = '.txt'
        print("'.txt' saved as default. Select  1  or  2  only !!")
    return save_type

save = select_save_format()


def saveToFile(url):
    makeDIR()
    title, lyrics_text = choose_source(url)
    cd = os.getcwd()
    text_file = open(f"{cd}\\Lyrics_data\\{title}{save}", "w", encoding = "utf-8")
    text_file.write(lyrics_text)
    text_file.close()
    
    print("Creating file ... ")
    print(f"Lyrics file <<{title}>> Successfully created !!")
