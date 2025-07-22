import os
import shutil
import sys
import platform
import datetime


# Sprachunterstützung
LANGUAGES = {
    "de": {
        "slogan": "FiveM Cleaner",
        "desc": "Dieses Tool löscht den FiveM-Cache auf deinem Windows-System.",
        "menu": [
            "[1] FiveM Cache löschen (mit Sicherung)",
            "[2] FiveM Cache sichern (Backup in Downloads)",
            "[3] Speicherplatz der Cache-Ordner anzeigen",
            "[4] Nur bestimmten Cache-Ordner löschen",
            "[5] Letzte Aktionen anzeigen",
            "[6] Cache- oder Backup-Ordner öffnen",
            "[7] Logdatei anzeigen oder löschen",
            "[8] Pfade konfigurieren",
            "[9] Sprache wechseln (Deutsch/Englisch)",
            "[0] Beenden",
        ],
        "select": "Bitte Auswahl eingeben: ",
        "backup_before_delete": "Vor dem Löschen ein Backup erstellen? (j/n): ",
        "last_deleted": "Letzter Löschvorgang:",
        "last_backup": "Letztes Backup:",
        "open_which": "Welchen Ordner öffnen? [1] Cache [2] Backup: ",
        "open_fail": "Öffnen des Ordners fehlgeschlagen.",
        "log_options": "[1] Log anzeigen  [2] Log löschen  [0] Zurück",
        "log_deleted": "Logdatei gelöscht.",
        "path_config": "Aktuelle Pfade anzeigen und ändern:",
        "enter_new_path": "Neuen Pfad eingeben (oder leer lassen für Standard): ",
        "admin_hint": "Hinweis: Für manche Aktionen sind Administratorrechte nötig!",
        "update_check": "Nach Updates suchen ... (Demo)",
        "deleted": "Gelöscht:",
        "notfound": "Nicht gefunden:",
        "done": "FiveM Cache wurde gelöscht.",
        "backupdone": "Backup abgeschlossen im Ordner:",
        "backupcreated": "Backup erstellt:",
        "backupfail": "Fehler beim Backup von",
        "deletefail": "Fehler beim Löschen von",
        "backupnotfound": "Nicht gefunden (kein Backup):",
        "size": "MB",
        "exit": "Beendet.",
        "invalid": "Ungültige Eingabe. Bitte eine gültige Option wählen.",
        "choosefolder": "Welchen Cache-Ordner löschen?",
        "folders": ["[1] cache", "[2] server-cache", "[3] server-cache-priv"],
        "log": "Logdatei gespeichert unter:",
    },
    "en": {
        "slogan": "FiveM Cleaner",
        "desc": "This tool deletes the FiveM cache on your Windows system.",
        "menu": [
            "[1] Delete all FiveM cache",
            "[2] Backup FiveM cache (to Downloads)",
            "[3] Show cache folder size",
            "[4] Delete only a specific cache folder",
            "[5] Switch language (Deutsch/English)",
            "[0] Exit",
        ],
        "select": "Please enter your choice: ",
        "deleted": "Deleted:",
        "notfound": "Not found:",
        "done": "FiveM cache deleted.",
        "backupdone": "Backup completed in folder:",
        "backupcreated": "Backup created:",
        "backupfail": "Error backing up",
        "deletefail": "Error deleting",
        "backupnotfound": "Not found (no backup):",
        "size": "MB",
        "exit": "Exited.",
        "invalid": "Invalid input. Please select a valid option.",
        "choosefolder": "Which cache folder to delete?",
        "folders": ["[1] cache", "[2] server-cache", "[3] server-cache-priv"],
        "log": "Log file saved at:",
    },
}


LANG = "de"
ENABLE_LOG = False

CACHE_PATHS = [
    os.path.expandvars(r"%LOCALAPPDATA%\FiveM\FiveM.app\data\cache"),
    os.path.expandvars(r"%LOCALAPPDATA%\FiveM\FiveM.app\data\server-cache"),
    os.path.expandvars(r"%LOCALAPPDATA%\FiveM\FiveM.app\data\server-cache-priv"),
]

LOGFILE = os.path.join(os.path.expanduser("~"), "Downloads", "fivem_cache_cleaner.log")
LAST_ACTION_FILE = os.path.join(
    os.path.expanduser("~"), "Downloads", "fivem_cache_cleaner_last.json"
)


def log_action(msg):
    if ENABLE_LOG:
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n"
            )


def save_last_action(action, path=None):
    import json

    data = {"action": action, "path": path, "time": datetime.datetime.now().isoformat()}
    with open(LAST_ACTION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)


