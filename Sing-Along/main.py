from save_file import saveToFile
from many_links import getAllLinks


def writeLyrics(choice):
    try:
        choice = int(choice)
    except ValueError:
        print("PLEASE ENTER INTEGER ONLY !!")

    if choice == 1:
        url = input("Enter URL :  ")
        saveToFile(url)
    
    elif choice == 2:
        urls = getAllLinks()
        for url in urls:
            if url:
                saveToFile(url.strip())
    else:
        print("Choose either  1  or  2 !!")


if __name__ == "__main__":
    choice = input("\n\t(1) Direct URL\n\t(2) 'links.txt' file -->  ")
    writeLyrics(choice)
    print("\n**** PROCESS COMPLETED ****")

    



