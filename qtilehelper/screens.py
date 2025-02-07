import datetime
import os
from subprocess import check_output


def getNumberOfConnectedScreens():
    output = [
        screen for screen in check_output(["xrandr"]).decode("utf-8").splitlines()
    ]
    return len(
        [
            screen_line.split()[0]
            for screen_line in output
            if " connected " in screen_line
        ]
    )


def setWallpaper():
    path = "/home/jasonmishi/Personal/Pictures/wallpaper/"
    wallpapers = os.listdir(path)
    day = int(datetime.datetime.now().timestamp()) // 86400
    wallpaper1_path = path + wallpapers[day % len(wallpapers)]
    if getNumberOfConnectedScreens() == 2:
        wallpaper2_path = path + wallpapers[(day % len(wallpapers)) - 1]
        os.system("feh --bg-max " + wallpaper1_path + " " + wallpaper2_path)
    else:
        os.system("feh --bg-max " + wallpaper1_path)
