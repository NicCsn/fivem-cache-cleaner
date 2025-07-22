# FiveM Cache Cleaner

Ein vielseitiges Python-Tool zum Löschen und Sichern des FiveM-Caches unter Windows (und eingeschränkt macOS/Linux). Das Tool bietet ein interaktives Konsolenmenü mit vielen Optionen.

## Voraussetzungen

- Python 3.8 oder neuer
- Windows empfohlen (macOS/Linux eingeschränkt)

## Installation & Start

1. Lade die Datei `fivem_cache_cleaner.py` herunter.
2. Öffne ein Terminal im Download-Ordner.
3. Starte das Tool mit:

   ```
   python fivem_cache_cleaner.py
   ```

## Menü-Optionen & Hinweise

**[1] FiveM Cache löschen (mit Sicherung)**

- Löscht alle relevanten Cache-Ordner.
- Vor dem Löschen wirst du gefragt, ob ein Backup erstellt werden soll.
- Tipp: Aktiviere Logging mit Taste `L`, um alle Aktionen zu protokollieren.

**[2] FiveM Cache sichern (Backup in Downloads)**

- Erstellt ein Backup aller Cache-Ordner im Ordner `Downloads/FiveM_Cache_Backup`.

**[3] Speicherplatz der Cache-Ordner anzeigen**

- Zeigt die Größe aller relevanten Cache-Ordner an.

**[4] Nur bestimmten Cache-Ordner löschen**

- Wähle gezielt einen der drei Cache-Ordner aus.
- Auch hier kannst du vorab ein Backup machen.

**[5] Letzte Aktionen anzeigen**

- Zeigt an, wann zuletzt gelöscht oder gesichert wurde.

**[6] Cache- oder Backup-Ordner öffnen**

- Öffnet den jeweiligen Ordner im Explorer/Finder.

**[7] Logdatei anzeigen oder löschen**

- Zeigt die Logdatei an oder löscht sie (nur wenn Logging aktiviert war).

**[8] Pfade konfigurieren**

- Passe die Pfade der Cache-Ordner an (z.B. bei abweichender Installation).

**[9] Sprache wechseln (Deutsch/Englisch)**

- Schaltet das gesamte Menü und alle Texte um.

**[L] Logging aktivieren/deaktivieren**

- Schaltet die Protokollierung aller Aktionen ein/aus.

**[0] Beenden**

- Beendet das Programm.

## Hinweise

- Für manche Aktionen sind Administratorrechte nötig (z.B. Löschen von Systemordnern).
- Das Tool funktioniert am besten unter Windows.
- Die Logdatei und Backups werden im Downloads-Ordner des aktuellen Benutzers gespeichert.

## .exe erstellen (optional)

1. Installiere PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Erstelle die .exe:
   ```
   pyinstaller --onefile fivem_cache_cleaner.py
   ```
3. Die ausführbare Datei findest du im `dist`-Ordner.

## GitHub-Nutzung

- Lade das Skript und ggf. die .exe in ein GitHub-Repository hoch.
- Füge diese README.md hinzu.
- Nutzer können das Tool direkt herunterladen und nutzen.

---

**Fragen oder Probleme?**
Erstelle ein Issue im GitHub-Repository oder kontaktiere den Entwickler.

# FiveM Cache Cleaner

Dieses Python-Skript bietet ein Konsolenmenü, um den FiveM-Cache unter Windows zu löschen. Es zeigt beim Start einen Slogan und eine Beschreibung an. Nach Auswahl von "1" werden die relevanten Cache-Ordner im %LOCALAPPDATA%-Verzeichnis gelöscht.

## Nutzung

1. Stelle sicher, dass Python installiert ist.
2. Starte das Skript mit:

   ```
   python fivem_cache_cleaner.py
   ```

3. Folge den Anweisungen im Konsolenmenü.

## Hinweis

- Das Skript funktioniert nur unter Windows, da es auf das %LOCALAPPDATA%-Verzeichnis zugreift.
- Das Skript benötigt ggf. Administratorrechte, um alle Dateien löschen zu können.