def show_last_actions():
    import json

    if os.path.exists(LAST_ACTION_FILE):
        with open(LAST_ACTION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(
            f"{LANGUAGES[LANG]['last_deleted']} {data.get('time','-')} ({data.get('action','-')})"
        )
    else:
        print("Keine Aktionen gespeichert.")


def open_folder(which):
    try:
        if which == 1:
            folder = CACHE_PATHS[0]
        else:
            folder = os.path.join(
                os.path.expanduser("~"), "Downloads", "FiveM_Cache_Backup"
            )
        if not os.path.exists(folder):
            print(LANGUAGES[LANG]["notfound"], folder)
            return
        sysname = platform.system()
        if sysname == "Windows":
            import subprocess

            subprocess.Popen(["start", "", folder], shell=True)
        elif sysname == "Darwin":
            os.system(f'open "{folder}"')
        else:
            os.system(f'xdg-open "{folder}"')
    except Exception as e:
        print(LANGUAGES[LANG]["open_fail"], str(e))


def log_file_options():
    print(LANGUAGES[LANG]["log_options"])
    opt = input("").strip()
    if opt == "1":
        if os.path.exists(LOGFILE):
            try:
                with open(LOGFILE, "r", encoding="utf-8") as f:
                    print(f.read())
            except Exception as e:
                print("Fehler beim Lesen der Logdatei:", str(e))
        else:
            print("Keine Logdatei vorhanden.")
    elif opt == "2":
        if os.path.exists(LOGFILE):
            try:
                os.remove(LOGFILE)
                print(LANGUAGES[LANG]["log_deleted"])
            except Exception as e:
                print("Fehler beim Löschen der Logdatei:", str(e))
        else:
            print("Keine Logdatei vorhanden.")
    else:
        return


def configure_paths():
    print(LANGUAGES[LANG]["path_config"])
    for i, p in enumerate(CACHE_PATHS):
        print(f"[{i+1}] {p}")
    idx = input("Nummer zum Ändern eingeben (oder Enter für Abbruch): ").strip()
    if idx.isdigit() and 1 <= int(idx) <= len(CACHE_PATHS):
        newp = input(LANGUAGES[LANG]["enter_new_path"]).strip()
        if newp:
            if os.path.isabs(newp):
                CACHE_PATHS[int(idx) - 1] = newp
                print("Pfad geändert.")
            else:
                print("Ungültiger Pfad. Bitte absoluten Pfad angeben.")
        else:
            print("Pfad nicht geändert.")
    else:
        print("Abbruch oder ungültige Eingabe.")


def delete_cache():
    # Automatische Sicherung vor Löschen
    backup = input(LANGUAGES[LANG]["backup_before_delete"])
    if backup.lower() == "j" or backup.lower() == "y":
        backup_cache()
        save_last_action("backup")
    for path in CACHE_PATHS:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"{LANGUAGES[LANG]['deleted']} {path}")
                log_action(f"{LANGUAGES[LANG]['deleted']} {path}")
            except Exception as e:
                print(f"{LANGUAGES[LANG]['deletefail']} {path}: {e}")
                log_action(f"{LANGUAGES[LANG]['deletefail']} {path}: {e}")
        else:
            print(f"{LANGUAGES[LANG]['notfound']} {path}")
            log_action(f"{LANGUAGES[LANG]['notfound']} {path}")
    print(LANGUAGES[LANG]["done"])
    log_action(LANGUAGES[LANG]["done"])
    save_last_action("delete")


def backup_cache():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    backup_dir = os.path.join(downloads, "FiveM_Cache_Backup")
    os.makedirs(backup_dir, exist_ok=True)
    for path in CACHE_PATHS:
        if os.path.exists(path):
            dest = os.path.join(backup_dir, os.path.basename(path))
            try:
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(path, dest)
                print(f"{LANGUAGES[LANG]['backupcreated']} {dest}")
                log_action(f"{LANGUAGES[LANG]['backupcreated']} {dest}")
            except Exception as e:
                print(f"{LANGUAGES[LANG]['backupfail']} {path}: {e}")
                log_action(f"{LANGUAGES[LANG]['backupfail']} {path}: {e}")
        else:
            print(f"{LANGUAGES[LANG]['backupnotfound']} {path}")
            log_action(f"{LANGUAGES[LANG]['backupnotfound']} {path}")
    print(f"{LANGUAGES[LANG]['backupdone']} {backup_dir}")
    log_action(f"{LANGUAGES[LANG]['backupdone']} {backup_dir}")
    print(f"{LANGUAGES[LANG]['log']} {LOGFILE}")
    save_last_action("backup")


