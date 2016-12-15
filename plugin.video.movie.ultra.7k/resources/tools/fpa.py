# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Filtros de películas de Movie Ultra 7K (FPA+)
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

'''
    # Guardamos la lista...
    filename = url.split("/");i=len(filename);filename=filename[i-1];#plugintools.log("Guardando archivo: "+filename)
    dlfile=playlists+filename+'.m3u'
    
    if os.path.exists(playlists + filename):
        pass
    else:
        try:
            response = urllib2.urlopen(url)
            body = response.read()
        except:
            # Control si la lista está en el cuerpo del HTTP
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
            body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)

        #open the file for writing
        fh = open(playlists + filename, "wb")        
        fh.write(body)
        fh.close()

'''


def filtros0(params, datamovie):
    plugintools.log("[%s %s] Cargando filtros... %s " % (addonName, addonVersion, repr(params)))
    url = params.get("url");title=params.get("title")

    # Analizamos filtros...
    filters = params.get("page")
    if filters.startswith("filtro_year") == True:        
        kolor=plugintools.get_setting("pelis_color")
        kkolor=plugintools.get_setting("pelistitle_color")
        year = datamovie["year"]
        fpa_on = plugintools.get_setting("fpa_on")
        filters=filters.replace("filtro_year:", "")
        if filters == year:
            title = '[COLOR '+kkolor+']'+title+'[/COLOR]'
            title_added = ""
            if fpa_on:  # Se muestran metadatos
                if plugintools.get_setting("showfpa_year") == "true":  # Se muestra año
                    title_added=title_added+' ['+datamovie["year"]+']'
                if plugintools.get_setting("showfpa_punt") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+']'
                if plugintools.get_setting("showfpa_punt2") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+'/'+datamovie["votes"]+']'
                if plugintools.get_setting("showfpa_gen") == "true":  # Se muestra género
                    title_added=title_added+' ['+datamovie["genre"]+']'
                if plugintools.get_setting("showfpa_dir") == "true":  # Se muestra director
                    title_added=title_added+' [Dir.: '+datamovie["director"]+']'
                if plugintools.get_setting("showfpa_wri") == "true":  # Se muestra escritor/guionista
                    title_added='['+datamovie["writer"]+']'
                if plugintools.get_setting("showfpa_cast") == "true":  # Se muestra escritor/guionista
                    cast_final = datamovie["cast"]
                    j=len(cast_final);i=0;total_cast=""
                    while i < j:
                        if total_cast == "": total_cast=cast_final[i]
                        else: total_cast=total_cast+", "+cast_final[i]
                        i = i + 1
                    title_added=title_added+' ['+total_cast+']'
                title=title+' [COLOR '+kolor+']'+title_added+'[/COLOR]'
                return title
        else:
            title = ""
            return title

    elif filters.startswith("filtro_punt") == True:        
        kolor=plugintools.get_setting("pelis_color")
        kkolor=plugintools.get_setting("pelistitle_color")
        punt = datamovie["rating"]
        try:
            punt = Decimal(punt)
            fpa_on = plugintools.get_setting("fpa_on")
            filters=filters.replace("filtro_punt:", "")
            filters=Decimal(filters)
            if int(filters) <= int(punt):
                title = '[COLOR '+kkolor+']'+title+'[/COLOR]'
                title_added = ""
                if fpa_on:  # Se muestran metadatos
                    if plugintools.get_setting("showfpa_year") == "true":  # Se muestra año
                        title_added=title_added+' ['+datamovie["year"]+']'
                    if plugintools.get_setting("showfpa_punt") == "true":  # Se muestra puntuación
                        title_added=title_added+' ['+datamovie["rating"]+']'
                    if plugintools.get_setting("showfpa_punt2") == "true":  # Se muestra puntuación
                        title_added=title_added+' ['+datamovie["rating"]+'/'+datamovie["votes"]+']'
                    if plugintools.get_setting("showfpa_gen") == "true":  # Se muestra género
                        title_added=title_added+' ['+datamovie["genre"]+']'
                    if plugintools.get_setting("showfpa_dir") == "true":  # Se muestra director
                        title_added=title_added+' [Dir.: '+datamovie["director"]+']'
                    if plugintools.get_setting("showfpa_wri") == "true":  # Se muestra escritor/guionista
                        title_added='['+datamovie["writer"]+']'
                    if plugintools.get_setting("showfpa_cast") == "true":  # Se muestra escritor/guionista
                        cast_final = datamovie["cast"]
                        j=len(cast_final);i=0;total_cast=""
                        while i < j:
                            if total_cast == "": total_cast=cast_final[i]
                            else: total_cast=total_cast+", "+cast_final[i]
                            i = i + 1
                        title_added=title_added+' ['+total_cast+']'
                        title=title+' [COLOR '+kolor+']'+title_added+'[/COLOR]'
                        return title
                else:
                    title = ""
                    return title

        except:
            title = ""
            return title
            pass
			
    elif filters.startswith("filtro_gen") == True:
        kolor=plugintools.get_setting("pelis_color")
        kkolor=plugintools.get_setting("pelistitle_color")
        generos = datamovie["genre"];generos=generos.lower()
        fpa_on = plugintools.get_setting("fpa_on")
        filters=filters.replace("filtro_gen:", "")
        if generos.find(filters) >= 0:
            title = '[COLOR '+kkolor+']'+title+'[/COLOR]'
            title_added = ""
            if fpa_on:  # Se muestran metadatos
                if plugintools.get_setting("showfpa_year") == "true":  # Se muestra año
                    title_added=title_added+' ['+datamovie["year"]+']'
                if plugintools.get_setting("showfpa_punt") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+']'
                if plugintools.get_setting("showfpa_punt2") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+'/'+datamovie["votes"]+']'
                if plugintools.get_setting("showfpa_gen") == "true":  # Se muestra género
                    title_added=title_added+' ['+datamovie["genre"]+']'
                if plugintools.get_setting("showfpa_dir") == "true":  # Se muestra director
                    title_added=title_added+' [Dir.: '+datamovie["director"]+']'
                if plugintools.get_setting("showfpa_wri") == "true":  # Se muestra escritor/guionista
                    title_added='['+datamovie["writer"]+']'
                if plugintools.get_setting("showfpa_cast") == "true":  # Se muestra escritor/guionista
                    cast_final = datamovie["cast"]
                    j=len(cast_final);i=0;total_cast=""
                    while i < j:
                        if total_cast == "": total_cast=cast_final[i]
                        else: total_cast=total_cast+", "+cast_final[i]
                        i = i + 1
                    title_added=title_added+' ['+total_cast+']'
                title=title+' [COLOR '+kolor+']'+title_added+'[/COLOR]'
                return title
        else:
            title = ""
            return title

    elif filters.startswith("filtro_title") == True:
        kolor=plugintools.get_setting("pelis_color")
        title_fixed=title.lower()
        fpa_on = plugintools.get_setting("fpa_on")
        filters=filters.replace("filtro_title:", "")
        if title_fixed.find(filters) >= 0:
            plugintools.log("Coincidente con título: "+title_fixed)
            if fpa_on:  # Se muestran metadatos
                return title
        else:
            title = ""
            return title

    elif filters.startswith("filtro_cast") == True:
        kolor=plugintools.get_setting("pelis_color")
        kkolor=plugintools.get_setting("pelistitle_color")
        cast = datamovie["cast"]
        fpa_on = plugintools.get_setting("fpa_on")
        filters=filters.replace("filtro_cast:", "").lower()
        v = 0;w=len(cast)
        while v<w:
            cast_item=cast[v].lower()
            if cast_item.find(filters) >= 0:
                title = '[COLOR '+kkolor+']'+title+'[/COLOR]'
                title_added = ""
                if fpa_on:  # Se muestran metadatos
                    if plugintools.get_setting("showfpa_year") == "true":  # Se muestra año
                        title_added=title_added+' ['+datamovie["year"]+']'
                    if plugintools.get_setting("showfpa_punt") == "true":  # Se muestra puntuación
                        title_added=title_added+' ['+datamovie["rating"]+']'
                    if plugintools.get_setting("showfpa_punt2") == "true":  # Se muestra puntuación
                        title_added=title_added+' ['+datamovie["rating"]+'/'+datamovie["votes"]+']'
                    if plugintools.get_setting("showfpa_gen") == "true":  # Se muestra género
                        title_added=title_added+' ['+datamovie["genre"]+']'
                    if plugintools.get_setting("showfpa_dir") == "true":  # Se muestra director
                        title_added=title_added+' [Dir.: '+datamovie["director"]+']'
                    if plugintools.get_setting("showfpa_wri") == "true":  # Se muestra escritor/guionista
                        title_added='['+datamovie["writer"]+']'
                    if plugintools.get_setting("showfpa_cast") == "true":  # Se muestra escritor/guionista
                        cast_final = datamovie["cast"]
                        j=len(cast_final);i=0;total_cast=""
                        while i < j:
                            if total_cast == "": total_cast=cast_final[i]
                            else: total_cast=total_cast+", "+cast_final[i]
                            i = i + 1
                        title_added=title_added+' ['+total_cast+']'
                    title=title+' [COLOR '+kolor+']'+title_added+'[/COLOR]'
                    v=v+1
                    return title
            else:
                title = ""
                v=v+1
                return title

    elif filters.startswith("filtro_dir") == True:
        kolor=plugintools.get_setting("pelis_color")
        kkolor=plugintools.get_setting("pelistitle_color")
        dir = datamovie["director"].lower()
        fpa_on = plugintools.get_setting("fpa_on")
        filters=filters.replace("filtro_dir:", "").lower()
        if dir.find(filters) >= 0:
            title = '[COLOR '+kkolor+']'+title+'[/COLOR]'
            title_added = ""
            if fpa_on:  # Se muestran metadatos
                if plugintools.get_setting("showfpa_year") == "true":  # Se muestra año
                    title_added=title_added+' ['+datamovie["year"]+']'
                if plugintools.get_setting("showfpa_punt") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+']'
                if plugintools.get_setting("showfpa_punt2") == "true":  # Se muestra puntuación
                    title_added=title_added+' ['+datamovie["rating"]+'/'+datamovie["votes"]+']'
                if plugintools.get_setting("showfpa_gen") == "true":  # Se muestra género
                    title_added=title_added+' ['+datamovie["genre"]+']'
                if plugintools.get_setting("showfpa_dir") == "true":  # Se muestra director
                    title_added=title_added+' [Dir.: '+datamovie["director"]+']'
                if plugintools.get_setting("showfpa_wri") == "true":  # Se muestra escritor/guionista
                    title_added='['+datamovie["writer"]+']'
                if plugintools.get_setting("showfpa_cast") == "true":  # Se muestra escritor/guionista
                    cast_final = datamovie["cast"]
                    j=len(cast_final);i=0;total_cast=""
                    while i < j:
                        if total_cast == "": total_cast=cast_final[i]
                        else: total_cast=total_cast+", "+cast_final[i]
                        i = i + 1
                    title_added=title_added+' ['+total_cast+']'
                title=title+' [COLOR '+kolor+']'+title_added+'[/COLOR]'
                return title
        else:
            title = ""
            return title           

    vista_pelis()


def vista_pelis():
    show=plugintools.get_setting("pelis_view")
    plugintools.modo_vista(show)

