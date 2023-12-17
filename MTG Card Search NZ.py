import os

def CardSearch(website):
    search = open("MTG Card Wishlist.txt", "r").readlines()
    command = ["firefox"]

    for index, line in enumerate(search):
        search[index] = line.replace(" ", "+")

    for index, site in enumerate(["shuffleandcutgames", "gamingdna", "cardmerchant", "goblingames"]):
        if site == website:
            for i in range(len(search)):
                    site_search = [f"https://www.shuffleandcutgames.co.nz/search?q=*{search[i].strip()}*", f"https://gamingdna.co.nz/search?q=*{search[i].strip()}*", f"https://cardmerchant.co.nz/search?q=*{search[i].strip()}*", f"https://goblingames.nz/search?q={search[i].strip()}"]
                    command.append(site_search[index])

    os.system(" ".join(command))

if __name__ == "__main__":
    sites = ["shuffleandcutgames", "gamingdna", "cardmerchant", "goblingames"]
    CardSearch(sites[0])
