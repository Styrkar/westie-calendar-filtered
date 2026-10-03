# 📅 Westie Community – Filtered Calendar Feed

This repository generates a **filtered, Outlook‑compatible ICS calendar feed** based on the public Westie Community event calendar:

https://westiecommunity.de/?post_type=tribe_events&ical=1&eventDisplay=list (westiecommunity.de in Bing)

Code

The feed is automatically cleaned, filtered, and published via **GitHub Pages**, allowing Outlook.com and other calendar apps to subscribe to a stable, static `.ics` file.

---

## ⭐ Features

- **Automatic daily updates** (via GitHub Actions)
- **Only commits when the calendar actually changes**
- **Filters out unwanted events**, including:
  - Beginner / entry‑level workshops
  - Events in specific excluded cities
- **Fully configurable** via `config.json`
- **Published as a static ICS file** compatible with:
  - Outlook.com (personal accounts)
  - Outlook Desktop
  - iOS / Android calendar apps
  - Google Calendar

---

## 📁 Repository Structure

westie-calendar-filtered/
│
├── filter.py          # Fetches, filters, and generates calendar.ics
├── config.json        # User-defined filters (keywords, locations)
├── calendar.ics       # Auto-generated filtered calendar feed
│
└── .github/
└── workflows/
└── update.yml # Daily update workflow

Code

---

## ⚙️ Configuration (`config.json`)

You can adjust filters at any time by editing `config.json`:

```json
{
  "exclude_locations": ["Wuppertal", "Mülheim", "Essen"],
  "exclude_keywords": ["Beginner", "Einsteiger", "Anfänger"],
  "include_all_other_events": true
}
```

### Supported filters:
exclude_locations  
Removes events whose location contains any of these city names.

### exclude_keywords  
Removes events whose title or description contains any of these words.

### include_all_other_events  
If set to true, all remaining events are included.

After changing the file, the next scheduled workflow run will regenerate the calendar.

## 🔧 How the Generator Works (filter.py)
Downloads the original ICS feed

Splits it into individual events

Applies filters from config.json

Rebuilds a clean, valid calendar.ics

Saves the result to the repository root

The workflow commits the file only if it changed

## 🤖 Automated Updates (update.yml)

The GitHub Actions workflow:
Runs once per day at 03:00
Executes filter.py
Checks whether calendar.ics changed
Commits only when necessary
Publishes the updated file via GitHub Pages
You can also trigger it manually via:
Actions → Update Calendar → Run workflow

## 🌐 Public ICS Feed URL
Once GitHub Pages is enabled (Settings → Pages → Deploy from branch → main → /), your calendar feed is available at:

```
https://<your-username>.github.io/westie-calendar-filtered/calendar.ics
```
For example:

```
https://styrkar.github.io/westie-calendar-filtered/calendar.ics
```
This URL can be subscribed to in Outlook:
**Outlook.com → Calendar → Add calendar → Subscribe from web**

## 🧪 Testing
You can test the workflow manually:
 1 Go to **Actions**
 2 Select **Update Calendar**
 3 Click **Run workflow**

Check whether:
- *calendar.ics* updates correctly
- The workflow logs show “No changes — skipping commit” when appropriate
- GitHub Pages serves the updated file

## 🛠️ Troubleshooting
### ❌ No *calendar.ics* generated
Check the workflow logs under the python filter.py step.

### ❌ Workflow cannot push
Ensure repository settings allow write access:
**Settings → Actions → General → Workflow permissions → Read and write**

### ❌ Outlook rejects the feed
Make sure the ICS file is accessible via GitHub Pages.

❌ Outlook rejects the feed
Make sure the ICS file is accessible via GitHub Pages.
