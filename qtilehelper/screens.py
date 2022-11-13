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
        if secondaryMonitor.get_height_mm() == 230 and secondaryMonitor.get_width_mm() == 300:
            os.system(
                f"xrandr --output {secondaryMonitor.get_model()} --mode 1280x960 --right-of {primaryMonitor.get_model()}"
            )
        # TODO: check if you can use EDID to uniquely identify monitors
        ''' 
        Samsung SyncMaster EDID (Not sure if EDID comes from monitor or HDMI to VGA)
        00ffffffffffff0004ef010031304e43
		2d170103a01e1761eae4de9e544a9723
		1c4c5400080081808140810001019500
		01010101010164190040410026301888
		360000c010000018023a801871382d40
		582c4500dd0c1100001e662150b05100
		1b304070360032313400001e000000fa
		00819981c081fc01010101950f0a013c
		02031b61230907078301000067030c00
		2000802d43908402e2000f8c0ad08a20
		e02d10103e9600a05a00000000000000
		00000000000000000000000000000000
		00000000000000000000000000000000
		00000000000000000000000000000000
		00000000000000000000000000000000
		00000000000000000000000000000029

        Acer B193 EDID
        00ffffffffffff003873752200000000
        011c0103a01e1764eae4de9e544a9723
        1c4c5400080081808140810001019500
        01010101010164190040410026301888
        360000c010000018023a801871382d40
        582c4500dd0c1100001e662150b05100
        1b304070360032313400001e000000fa
        00819981c081fc01010101950f0a0104
        02031b61439084022309070783010000
        67030c0020008028e2000f8c0ad08a20
        e02d10103e9600a05a00000000000000
        00000000000000000000000000000000
        00000000000000000000000000000000
        00000000000000000000000000000000
        00000000000000000000000000000000
        0000000000000000000000000000002e
        '''

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
