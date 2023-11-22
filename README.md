# MTG-Card-Search-NZ
A python script that searches a wishlist of MTG cards on common New Zealand MTG card retailers.

## How to use
Open the "MTG Card Wishlist.txt" file and write down what cards you want to search for, then save. Make sure there is no punctuation in the card names, such as commas or hyphens. Upper or lower case does not matter.

Have a terminal open and run the code. You have a 2-second window to tab over to the terminal before the script writes out the searches and executes.

## Advanced
By default, the program will search https://www.shufflencutgames.co.nz. You can alter the "website" variable within "MTG Card Search NZ.py" to select from a variety of pre-added websites, such as https://gamingdna.conz, https://cardmerchant.co.nz and https://goblingames.nz. Feel free to add your own websites.

Also by default is the use of firefox, executing it in the terminal. Feel free to change this too.

## Troubleshooting
Since this script uses pyautogui to write in the terminal, you can move your mouse to the top-left of your screen as a fail-safe abort.
