import re
import json
import requests

CONFIG = json.load(open("config.json", encoding="utf-8"))

SOURCE_URL = "https://westiecommunity.de/?post_type=tribe_events&ical=1&eventDisplay=list"

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

# Build filtered ICS
output_filtered = (
    "BEGIN:VCALENDAR\n"
    "VERSION:2.0\n"
    "PRODID:-//Filtered Westie Calendar//EN\n"
    "CALSCALE:GREGORIAN\n"
    "METHOD:PUBLISH\n"
    + "\n".join(filtered)
    + "\nEND:VCALENDAR"
)

open("calendar.ics", "w", encoding="utf-8").write(output_filtered)
print("calendar.ics generated.")

# Build excluded ICS
output_excluded = (
    "BEGIN:VCALENDAR\n"
    "VERSION:2.0\n"
    "PRODID:-//Excluded Westie Calendar//EN\n"
    "CALSCALE:GREGORIAN\n"
    "METHOD:PUBLISH\n"
    + "\n".join(excluded)
    + "\nEND:VCALENDAR"
)

open("calendarexc.ics", "w", encoding="utf-8").write(output_excluded)
print("calendarexc.ics generated.")
