# Import Country flags for cards

import os
import urllib.request

flags = {
    "south_africa": "za",
    "chile": "cl",
    "brazil": "br",
    "uganda": "ug",
    "egypt": "eg",
    "germany": "de",
    "france": "fr",
    "india": "in",
    "new_zealand": "nz",
    "japan": "jp"
}

os.makedirs("static/images/flags", exist_ok=True)

print("Downloading local SVG flags.")
for name, code in flags.items():
    url = f"https://flagcdn.com/{code}.svg"
    filepath = f"static/images/flags/{name}.svg"

    try:
        urllib.request.urlretrieve(url, filepath)
        print(f" [SUCCESS] Saved {name}.svg")
    except Exception as e:
        print(f" [ERROR] failed to download {name}.svg: {e}")

print("\nDone. All 10 flag SVG's are saved.")