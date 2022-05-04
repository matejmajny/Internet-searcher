#imports
import time
import webbrowser
from colorama import *
#Thanks
print("Thank you for downloading this thing lol\n")
init()

#██╗███╗░░██╗████████╗███████╗██████╗░███╗░░██╗███████╗████████╗
#██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗████╗░██║██╔════╝╚══██╔══╝
#██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝██╔██╗██║█████╗░░░░░██║░░░
#██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██║╚████║██╔══╝░░░░░██║░░░
#██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░╚███║███████╗░░░██║░░░
#╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
#
#░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
#██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗
#╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝
#░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗
#██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║
#╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
# Made by @matejmajny, improved by @dumpydev.
#ask for input
engine1 = input("Which search engine you want use? \n[G] Google \n[Y] Yandex \n[D] DuckDuckGo \n[S] Startpage \n[B] Bing\n")
search = input("\nFor what do you want to search? ") 
print("")

engine = engine1.lower()

#check what engine it is.
if engine == "g" or engine == "google":
    print(Fore.BLUE + "Googling...")
    time.sleep(2)
    webbrowser.open("https://www.google.com/search?q=" + search)

elif engine == "y" or engine == "yandex":
    print(Fore.RED + "Yandexing...")
    time.sleep(2)
    webbrowser.open("https://yandex.com/search/?text=" + search)

elif engine == "d" or engine == "duckduckgo":
    print(Fore.YELLOW + "DuckDuckGoing...")
    time.sleep(2)
    webbrowser.open("https://duckduckgo.com/?q=" + search)

elif engine == "s" or engine == "startpage":
    print(Fore.BLUE + "Startpaging...")
    time.sleep(2)
    webbrowser.open("https://www.startpage.com/do/search?query=" + search)
# who the fuck uses this?
elif engine == "b" or engine == "bing":
    print(Back.RED + "Binging...")
    time.sleep(2)
    webbrowser.open("https://www.bing.com/search?q=" + search)

else:
    print(Back.RED + "Sorry, but " + engine1 + " is not supported")

input("\nHit ENTER to exit")