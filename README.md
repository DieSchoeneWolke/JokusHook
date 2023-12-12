# JokusHook

This repository contains Python scripts to automatically fetch jokes ('Jokus') via the JokeAPI and send them via apprise.

The notification services can be easily extended by using apprise.


## Installation

1. Install the requirements with `pip install -r requirements.txt`.

2. Create an `.env` file in the root directory and attach your credentials:


#### Discord Webhook:

```
DISCORD_ID = "1234"
DISCORD_TOKEN = "ab31c647dhfataw412e"
```


#### Nextcloud Talk:

```
NEXTCLOUDTALK_USER = "NeuerUser"
NEXTCLOUDTALK_PASS = "AppPassword"
NEXTCLOUDTALK_HOST = "nc.dieschoenewolke.com"
NEXTCLOUD_ROOM1 = "1abc2345"
```


## Usage

Run the python script to send a Jokus.


#### Discord Webhook:


```
python /Notifications/Discord/jokus.py
```


#### Nextcloud Talk:

```
python /Notifications/NextcloudTalk/jokus.py
```


## Sources

https://github.com/caronc/apprise

https://github.com/Sv443/JokeAPI

https://github.com/leet-hakker/JokeAPI-Python


## License

This project is licensed under the GNU General Public License, Version 3.0 (GPL-3.0).


## 3rd Party Components

Some components of this project contains 3rd party elements that are licensed under the BSD 2-Clause License.

- `apprise`


<details>
  <summary> 🇩🇪 Translation</summary>
  
# JokusHook

Dieses Repository enthält Skripte, um mit Hilfe von Python und der JokeAPI Witze ("Jokus") zu generieren und diese über apprise zu versenden.

Durch die Verwendung von apprise können die Benachrichtigungsdienste sehr einfach erweitert werden.


## Installation

1. Installiere die Anforderungen mit `pip install -r requirements.txt`.

2. Erstelle eine `.env` Datei im Hauptverzeichnis des Repository und füge deine Zugangsdaten hinzu:


#### Discord Webhook:

```
DISCORD_ID = "1234"
DISCORD_TOKEN = "ab31c647dhfataw412e"
```


#### Nextcloud Talk:

```
NEXTCLOUDTALK_USER = "NeuerUser"
NEXTCLOUDTALK_PASS = "AppPassword"
NEXTCLOUDTALK_HOST = "nc.dieschoenewolke.com"
NEXTCLOUD_ROOM1 = "1abc2345"
```


## Verwendung

Führe das Python-Skript aus, um einen Jokus zu versenden.


#### Discord Webhook:


```
python /Notifications/Discord/jokus.py
```


#### Nextcloud Talk:

```
python /Notifications/NextcloudTalk/jokus.py
```


## Quellen

https://github.com/caronc/apprise

https://github.com/Sv443/JokeAPI

https://github.com/leet-hakker/JokeAPI-Python


## Lizenz

Dieses Projekt ist unter der GNU General Public License, Version 3.0 (GPL-3.0) lizenziert.


## Komponente von Drittanbietern

Einige Teile dieses Projekts stammen von oder enthalten Komponenten, die unter der BSD 2-Clause License lizenziert sind.

- `apprise`

</details>
