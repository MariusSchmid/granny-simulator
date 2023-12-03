import webbrowser
from pynput import keyboard

def menu():
    print("Menü: ")
    print("1. Google Suche ")
    print("2. YouTube Video schauen ")


def open_google():
    print("Google Suche")

    search_query = input("Bitte geben sie ein nach was sie suchen wollen:")

    google_url = f"https://www.google.com/search?q={search_query}"

    webbrowser.open(google_url)


def open_youtube():

    search_query = input("Bitte geben sie ein nach was sie suchen wollen:")

    youtube_url = f"https://www.youtube.com/results?search_query={search_query}"

    webbrowser.open(youtube_url)

def escape_all():
    print("exit")

def main():

    with keyboard.GlobalHotKeys({
            'n': escape_all() })  as h:
        h.join()

    while True:
        menu()
        choice = input("Bitte wählen sie einen Menüpunkt aus!")

        if choice == "1":
            open_google()
        elif choice == "2":
            open_youtube()



if __name__ == "__main__":
    main()

