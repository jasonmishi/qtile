import datetime
import os

import gi

gi.require_version("Gdk", "3.0")
from gi.repository import Gdk  # noqa


def getNumberOfConnectedScreens():
    return Gdk.Display.get_default().get_n_monitors()


def setWallpaper():
    path = "/home/jason/Personal/Pictures/wallpaper/"
    wallpapers = os.listdir(path)
    day = int(datetime.datetime.now().timestamp()) // 86400
    wallpaper1_path = path + wallpapers[day % len(wallpapers)]
    if getNumberOfConnectedScreens() == 2:
        wallpaper2_path = path + wallpapers[(day % len(wallpapers)) - 1]
        os.system("feh --bg-max " + wallpaper1_path + " " + wallpaper2_path)
    else:
        os.system("feh --bg-max " + wallpaper1_path)
