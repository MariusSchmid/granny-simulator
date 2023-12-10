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
    print("3. WhatsApp ")


def open_browser_url(url):
    specific_browser_path =  os.environ.get('BROWSER_PATH')
    if specific_browser_path:
        print(specific_browser_path)
        webbrowser.get(f"{specific_browser_path} %s").open(url)
    else:
        webbrowser.open(url)

def open_google():
    print("Google Suche")
    search_query = input("Bitte gib ein, nach was du suchen möchtest:")
    open_browser_url(f"https://www.google.com/search?q={search_query}")


def open_youtube():
    search_query = input("Bitte gib ein, nach was du suchen möchtest:")
    open_browser_url(f"https://www.youtube.com/results?search_query={search_query}")

def escape_all():
    #os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM WhatsApp.exe /F")
    all_windows_titles = gw.getAllTitles()
    matching_windows_string = [s for s in all_windows_titles if "main.exe" in s]
    print(matching_windows_string)
    granny_simulator =  gw.getWindowsWithTitle(matching_windows_string[0])[0]
    os.system('cls')
    show_menu()
    granny_simulator.maximize()

def open_whatsapp():
    whatsapp_path = r'C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2348.4.0_x64__cv1g1gvanyjgm'
    print(f"this is the path to whatsapp.exe {whatsapp_path}")
    os.chdir(whatsapp_path)
    os.system(f'start WhatsApp.exe')


def main():
    hkm.listen_to_hotkeys(escape_all)
    while True:
        show_menu()
        choice = input("Bitte wähle einen Menüpunkt aus.")
        if choice == "1":
            open_google()
        elif choice == "2":
            open_youtube()
        elif choice == "3":
            open_whatsapp()
        else:
            print(f"Der Menüpunkt {choice} existiert nicht.")



if __name__ == "__main__":
    main()

