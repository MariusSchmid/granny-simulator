def menu():
    print("Menü: ")
    print("1. Google Suche ")
    print("2. YouTube Video schauen ")


def open_google():
    return

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