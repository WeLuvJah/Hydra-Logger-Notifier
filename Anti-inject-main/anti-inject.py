import os
from os import name, system, getenv
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
import time
import shutil
import ctypes
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

class WatchDogEvent (LoggingEventHandler):
    def on_modified(self, event):
        ctypes.windll.user32.MessageBoxW(0, "Injection detected!", "Hydra [ANTI-INJECT]", 1)
        indexrestor()
        time.sleep(1)
        main()

def indexrestor():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': local + '\Discord',
        'Discord Canary': local + '\discordcanary',
        'Discord PTB': local + '\discordptb',
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        path += '\\app-1.0.9003\modules\discord_desktop_core-1\discord_desktop_core' # I would make the program find the version of discord on its own later :)
        time.sleep(1)
        with open(f"{path}\index.txt", "w", encoding="utf8") as f:
            f.write("module.exports = require('./core.asar');")
        os.remove(f"{path}\index.js")
        os.rename(f"{path}\index.txt", f"{path}\index.js")
        time.sleep(1)
        ctypes.windll.user32.MessageBoxW(0, "Restoration of index.js file finished! \nPlease change your Discord password anyway to reset your token.", "Hydra [ANTI-INJECT]", 1)

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': local + '\Discord',
        'Discord Canary': local + '\discordcanary',
        'Discord PTB': local + '\discordptb',
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        path += '\\app-1.0.9003\modules\discord_desktop_core-1\discord_desktop_core'
        observer = Observer()
        observer.schedule(WatchDogEvent(), path, recursive=True)
        print("[i] Your Discord is under surveillance by Hydra.")
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

def settings():
    startup = input("[>] Do you want the program to start at startup? (true/false)")
    if startup == "true":
        roaming = os.getenv('APPDATA')
        filePath = shutil.copy('anti-inject.py', f'{roaming}/Microsoft/Windows/Start Menu/Programs/Startup')
        main()
    else:
        main()

banner = """
 ______________
|[]            |
|  __________  |
|  | Hydra  |  |
|  | Press  |  |
|  | Enter  |  |
|  |________|  |
|   ________   |
|   [ [ ]  ]   |
\___[_[_]__]___|
"""[1:]

Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, enter=True)
settings()
