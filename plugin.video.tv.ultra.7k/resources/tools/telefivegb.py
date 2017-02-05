# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Telefivegb.com
# Version 0.1 (15.03.2016)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info) y a los tutoriales de Juarrox



import os
import sys
import urllib
import urllib2
import re

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import plugintools
import requests
from resources.tools.resolvers import *

playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")


url_pri = 'http://verplusonline.com/category/tv-spain/'
url_ref = 'http://verplusonline.com/'


def telefivegb0(params):
	plugintools.log("[%s %s] Parser www.telefivegb.com... %s " % (addonName, addonVersion, repr(params)))
	extra = params.get("extra")
	url = params.get("url")
	title = params.get("title")
	
	if "Pag." in extra:  # Viene de Paginación
		title=extra
		
	else:
		title="    [COLOR blue][B]Ver Tv Online [I][/B][/COLOR][COLOR yellow][I]    [/I][/COLOR]"
		url = url_pri

	thumbnail = 'https://dl.dropbox.com/s/m3w8aslaxgztjn5/tvendirecto.jpg?dl=0'
	fanart = 'https://dl.dropbox.com/s/yfxrq6zk62h7d31/fondotvultran.jpg?dl=0'

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url}
	r=requests.get(url, headers=headers)
	#r = requests.get(url)
	data = r.content

	plugintools.log("************DATA: "+data+"**************")

	plugintools.add_item(action="",url="",title=title,thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	cada_canal = plugintools.find_multiple_matches(data,'<div class="latestname(.*?)<div class="latestinfo')	

	for item in cada_canal:
		url_canal = plugintools.find_single_match(item,'href="(.*?)/"')
		titulo_canal = plugintools.find_single_match(item,'title="(.*?)"')
		logo_canal = plugintools.find_single_match(item,'img src="(.*?)"')

		if ("http://verplusonline.com" in logo_canal) or ("https://" in logo_canal):
			hacer = "Nada"
		else:
			logo_canal = "http://verplusonline.com" + logo_canal
		
		url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+url_canal+'%26referer='+url_ref
		plugintools.add_item(action="runPlugin",title=titulo_canal,url=url_montada,thumbnail=logo_canal,fanart=fanart,folder=False,isPlayable=True)

	#Resuelvo la posibilidad de mas de 1 Página

	mas_pag = plugintools.find_single_match(data,"'Nav'(.*?)sidebar_right")
	if len(mas_pag) <> 0:  # Hay mas de una página
		pag_actu = plugintools.find_single_match(mas_pag,"class='on'>(.*?)<")
		pag_final = plugintools.find_single_match(mas_pag,"<span>Pages(.*?):").replace(" (","").replace(")","")
		pag_siguiente = str(int(pag_actu)+1)
		url_pag = url + "page/" + pag_siguiente + "/"

		if "Pag." in title:
			title = plugintools.find_single_match(title,"(.*?)   Pag")
			
		extra = "[COLOR lightgreen][B]    ·····"+title+"[I]     Pag. "+pag_siguiente+"[/I]·····[/COLOR]"

		plugintools.add_item(action="telefivegb0",title="[COLORFFFF0759]Página: " + pag_siguiente + "  >>>[/COLOR]", url=url_pag, extra=extra, thumbnail=thumbnail, fanart=fanart, folder=True, isPlayable=False)


		
		
