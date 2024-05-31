ASTD-UIAS(Unit Information and Stats)
====
This is the official repository and issue-tracker for ASTD-UIAS

ASTD-UIAS is meant to provide players with useful information regarding their favorite ASTD characters.

You can check out unit data without using this software by going here: https://docs.google.com/spreadsheets/d/1U2aB8bV154fXYi3sX4pvs6W6Mk-LWjswPqWY4hD6fYw/edit?usp=sharing though it won't always be updated, hence the code provided.

The current version of this software works by scraping the ASTD wiki for all relevant characters and character stats. Those stats need to be uploaded to excel to be properly accessed and calculated.

Dependencies
====
Python 3.11(+)

requirements.txt

Installation
====
1. Create a python3 .venv (recommended) (https://docs.python.org/3/library/venv.html)
2. Open cmd.exe
3. Paste: pip install -r requirements.txt

Alternatively using https://pypi.org/:
1. Follow steps 1(recommended) and 2
2. Install beautifulsoup4, requests, and html5lib

What to do after running ASTD-UIAS:
1. Download the excel sheet provided in README.md
2. UIAS will generate some .csv files for you to upload to excel.
3. Replace the respective sheets in excel with the .csv files provided

Quick Tips
====
After running ASTD-UIAS.py, be sure to check each .csv file's length. Each file should be the exact same length. This is done to ensure character stats line up with each other.

updateList.py should be ran every time the WIKI gets updated, not ASTD. The data gathered is from the wiki, not the game itself. 

A list is provided if you do not wish to generate one yourself. Be aware, this list will not be updated, its only provided for accessibility.

Certain units are blacklisted. At the moment I don't have a way to easily deal with those units, so they're out for now.

Still Need Help?
====
When reporting an issue put the version number before the issue title! Such as [0.05]This software is broken! Also, please provide as much information as possible when reporting issues!

A Discord may be provided at a later date.

Notice of Non-Affiliation and Disclaimer
====
ASTD-UIAS is not affiliated, associated, authorized, endorsed by, or in any way officially connected with All Star Tower Defence nor its development team Top Down Games.
