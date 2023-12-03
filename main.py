import os
import subprocess
import sys
import webbrowser
import hotkey_manager as hkm
import pygetwindow as gw

def show_menu():
    print("Menü: ")
    print("1. Google Suche ")
    print("2. YouTube Video schauen ")


def open_browser_url(url):
    specific_browser_path =  os.environ.get('BROWSER_PATH')
    if specific_browser_path:
        print(specific_browser_path)
        webbrowser.get(f"{specific_browser_path} %s").open(url)
    else:
        webbrowser.open(url)

def open_google():
    print("Google Suche")
    search_query = input("Bitte geben sie ein nach was sie suchen wollen:")
    open_browser_url(f"https://www.google.com/search?q={search_query}")


def open_youtube():
    search_query = input("Bitte geben sie ein nach was sie suchen wollen:")
    open_browser_url(f"https://www.youtube.com/results?search_query={search_query}")

def escape_all():
    os.system("taskkill /IM chrome.exe /F")
    all_windows_titles = gw.getAllTitles()
    matching_windows_string = [s for s in all_windows_titles if "main.exe" in s]
    print(matching_windows_string)
    granny_simulator =  gw.getWindowsWithTitle(matching_windows_string[0])[0]
    os.system('cls')
    show_menu()
    granny_simulator.maximize()

def main():
    hkm.listen_to_hotkeys(escape_all)
    while True:
        show_menu()
        choice = input("Bitte wählen sie einen Menüpunkt aus!")
        if choice == "1":
            open_google()
        elif choice == "2":
            open_youtube()



if __name__ == "__main__":
    main()

