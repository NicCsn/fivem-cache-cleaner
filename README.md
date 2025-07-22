# FiveM Cache Cleaner

A versatile Python tool for deleting and backing up the FiveM cache on Windows (and limited support for macOS/Linux). The tool provides an interactive console menu with many options.

## Requirements

- Python 3.8 or newer
- Windows recommended (macOS/Linux limited support)

## Installation & Start

1. Download the file `fivem_cache_cleaner.py`.
2. Open a terminal in the download folder.
3. Start the tool with:

   ```
   python fivem_cache_cleaner.py
   ```

## Menu Options & Notes

**[1] Delete FiveM cache (with backup)**

- Deletes all relevant cache folders.
- You will be asked if you want to create a backup before deletion.
- Tip: Activate logging with key `L` to log all actions.

**[2] Backup FiveM cache (backup in Downloads)**

- Creates a backup of all cache folders in the `Downloads/FiveM_Cache_Backup` folder.

**[3] Show cache folder size**

- Shows the size of all relevant cache folders.

**[4] Delete only a specific cache folder**

- Select one of the three cache folders to delete.
- You can also create a backup beforehand here.

**[5] Show last actions**

- Shows when cache or backup was last deleted or created.

**[6] Open cache or backup folder**

- Opens the respective folder in Explorer/Finder.

**[7] Show or delete log file**

- Shows or deletes the log file (only if logging was enabled).

**[8] Configure paths**

- Adjust the paths of the cache folders (e.g. for custom installations).

**[9] Switch language (German/English)**

- Switches the entire menu and all texts.

**[L] Enable/disable logging**

- Turns logging of all actions on/off.

**[0] Exit**

- Exits the program.

## Notes

- Some actions may require administrator rights (e.g. deleting system folders).
- The tool works best on Windows.
- The log file and backups are saved in the current user's Downloads folder.

## Create .exe (optional)

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Create the .exe:
   ```
   pyinstaller --onefile fivem_cache_cleaner.py
   ```
3. The executable file can be found in the `dist` folder.

## GitHub Usage

- Upload the script and optionally the .exe to a GitHub repository.
- Add this README.md.
- Users can download and use the tool directly.

---

**Questions or problems?**
Create an issue in the GitHub repository or contact the developer.
