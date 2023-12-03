import webbrowser

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
    return

def main():
    while True:
        menu()
        choice = input("Bitte wählen sie einen Menüpunkt aus!")

        if choice == "1":
            open_google()
        elif choice == "2":
            open_youtube()


if __name__ == "__main__":
    main()

