import os
import datetime
import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk


def getNumberOfConnectedScreens():
    return Gdk.Display.get_default().get_n_monitors();

def setupScreens():
    numberOfScreens = getNumberOfConnectedScreens()
    if numberOfScreens == 2:
        # set-up second monitor
        gdkdsp = Gdk.Display.get_default()
        primaryMonitor = gdkdsp.get_monitor(0)
        secondaryMonitor = gdkdsp.get_monitor(1)
        if monitor.get_height_mm() == 230 and monitor.get_width_mm() == 300:
            os.system(
                f"xrandr --output {secondaryMonitor.get_model()} --mode 1280x960 --right-of {primaryMonitor.get_model()}"
            )

def setWallpaper():
    path = '/home/jason/Personal/Pictures/wallpaper/'
    wallpapers = os.listdir(path)
    day = int(datetime.datetime.now().timestamp())//86400
    wallpaper1_path = path + wallpapers[day%len(wallpapers)]
    if getNumberOfConnectedScreens() == 2:
        wallpaper2_path = path + wallpapers[(day%len(wallpapers)) - 1]
        os.system('feh --bg-max ' + wallpaper1_path + ' ' + wallpaper2_path)
    else:
        os.system('feh --bg-max ' + wallpaper1_path)
