#!/usr/bin/env python

"""
Interaction with Mac os.

Current options: set the wallpaper.
"""

from appscript import *

def set_wallpaper_image(imgs, mode='stretched'):
    """Set the given file as wallpaper."""
    if not len(imgs):
        return

    default_image = imgs[0]

    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for i, d in enumerate(desktops):
        desk = se.desktops[its.display_name == d]
        img = imgs[i] if len(imgs) > i else default_image
        desk.picture.set(mactypes.File(img))

def get_no_of_monitors():
    return len(app('System Events').desktops.display_name.get())
