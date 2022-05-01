print("Thank you for downloading this thing lol")
print("\n")


#modules + input

engine1 = input("Which search engine you want use? Google, Yandex, DuckDuckGo, Startpage or Bing? ")
search = input("\nFor what do you want to search? ")

engine = engine1.lower()

import time
import webbrowser

#search

if engine == "google":
    print("Googling...")
    time.sleep(2)
    webbrowser.open("https://www.google.com/search?q=" + search)

elif engine == "yandex":
    print("Yandexing...")
    time.sleep(2)
    webbrowser.open("https://yandex.com/search/?text=" + search)

elif engine == "duckduckgo":
    print("DuckDuckGoing...")
    time.sleep(2)
    webbrowser.open("https://duckduckgo.com/?q=" + search)

elif engine == "startpage":
    print("Startpaging...")
    time.sleep(2)
    webbrowser.open("https://www.startpage.com/do/search?query=" + search)

elif engine == "bing":
    print("Binging...")
    time.sleep(2)
    webbrowser.open("https://www.bing.com/search?q=" + search)

else:
    print("Sorry, but " + engine1 + " is not supported")

input("\nHit ENTER to exit")