import time
import pyautogui as pg

time.sleep(2)
search = open("MTG Card Wishlist.txt", "r").readlines()

sites = ["shuffleandcutgames", "gamingdna", "cardmerchant", "goblingames"]
website = sites[0]

i = 0
for line in search:
    search[i] = line.replace(" ", "+")
    i += 1

# shuffleandcutgames
for i in range(len(search)):
    if website == "shuffleandcutgames":
        if i == 0:
            pg.write("firefox ")
        # .strip() removes \n at end of line
        pg.write(f"https://www.shuffleandcutgames.co.nz/search?q=*{search[i].strip()}* ")

    if website == "gamingdna":
        if i == 0:
            pg.write("firefox ")
        # .strip() removes \n at end of line
        pg.write(f"https://gamingdna.co.nz/search?q=*{search[i].strip()}* ")

    if website == "cardmerchant":
        if i == 0:
            pg.write("firefox ")
        # .strip() removes \n at end of line
        pg.write(f"https://cardmerchant.co.nz/search?q=*{search[i].strip()}* ")

    if website == "goblingames":
        if i == 0:
            pg.write("firefox ")
        # .strip() removes \n at end of line
        pg.write(f"https://goblingames.nz/search?q={search[i].strip()} ")

pg.press("enter")