def show_cache_size():
    def get_size(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total

    for path in CACHE_PATHS:
        if os.path.exists(path):
            size = get_size(path)
            mb = size / (1024 * 1024)
            print(f"{path}: {mb:.2f} {LANGUAGES[LANG]['size']}")
            log_action(f"{path}: {mb:.2f} {LANGUAGES[LANG]['size']}")
        else:
            print(f"{LANGUAGES[LANG]['notfound']} {path}")
            log_action(f"{LANGUAGES[LANG]['notfound']} {path}")


def main():
    global LANG, ENABLE_LOG
    if platform.system() != "Windows":
        print(
            "Warnung: Dieses Tool ist für Windows ausgelegt. Einige Funktionen funktionieren auf diesem System möglicherweise nicht korrekt."
        )
    while True:
        print("=" * 40)
        print(f"{LANGUAGES[LANG]['slogan']}")
        print("=" * 40)
        print(LANGUAGES[LANG]["desc"])
        print(LANGUAGES[LANG]["admin_hint"])
        print(f"[L] Logging {'aktiviert' if ENABLE_LOG else 'deaktiviert'}")
        for line in LANGUAGES[LANG]["menu"]:
            print(line)
        choice = input(f"\n{LANGUAGES[LANG]['select']}").strip().lower()
        if choice == "1":
            delete_cache()
        elif choice == "2":
            backup_cache()
        elif choice == "3":
            show_cache_size()
        elif choice == "4":
            print("\n" + LANGUAGES[LANG]["choosefolder"])
            for idx, folder in enumerate(LANGUAGES[LANG]["folders"]):
                print(folder)
            sub = input(f"{LANGUAGES[LANG]['select']}")
            try:
                idx = int(sub) - 1
                if 0 <= idx < len(CACHE_PATHS):
                    path = CACHE_PATHS[idx]
                    if os.path.exists(path):
                        backup = input(LANGUAGES[LANG]["backup_before_delete"])
                        if backup.lower() == "j" or backup.lower() == "y":
                            backup_cache()
                            save_last_action("backup", path)
                        try:
                            shutil.rmtree(path)
                            print(f"{LANGUAGES[LANG]['deleted']} {path}")
                            log_action(f"{LANGUAGES[LANG]['deleted']} {path}")
                        except Exception as e:
                            print(f"{LANGUAGES[LANG]['deletefail']} {path}: {e}")
                            log_action(f"{LANGUAGES[LANG]['deletefail']} {path}: {e}")
                        save_last_action("delete", path)
                    else:
                        print(f"{LANGUAGES[LANG]['notfound']} {path}")
                        log_action(f"{LANGUAGES[LANG]['notfound']} {path}")
                else:
                    print(LANGUAGES[LANG]["invalid"])
            except ValueError:
                print(LANGUAGES[LANG]["invalid"])
        elif choice == "5":
            show_last_actions()
        elif choice == "6":
            which = input(LANGUAGES[LANG]["open_which"])
            if which == "1":
                open_folder(1)
            elif which == "2":
                open_folder(2)
        elif choice == "7":
            log_file_options()
        elif choice == "8":
            configure_paths()
        elif choice == "9":
            LANG = "en" if LANG == "de" else "de"
            print(f"Sprache gewechselt zu: {'Englisch' if LANG == 'en' else 'Deutsch'}")
        elif choice == "l":
            ENABLE_LOG = not ENABLE_LOG
            print(f"Logging {'aktiviert' if ENABLE_LOG else 'deaktiviert'}.")
        elif choice == "0":
            print(LANGUAGES[LANG]["exit"])
            log_action(LANGUAGES[LANG]["exit"])
            print(f"{LANGUAGES[LANG]['log']} {LOGFILE}")
            sys.exit(0)
        else:
            print(LANGUAGES[LANG]["invalid"])


# Vorschläge für weitere Funktionen:
# - Automatische Sicherung des Cache-Ordners vor dem Löschen
# - Anzeige des belegten Speicherplatzes der Cache-Ordner
# - Option, nur bestimmte Cache-Typen zu löschen (z.B. nur server-cache)
# - Protokollierung der Löschvorgänge in einer Logdatei
# - Mehrsprachige Benutzeroberfläche (Deutsch/Englisch)
# - Option, das FiveM-Programm nach dem Löschen automatisch zu starten


if __name__ == "__main__":
    main()
