#!/usr/bin/env python

"""
Interaction with Windows 7.
Copy paste for now as have no option to test
"""

import ctypes

def set_wallpaper_image(imgs, mode='stretched'):
    if not len(imgs):
        return

    default_image = imgs[0]
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, default_image , 3)
    
def get_no_of_monitors():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(80)
