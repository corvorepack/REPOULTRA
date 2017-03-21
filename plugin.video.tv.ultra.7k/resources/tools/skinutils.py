# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Filtros de películas de TV Ultra 7K (FPA+)
# Version 0.1 (28.06.2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)


import os
import sys
import urllib
import urllib2
import re
import shutil
import zipfile
import time

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import re,urllib,urllib2,sys
import plugintools

from decimal import *
from __main__ import *


addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")


temp = xbmc.translatePath(os.path.join('special://home/userdata/playlists/tmp', ''))
playlists = xbmc.translatePath(os.path.join('special://home/userdata/playlists', ''))
art = xbmc.translatePath(os.path.join('special://home/art', ''))

thumbnail = art + 'icon.png'
fanart = art + 'fanart.jpg'


def xml_skin():
    plugintools.log('[%s %s].xml_skin ' % (addonName, addonVersion))

    mastermenu = plugintools.get_setting("mastermenu")
    xmlmaster = plugintools.get_setting("xmlmaster")
    SelectXMLmenu = plugintools.get_setting("SelectXMLmenu")

    # values="Premium|TV Ultra 7K Team|Latino Total|PLD|T-Killa|Pastebin|Personalizado|Halloween"
    if xmlmaster == 'true':
        if SelectXMLmenu == '0':  # TV Ultra 7K Team
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            plugintools.log("[tv.ultra.7k.xml_skin: "+SelectXMLmenu)
            # Control para ver la intro de TV Ultra 7K
            ver_intro = plugintools.get_setting("ver_intro")
            if ver_intro == "true":
                xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')
				
        elif SelectXMLmenu == '1':   # Nano Kodi
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            if mastermenu == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                # Control para ver la intro de TV Ultra 7K
                ver_intro = plugintools.get_setting("ver_intro")
                if ver_intro == "true":
                    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')				

        elif SelectXMLmenu == '2':   # Latino Total
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            if mastermenu == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                # Control para ver la intro de TV Ultra 7K
                ver_intro = plugintools.get_setting("ver_intro")
                if ver_intro == "true":
                    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')

        elif SelectXMLmenu == '3':   # Proyecto Luz Digital
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            if mastermenu == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                # Control para ver la intro de TV Ultra 7K
                ver_intro = plugintools.get_setting("ver_intro")
                if ver_intro == "true":
                    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')

        elif SelectXMLmenu == '4':   # T-Killa
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            if mastermenu == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                # Control para ver la intro de TV Ultra 7K
                ver_intro = plugintools.get_setting("ver_intro")
                if ver_intro == "true":
                    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')

        elif SelectXMLmenu == '5':  # Pastebin
            id_pastebin = plugintools.get_setting("id_pastebin")
            if id_pastebin == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            else:
                mastermenu = 'http://pastebin.com/raw.php?i=' +id_pastebin
                plugintools.log("[tv.ultra.7k.xml_skin: "+mastermenu)

        elif SelectXMLmenu == '6':   # Personalizado
            id_pastebin = plugintools.get_setting("id_pastebin")
            if id_pastebin == "":
                mastermenu = plugintools.get_setting("mastermenu")
                if mastermenu == "":
                    plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                    mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                    # Control para ver la intro de TV Ultra 7K
                    ver_intro = plugintools.get_setting("ver_intro")
                    if ver_intro == "true":
                        xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')

        elif SelectXMLmenu == '7':   # Halloween
            mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
            if mastermenu == "":
                plugintools.log("[tv.ultra.7k.xml_skin: No definido")
                mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'
                # Control para ver la intro de TV Ultra 7K
                ver_intro = plugintools.get_setting("ver_intro")
                if ver_intro == "true":
                    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')

    else:
        # xmlmaster = False (no activado), menú por defecto
        mastermenu = 'http://pastebin.com/raw.php?i=9ktyM0Mg'

        # Control para ver la intro de TV Ultra 7K
        ver_intro = plugintools.get_setting("ver_intro")
        if ver_intro == "true":
            xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art + 'intro.mp4')


    return mastermenu

def skinlist(params):
    plugintools.log('[%s %s].skinlist ' % (addonName, addonVersion))

    filename = temp + 'skin.lst'
    skinlist = open(filename, "r")
    skinlist.seek(0)
    data = skinlist.readline()
    plugintools.log("data= "+data)    
    while data.startswith("EOF") == False:
        if data == "\n" or data == "":
            data = skinlist.readline()
            print data
            continue
        else:
            data=data.split(",");print 'data',data
            nameskin=data[0];urlskin=data[1]
            plugintools.add_item(action="load_skin", title='[COLOR white]'+nameskin+'[/COLOR]', url=urlskin, thumbnail=params.get("thumbnail"), fanart=params.get("fanart"), folder=True, isPlayable=False)
        data=skinlist.readline()
        
            
            
    
