Wallpaper Downloader and Rotator for Gnome
==========================================

* Authors:
    - Laszlo Szathmary (<jabba.laci@gmail.com>)
    - iwakun (<http://www.reddit.com/user/iwakun>)
* Date:      April, 2011
* Last mod.: May, 2011
* Version:   0.3.6
* Website:   <https://ubuntuincident.wordpress.com/2011/04/06/wallpaper-downloader-and-rotator-for-gnome/>
* GitHub:    <https://github.com/jabbalaci/Wallpaper-Downloader-and-Rotator-for-Gnome>

This free software is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user iwakun.
See the `original_by_iwakun/` folder for more information.)

The goal of the script is to download images from a reddit category and 
create an XML file that can be set as background in Gnome. The XML file
will rotate the images.

Here is the list of changes that I added to the original version:

* You can choose from several reddit categories. You can also 
  specify your favorite category.
* Screen scraping is done with the BeautifulSoup library.
* The most important change is the filtering of images that are
  unsuitable as wallpapers, i.e. small images, portrait images, and
  images with strange ratio are removed from the list.
* XML writing is done with the lxml library.
* Support for Flickr images (zioyero's patch).
* The URLs of the downloaded images are strored in an SQLite database.
  This way an already fetched image (either good or bad) won't be downloaded again.
* The script can set the produced XML as your wallpaper, you don't need to
  do that manually. Also, XML production can be switched off if you want to
  use a different wallpaper manager.

For installing lxml, please refer to [this entry][1], where the 
installation procedure is explained at the end of the post.

[1]: https://pythonadventures.wordpress.com/2011/04/04/write-xml-to-file/


Usage:
------

First, you might want to customize some settings in the `config.py` file.
The most important thing is the `PHOTO_DIR` directory, i.e. where to store
the downloaded images. Create this directory if it doesn't exist.
Then, simply launch the script:

    ./wallpapers.py
    
You can also add it to your crontab:

    $ crontab -e
    10 */2 * * * /absolute_path_to/wallpapers.py
    
Add the second line to the end of the crontab list. Here the script is 
called at every two hours (at 0h10, 2h10, etc.).

**New:**

I changed the default behaviour of the script. By default it doesn't
generate an XML output. I find it a better solution to use a dedicated
wallpaper manager for this task (see below for a list of alternatives).
Rotating the images with an XML is not very flexible, a wallpaper manager
can provide a better experience.
If you still want the XML, set it in the config file.


Contributors:
-------------

* Nathan B, alias [ndbroadbent][2]
* Adrian Castillejos, alias [zioyero][3]

[2]: https://github.com/ndbroadbent
[3]: https://github.com/zioyero


Managing the downloaded wallpapers:
-----------------------------------

There are several ways to manage the downloaded images:

1. The easiest way is to let this job done by the script. By default,
   it produces an XML file and sets it as your wallpaper. See the
   config file if you want to do some customizations.
2. You can also use a wallpaper manager. I suggest wally, it worked
   very well for me. See [this post][4] for more information on how to 
   install and make it work under Unity.
   
   Nathan B, alias ndbroadbent suggests Cortina. Here is what he has to say 
   about it:

> I'd just like to mention that I found the 'Cortina' application, and it blows away Gnome's wallpaper rotater.
> It monitors an image directory and changes your wallpapers after a desired interval, but also:
> 
> * Can be set to change wallpapers in a random order
> * Puts an icon in the system tray
>     * Left-click: immediately change the wallpaper
>     * Right-click  => Current Wallpaper => remove from disk
> 
> You can install it from a custom PPA with this command:
> 
>     sudo add-apt-repository ppa:cs-sniffer/cortina && sudo apt-get update && sudo apt-get install cortina

I couldn't install Cortina under Ubuntu 11.04 but it might work with older systems.
Note that wally can do similar things too.

[4]: https://ubuntuincident.wordpress.com/2011/01/10/wallpaper-changer/


TODO:
-----

Add support to more wallpaper sites:

* <http://wallbase.cc>
* <http://4walled.org/>
