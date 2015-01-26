#!/usr/bin/env python

"""
Project configuration.
Override it in local_config.py
"""

import sys
import os

# Base dir. Set it in ABSOLUTE path. No slash at the end.
# Images will be saved here.
BASE_DIR = ''

# WGET CONF
# number of times for wget to retry
WGET_RET = 1
# timeout
WGET_TIMEOUT=30

#the same image on multiple monitors?
SINGLE_WALLPAPER = False

# types of websites
REDDIT_COM = 0
FOUR_WALLED_ORG = 1     # 4walled.org

# Wallbase info
# -------------
#
# See http://wallbase.cc/tags for a list of tags. If you click on 'Star Wars'
# for instance, you'll be redirected to http://wallbase.cc/tags/info/7964.
# This is what you should add to the list below. To the ID, I suggest adding
# the 'wb_' prefix to differentiate it from subreddits.

# expand the list if you want
WALLPAPER_PAGES = {
    ### add subreddits below:
    0 : {'id': 'ArchPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/ArchitecturePorn'},
    1 : {'id': 'CityPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/CityPorn'},
    2 : {'id': 'EarthPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/EarthPorn'},
    3 : {'id': 'InfraPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/InfrastructurePorn'},

    4 : {'id': 'backart',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/BackgroundArt'},
    5 : {'id': 'gameworlds',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/gameworlds'},
    6 : {'id': 'imglands',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/ImaginaryLandscapes'},
    7 : {'id': 'imgmonst',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/ImaginaryMonsters'},
    8 : {'id': 'imgtech',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/ImaginaryTechnology'},
   ### add 4walled pages below:
#   15 : {'id': '4w_Linux',       'type': FOUR_WALLED_ORG, 'url': get_4walled_url(tag='linux', sfw=True)},
}

# Your choice. Example: 0, which means EarthPorn.
CURRENT_CHOICE = 0
# The downloader can grab images from _several_ sites too. Precise their keys here _in a list_.
# This list should contain at least one element, the CURRENT_CHOICE.
MULTIPLE_CHOICE = WALLPAPER_PAGES.keys()    # all of them

# this is for wallpaper_rotator.py
# images will be chosen from this (or these) category(s)
# it's a _list_
ROTATOR_CHOICE = WALLPAPER_PAGES.keys()    # all of them
# image size should have at least that many pixels:
SIZE_THRESHOLD = (900, 600)
# accept image if smaller than threshold by this percentage:
SIZE_TOLERANCE_PERCENTAGE = 5.0
# ratio must be in this interval:
RATIO_INTERVAL = (1.0, 2.1)
# Should large images be resized?
RESIZE_LARGE_IMAGES = True
# Here you can specify the width of your screen in pixels.
# Too large images will be resized to this width.
MAX_WIDTH = 1920
# how long to set wallpaper for in seconds
DURATION = '600.0'

#OVERRIDE your settings in local_config.py
try:
    from local_config import *
except ImportError as e:
    pass


def get_curr_photo_dir():
    """Get the current photo dir.
    
    It must be here to be visible."""
    return os.path.join(BASE_DIR, WALLPAPER_PAGES[CURRENT_CHOICE]['id'])

def get_photo_dir_by_key(key):
    """Get the photo dir. of the given key."""
    return os.path.join(BASE_DIR, WALLPAPER_PAGES[key]['id'])

def get_4walled_url(tag, sfw):
    # at 4walled.org sfw=0 means you want sfw images
    template = 'http://4walled.org/search.php?tags={tag}&board=&width_aspect=&searchstyle=larger&sfw={sfw}&search=search'
    return template.format(tag=tag, sfw = '0' if sfw else '')

##############################################################################
## change these variables if you want
##############################################################################
# Where to save the images. Example: /trash/gnome-wallpapers/EarthPorn
PHOTO_DIR = get_curr_photo_dir()
# SQLite database will be stored here:
SQLITE_DB = os.path.join(BASE_DIR, '.database', 'wallpapers.sqlite')

def get_current_site_record():
    """Get the chosen record as a dictionary."""
    return WALLPAPER_PAGES[CURRENT_CHOICE]


def set_current_choice(choice):
    """Set the current choice. Update photo dir. too."""
    global CURRENT_CHOICE, PHOTO_DIR
    
    CURRENT_CHOICE = choice
    PHOTO_DIR = get_curr_photo_dir()
    
def self_verify():
    """Let's do some verifications to be sure that everythign was set correctly."""
    global BASE_DIR, MULTIPLE_CHOICE, ROTATOR_CHOICE
    
    if not BASE_DIR: 
        print >>sys.stderr, "Error: you need to set BASE_DIR"
        sys.exit(2)

    BASE_DIR = os.path.normpath(BASE_DIR)
        
    if CURRENT_CHOICE not in WALLPAPER_PAGES.keys():
        print >>sys.stderr, "Error: your CURRENT_CHOICE in the config file is invalid."
        sys.exit(2)
        
    if CURRENT_CHOICE not in MULTIPLE_CHOICE:
        print >>sys.stderr, "Error: CURRENT_CHOICE must be included in MULTIPLE_CHOICE."
        sys.exit(2)
         
    MULTIPLE_CHOICE = sorted(list(set(MULTIPLE_CHOICE)))    # remove duplicates
    for e in MULTIPLE_CHOICE:
        if e not in WALLPAPER_PAGES.keys():
            print >>sys.stderr, "Error: MULTIPLE_CHOICE contains an invalid entry."
            sys.exit(2)

    if len(ROTATOR_CHOICE) == 0:
        print >>sys.stderr, "Error: ROTATOR_CHOICE cannot be empty."
        sys.exit(2)
        
    ROTATOR_CHOICE = list(set(ROTATOR_CHOICE))    # remove duplicates
    for e in ROTATOR_CHOICE:
        if e not in WALLPAPER_PAGES.keys():
            print >>sys.stderr, "Error: ROTATOR_CHOICE contains an invalid entry."
            sys.exit(2)
