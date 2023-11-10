# JokusHook

Dieses Repository enthält ein Script um mittles Python mit der JokeAPI Witze zu generieren und diese dann mittels apprise zu versenden.
Durch die Nutzung von apprise lassen sich die Benachrichtigungsdienste sehr leicht erweitern.

## Installation

1. Installiere die Anforderungen mit `pip install -r requirements.txt`.

2. Erstelle eine `.env` Datei im Hauptverzeichnis des Repository und füge deine Zugangsdaten hinzu:

Beispiel Discord:
```
DISCORD_ID="1234"
DISCORD_TOKEN="ab31c647dhfataw412e"
```

## Verwendung

Führe das Python-Skript aus, um einen Jokus zu versenden.

Beispiel Discord:
```
python /Notifications/Discord/jokus.py
```

## Quellen

https://github.com/caronc/apprise
https://github.com/Sv443/JokeAPI
https://github.com/leet-hakker/JokeAPI-Python


## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.