import re
import json

CONFIG = json.load(open("config.json", encoding="utf-8"))

SOURCE_URL = "https://westiecommunity.de/?post_type=tribe_events&ical=1&eventDisplay=list"

import requests

ics = requests.get(SOURCE_URL).text

events = ics.split("BEGIN:VEVENT")
filtered = []
excluded = []

for e in events:
    block = "BEGIN:VEVENT" + e if "END:VEVENT" in e else None
    if not block:
        continue

    # Filter: Keywords (Beginner etc.)
    if any(kw.lower() in block.lower() for kw in CONFIG["exclude_keywords"]):
        excluded.append(block)
        continue

    # Filter: Locations
    if any(loc.lower() in block.lower() for loc in CONFIG["exclude_locations"]):
        excluded.append(block)
        continue

    filtered.append(block)

# Build final ICS
output = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
output += "\n".join(filtered)
output += "\nEND:VCALENDAR"

open("calendar.ics", "w", encoding="utf-8").write(output)
print("calendar.ics generated.")

# Build final ICS
output = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
output += "\n".join(excluded)
output += "\nEND:VCALENDAR"

open("calendarexc.ics", "w", encoding="utf-8").write(output)
print("calendarexc.ics generated.")


