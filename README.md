# JokusHook

Dieses Repository enthält Skripte, um mit Hilfe von Python und der JokeAPI Witze zu generieren und diese über apprise zu versenden.
Durch die Verwendung von apprise können die Benachrichtigungsdienste sehr einfach erweitert werden.

## Installation

1. Installiere die Anforderungen mit `pip install -r requirements.txt`.

2. Erstelle eine `.env` Datei im Hauptverzeichnis des Repository und füge deine Zugangsdaten hinzu:

Discord Webhook:

```
DISCORD_ID="1234"
DISCORD_TOKEN="ab31c647dhfataw412e"
```

und / oder

Nextcloud Talk:

```
NEXTCLOUDTALK_USER = "NeuerUser"
NEXTCLOUDTALK_PASS = "AppPassword"
NEXTCLOUDTALK_HOST = "nc.dieschoenewolke.com"
NEXTCLOUD_ROOM1 = "1abc2345"
```

## Verwendung

Führe das Python-Skript aus, um einen Jokus zu versenden.

Discord Webhook:

```
python /Notifications/Discord/jokus.py
```

Nextcloud Talk:

```
python /Notifications/NextcloudTalk/jokus.py
```

## Quellen

https://github.com/caronc/apprise

https://github.com/Sv443/JokeAPI

https://github.com/leet-hakker/JokeAPI-Python

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
