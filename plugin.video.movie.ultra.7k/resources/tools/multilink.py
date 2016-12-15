# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Movie Ultra 7K - Kodi Add-on
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#------------------------------------------------------------
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info
#------------------------------------------------------------

import os
import sys
import urllib
import urllib2
import re
import shutil
import zipfile

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools

from __main__ import *
from resources.tools.media_analyzer import *

# Regex de EPG
from resources.tools.epg_miguiatv import *
from resources.tools.epg_ehf import *
from resources.tools.epg_arenasport import *
from resources.tools.epg_formulatv import *

# Regex de canales
from resources.regex.vaughnlive import *
from resources.regex.ninestream import *
from resources.regex.vercosas import *
from resources.regex.castalba import *
from resources.regex.castdos import *
from resources.regex.directwatch import *
from resources.regex.freetvcast import *
from resources.regex.freebroadcast import *
from resources.regex.sawlive import *
from resources.regex.broadcastlive import *
from resources.regex.businessapp import *
from resources.regex.rdmcast import *
from resources.regex.dinozap import *
from resources.regex.streamingfreetv import *
from resources.regex.byetv import *
from resources.regex.ezcast import *
from resources.regex.janjua import *


# Regex de pelis y series
from resources.linkers.seriesblanco import *
from resources.linkers.seriesflv import *
from resources.linkers.seriesadicto import *
from resources.linkers.seriesyonkis import *
from resources.linkers.seriesmu import *
from resources.linkers.oranline import *
from resources.linkers.cineclasico import *
from resources.linkers.pordede import *
from resources.linkers.pelisadicto import *
from resources.linkers.tvvip_regex import *
from resources.linkers.hdfull_regex import *
from resources.linkers.danko import *
from resources.linkers.inkapelis import *

# Tools & resolvers
from resources.tools.resolvers import *
from resources.tools.mundoplus import *
from resources.tools.bum import *
from resources.tools.yt_playlist import *
from resources.tools.dailymotion import *



playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))


def rtmp_analyzer(params):
    plugintools.log('[%s %s] RTMP Analyzer movie.ultra.7k %s' % (addonName, addonVersion, repr(params)))

    url = params.get("url")

    if url.startswith("rtmp") == True:
    
        if url.find("freetvcast.pw") >= 0:
            freetvcast(params)  
                    
        elif url.find("http://privado.streamingfreetv.net") >= 0:
            streamingfreetv0(params)  		

        elif url.find("9stream") >= 0:            
            ninestreams(params)

        elif url.find("freebroadcast") >= 0:
            freebroadcast(params)   

        elif url.find("cast247") >= 0:
            castdos(params)

        elif url.find("castalba") >= 0:
            castalba(params)     

        elif url.find("direct2watch") >= 0:
            directwatch(params)
        
        elif url.find("vaughnlive") >= 0:
            resolve_vaughnlive(params)

        elif url.find("shidurlive") >= 0:
            shidurlive(params)      
    
        elif url.find("vercosasgratis") >= 0:
            vercosas(params)

        elif url.find("businessapp1") >= 0:
            businessapp0(params)

        elif url.find("broadcastlive") >= 0:
            broadcastlive0(params)             

        elif url.find("pageUrl=http://rdmcast.com") >= 0:
            rdmcast0(params)

        elif url.find("janjua") >= 0:
            janjua0(params)
            
        else:            
            params["url"]=url            
            plugintools.play_resolved_url(url)
        
    elif url.startswith("serie") >= 0:
        if url.find("seriesadicto") >= 0:
            from resources.tools.seriesadicto import *
            seriecatcher(params)
            
        elif url.find("seriesflv") >= 0:
            from resources.tools.seriesflv import *
            lista_capis(params)

        elif url.find("seriesyonkis") >= 0:
            from resources.tools.seriesyonkis import *
            serie_capis(params)

        elif url.find("seriesblanco") >= 0:
            from resources.tools.seriesblanco import *
            seriesblanco0(params)

        elif url.find("seriesmu") >= 0:
            from resources.tools.seriesblanco import *
            seriesmu0(params)
			
        elif url.find("hdfull.tv") >= 0:
            from resources.tools.hdfull_regex import *
            hdfull_regex0(params)

        elif url.find("tv-vip.com") >= 0:
            from resources.tools.tvvip_regex import *
            tvvip_regex0(params)

        elif url.find("inkapelis") >= 0:
            from resources.tools.inkapelis import *
            inkapelis_linker0(params)

        elif url.find("descargacineclasico") >= 0:
            from resources.tools.cineclasico import *
            cineclasico_linker0(params)

        elif url.find("seriesdanko") >= 0:
            from resources.tools.danko import *
            danko_linker0(params)            

    elif url.startswith("bum") == True or url.startswith("BUM") == True:
        from resources.tools.bum import *
        url = url.strip()
        title = title.replace(" [COLOR lightyellow][B][BUM+][/COLOR]", "").strip()
        params["title"]=title
        params["url"]=url
        get_server(params)
        bum_multiparser(params)
 
    else:
	plugintools.play_resolved_url(url)




#def play_url(url):
def play_url(params):
    #plugintools.log('[%s %s].play %s' % (addonName, addonVersion, url))	
    plugintools.log('[%s %s].play %s' % (addonName, addonVersion, params))	

    params = plugintools.get_params()
    url = params.get("url")

    # Notificación de inicio de resolver en caso de enlace RTMP
    url = url.strip()

    if url.startswith("http") == True:
        if url.find("allmyvideos") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            allmyvideos(params)
        elif url.find("streamcloud") >= 0 :
            params["url"]=url
            params["title"]=title
            params = plugintools.get_params() 
            streamcloud(params)
        elif url.find("vidspot") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            vidspot(params)
        elif url.find("played.to") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            playedto(params)
        elif url.find("vk.com") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            vk(params)
        elif url.find("nowvideo") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            nowvideo(params)
        elif url.find("tumi") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            tumi(params)
        elif url.find("streamin.to") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            streaminto(params)
        elif url.find("veehd") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            veehd(params)
        elif url.find("novamov") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            novamov(params)
        elif url.find("gamovideo") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            gamovideo(params)
        elif url.find("movshare") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            movshare(params)
        elif url.find("powvideo") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            powvideo(params)
        elif url.find("mail.ru") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            mailru(params)
        elif url.find("tumi.tv") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            tumi(params)
        elif url.find("videobam") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            videobam(params)
        elif url.find("videoweed") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            videoweed(params)
        elif url.find("streamable") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            streamable(params)
        elif url.find("rocvideo") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            rocvideo(params)
        elif url.find("realvid") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            realvid(params)
        elif url.find("netu") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            netu(params)
        elif url.find("waaw") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            waaw(params)            
        elif url.find("videomega") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            videomega(params)
        elif url.find("video.tt") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            videott(params)
        elif url.find("flashx.tv") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            flashx(params)
        elif url.find("ok.ru") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            okru(params)
        elif url.find("vidto.me") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            vidtome(params)
        elif url.find("openload") >= 0 :
            params = plugintools.get_params()
            params["url"]=url
            openload(params)            
        else:
            url = url.strip()
            plugintools.play_resolved_url(url)

    elif url.startswith("rtp") >= 0:  # Control para enlaces de Movistar TV
        plugintools.play_resolved_url(url)
       
    else:
        plugintools.play_resolved_url(url)



def url_analyzer(params):
    #plugintools.log('[%s %s].URL Analyzer %s' % (addonName, addonVersion, repr(params)))
    url = params.get("url");title='[COLOR white]'+params.get("title").replace("[Multi]","").strip()+'[/COLOR]';title = multiparse_title(title,url)
    thumbnail = params.get("thumbnail");fanart=params.get("fanart");datamovie={};datamovie["plot"] = params.get("plot")

    if url.startswith("plugin") == True:
        plot = params.get("plot")
        title=params.get("title").replace("[Multi]", "").strip()
        plugin_analyzer(url, title, plot, datamovie, thumbnail, fanart)
    
 
    elif url.startswith("llamada") == True:

        plot = params.get("plot")
        title=params.get("title")  # .replace("[Multi]", "").strip()
        ruta_llamadas = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie.ultra.7k/resources/llamadas/', ''))  # Esto irá en default.py
        url = url.replace("llamada:", "")
        comandos = url.split("; ")
        fich_llamada = ruta_llamadas + comandos[0] + ".txt"  # El 1º es el nombre del fichero

        archivo_llamada = open(fich_llamada, "r")
        url_llamada = archivo_llamada.read()
        num_comandos = len(comandos)

        for comando in range(1, num_comandos):  # Empiezo en 1 para saltarme el 1º, q es el nombre del fichero, no un "comando" a reemplazar
            sustituye = plugintools.find_single_match(comandos[comando],'(.*?)=')
            por_este = plugintools.find_single_match(comandos[comando],'=(.*)')
            url_llamada = url_llamada.replace(sustituye, por_este)

        thumbnail=params.get("thumbnail")
        fanart=params.get("fanart")

        plugin_analyzer(url_llamada, title, plot, datamovie, thumbnail, fanart)
		
		
		
		  #*********DMO**********
    elif url.find("diskokosmiko") >= 0:
        #plugintools.add_item(action="kosmiko_linker", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False) 
        from resources.tools.listmaker import *
        url_montada = lanza_kosmipop(url=url)
        plugintools.runAddon(action="runPlugin" , title=title, url=url_montada, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False) 

    elif url.find("copiapop") >= 0:
        #plugintools.add_item(action="kosmiko_linker", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False) 
        from resources.tools.listmaker import *
        url_montada = lanza_kosmipop(url=url)
        plugintools.runAddon(action="runPlugin" , title=title, url=url_montada, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False) 
    #*********DMO**********

    elif url.startswith("bum") == True:
        #title_fixed = multiparse_title(title, url)
        plugintools.addDir( action = "bum_linker" , title = title, url = url.replace("bum:", "").strip(), thumbnail = thumbnail, extra=url.replace("bum:", ""), fanart = fanart , folder = True , isPlayable = False )         
		
    elif url.startswith("peli") == True:
        if url.find("oranline") >= 0:
            url = url.replace("peli:", "");#url=url.replace("oranline.com/pelicula/", "oranline.com/?review=")
            plugintools.add_item(action="oranline_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("pelisadicto") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="pelisadicto_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("pordede") >= 0:
            url = url.replace("peli:", "").strip()
            url_links=url.replace("/peli/","/links/view/slug/")+"/what/peli"
            plugintools.add_item(action="pordede_linker0", title=title, url=url_links, thumbnail=thumbnail, fanart=fanart, extra="regex", page=url, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("hdfull.tv") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="hdfull_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=url, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("tv-vip.com") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="tvvip_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=url, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("inkapelis") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="inkapelis_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=url, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("descargacineclasico") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="cineclasico_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=url, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("pelisdanko") >= 0:
            url = url.replace("peli:", "").strip()
            plugintools.add_item(action="danko_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=url, info_labels=datamovie, folder=True, isPlayable=False)
			
    elif url.startswith("devil:") == True:
        url = url.replace("devil:", "").replace(" referer=","%26referer=")
        url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+url  # +'%26referer='+referer
        plugintools.add_item(action="runPlugin", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder = False, isPlayable=True)            
        
    elif url.startswith("serie") == True:
        url = url.replace("serie:", "")
        if url.find("seriesflv") >= 0:
            plugintools.add_item(action="seriesflv_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("seriesyonkis") >= 0:
            plugintools.add_item(action="serieyonkis_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("seriesadicto") >= 0:
            plugintools.add_item(action="seriesadicto_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("seriesblanco") >= 0:
            plugintools.add_item(action="seriesblanco_linker0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("pordede") >= 0:
            plugintools.add_item(action="pordede_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)    
        elif url.find("hdfull.tv") >= 0:
            plugintools.add_item(action="hdfull_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False) 
        elif url.find("tv-vip.com") >= 0:
            plugintools.add_item(action="tvvip_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("inkapelis") >= 0:
            plugintools.add_item(action="inkapelis_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("descargacineclasico") >= 0:
            plugintools.add_item(action="cineclasico_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        elif url.find("seriesdanko") >= 0:
            plugintools.add_item(action="danko_linker0", title=title, url=url, page=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)            

    elif url.startswith("rtmp") == True or url.startswith("rtsp") == True:
        plugintools.add_item(action="rtmp_analyzer", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
        
    elif url.startswith("http") == True:
        server = video_analyzer(url)
        if server != "unknown":
            #*********DMO**********
            if url.find("diskokosmiko") >= 0 or url.find("copiapop") >= 0:
                from resources.tools.listmaker import *
                url_montada = lanza_kosmipop(url=url)
                plugintools.runAddon(action="runPlugin" , title=title, url=url_montada, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)

            else:
                plugintools.add_item(action=server, title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
            #*********DMO**********
        
        elif url.find("dailymotion.com/video") >= 0:
            plugintools.log("Dailymotion: "+url)
            video_id = dailym_getvideo(url)
            if video_id != "":
                thumbnail = "https://api.dailymotion.com/thumbnail/video/"+video_id+""
                url = "plugin://plugin.video.dailymotion_com/?url="+video_id+"&mode=playVideo"
                plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=params.get("fanart"), info_labels=datamovie, folder=False, isPlayable=True)

        elif url.find("dailymotion.com/playlist") >= 0:
            plugintools.log("Dailymotion: "+url)
            id_playlist = dailym_getplaylist(url)
            if id_playlist != "":
                url = "https://api.dailymotion.com/playlist/"+id_playlist+"/videos"
                thumbnail = "https://api.dailymotion.com/thumbnail/video/"+id_playlist
                if thumbnail == "":
                    thumbnail = 'http://press.dailymotion.com/wp-old/wp-content/uploads/logo-Dailymotion.png'
                url = "https://api.dailymotion.com/playlist/"+id_playlist+"/videos"
                plugintools.add_item(action="dailym_pl", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
    
        elif url.find("https://www.youtube.com/watch?") >= 0:
            plot = params.get("plot")
            title=params.get("title").replace("[Multi]", "").strip()
            videoid = url.replace("https://www.youtube.com/watch?v=", "")
            url = 'plugin://plugin.video.youtube/play/?video_id='+videoid
            plugin_analyzer(url, title, plot, datamovie, thumbnail, fanart)                
                
        elif url.find(".m3u8") >= 0:
            plugintools.add_item(action="play", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)

        else:
            plugintools.add_item(action="play", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
            
    elif url.startswith("udp") == True:
        plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
    
    elif url.startswith("rtp") == True:
        plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
        
    elif url.startswith("mms") == True:
        plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
            
    elif url.startswith("sop") == True:
        # plugin://plugin.video.p2p-streams/?url=sop://124.232.150.188:3912/11265&mode=2&name=Titulo+canal+Sopcast
        url = 'plugin://plugin.video.p2p-streams/?url=' + url + '&mode=2&name='
        plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)
        
    elif url.startswith("ace") == True:
        plugintools.log("Acestream: "+url)
        url = url.replace("ace:", "")
        url = 'plugin://plugin.video.p2p-streams/?url=' + url + '&mode=1&name='
        plugintools.add_item(action="play_url", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)
    
    elif url.startswith("yt_playlist") == True:
        pid = url.replace("yt_playlist(", "")
        pid = pid.replace(")", "").strip()
        pid = pid+'/';pid=pid.strip();pid.replace(" ", "")
        url = 'plugin://plugin.video.youtube/playlist/'+pid
        plugintools.add_item(action="run_tube", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
        
    elif url.startswith("yt_channel") == True:
        uid = url.replace("yt_channel(", "")
        uid = uid.replace(")", "").strip()
        uid = uid+'/';uid=uid.strip();uid.replace(" ", "")        
        url = 'plugin://plugin.video.youtube/user/'+uid
        plugintools.add_item(action="run_tube2", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)
            
    elif url.startswith("short") == True:
        url = url.replace("short:", "").strip()                
        plugintools.add_item(action="longurl", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)                

    elif url.startswith("devil") == True:
        url_devil = url.replace("devil:", "").replace(" referer=","%26referer=")
        url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+url_devil  # +'%26referer='+referer
        #xbmc.executebuiltin('XBMC.RunPlugin(' + url +')')
        plugintools.add_item(action="runPlugin", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)
        
    elif url.startswith("bum") == True:
        plugintools.add_item(action="bum_multiparser", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)

    elif url.startswith("txt") == True:
        from resources.tools.txt_reader import *
        url=url.replace("txt:", "")
        plugintools.add_item(action="txt_reader", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)

    elif url.startswith("epg-txt") == True:
        from resources.tools.epg_txt import *
        url=url.replace("epg-txt:", "")
        url = epg_txt_dict(parser_title(url))
        plugintools.add_item(action="epg_txt0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                

    elif url.startswith("agendatv") == True:
        url = url.replace("agendatv:", "").strip()
        if url == "futbolenlatv":
            url = 'http://agenda.futbolenlatv.com/m?deporte=agenda'
            plugintools.add_item(action="futbolentv0", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                    
        elif url == "footballonuktv":
            url = 'http://www.footballonuktv.com/'
            plugintools.add_item(action="agendatv", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                                        
        elif url == "calciointv":
            url = 'http://www.calciointv.com/'
            plugintools.add_item(action="agendatv", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                                        
        elif url == "futbolenlatele":
            url = 'http://www.futbolenlatele.com'
            plugintools.add_item(action="agendatv", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                                        
        elif url == "queverahora":
            url = 'http://www.formulatv.com/programacion/'
            plugintools.add_item(action="epg_verahora", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=False)                    
        else:
            plugintools.add_item(action="play", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=True, isPlayable=False)                    

    elif url.startswith("torrent") == True:
        url = p2p_builder_url(url, title, p2p="torrent")
        plugintools.add_item(action="launch_torrent", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)

    elif url.startswith("magnet") == True:
        url = p2p_builder_url(url, title, p2p="magnet")
        plugintools.add_item(action="launch_magnet", title=title, url=url, thumbnail=thumbnail, fanart=fanart, info_labels=datamovie, folder=False, isPlayable=True)
    
    elif url == "mundoplus":
        plugintools.add_item(action="mundoplus_guide", title=title, url=url, thumbnail=thumbnail, fanart=fanart, page=params.get("page"), info_labels=datamovie, folder=True, isPlayable=False)
    
    elif url.startswith("goear") == True:
        id_goear = url.replace("goear:", "").replace('"', "").strip()
        url = 'http://www.goear.com/action/sound/get/'+id_goear
        plugintools.add_item(action="play", title=title, url=url, thumbnail=thumbnail, fanart=fanart, extra="regex", info_labels=datamovie, folder=True, isPlayable=False)

    else:
        plugintools.add_item(action="play", title=title, url=url, thumbnail=thumbnail, fanart=fanart, extra="regex", info_labels=datamovie, folder=True, isPlayable=False)
        

def youtube_playlists(url):
    plugintools.log('[%s %s].youtube_playlists %s' % (addonName, addonVersion, url))	
    
    data = plugintools.read(url)
        
    pattern = ""
    matches = plugintools.find_multiple_matches(data,"<entry(.*?)</entry>")
    
    for entry in matches:
        plugintools.log("entry="+entry)
        
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>")
        plot = plugintools.find_single_match(entry,"<media\:descriptio[^>]+>([^<]+)</media\:description>")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")           
        url = plugintools.find_single_match(entry,"<content type\='application/atom\+xml\;type\=feed' src='([^']+)'/>")
        fanart = art + 'youtube.png'
        
        plugintools.add_item( action="youtube_videos" , title=title , plot=plot , url=url , thumbnail=thumbnail , fanart=fanart , folder=True )
        plugintools.log("fanart= "+fanart)


# Muestra todos los vídeos del playlist de Youtube
def youtube_videos(url):
    plugintools.log('[%s %s].youtube_videos %s' % (addonName, addonVersion, url))	
    
    # Fetch video list from YouTube feed
    data = plugintools.read(url)
    plugintools.log("data= "+data)
    
    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(data,"<entry(.*?)</entry>")
    
    for entry in matches:
        plugintools.log("entry="+entry)
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>")
        title = title.replace("I Love Handball | ","")
        plot = plugintools.find_single_match(entry,"<summa[^>]+>([^<]+)</summa")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        fanart = art+'youtube.png'
        video_id = plugintools.find_single_match(entry,"http\://www.youtube.com/watch\?v\=([0-9A-Za-z_-]{11})")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , fanart=fanart , isPlayable=True, folder=False )


def parse_url(url):
    if url != "":
        url = url.strip()
        url = url.replace("rtmp://$OPT:rtmp-raw=", "")        
        return url
    
    else:
        plugintools.log("error en url= ")  # Mostrar diálogo de error al parsear url (por no existir, por ejemplo)


def multilink(params):
    plugintools.log('[%s %s] movie.ultra.7k Multilink %s' % (addonName, addonVersion, repr(params)))
    dialog = xbmcgui.Dialog()
    filename = params.get("extra")
    file = open(playlists + filename, "r")
    file.seek(0)
    title = params.get("title")
    title_parsed = parser_title(params.get("title"))
    if title.find("  ") >= 0:
        title = "@"+title.split("  ")[0].strip()  # En la lista aparecerá el título precedido por el símbolo @
    if title.startswith("[COLOR white]") == True:
        title_fixed=title[13:].strip()
        encuentra = '#EXTINF:-1,' + title_fixed.replace("[COLOR lightyellow][/COLOR]","").strip()
    else:
        encuentra = '#EXTINF:-1,' + title.replace("[COLOR lightyellow][Multi][/COLOR]","").strip()
    if encuentra.startswith("#EXTINF:-1,@") == True:
        title_epg = title.replace("[COLOR white]","").split("[COLOR orange")
        if len(title_epg) >= 1:
            title_epg = title_epg[0]
        encuentra = '#EXTINF:-1,'+title_epg;encuentra=encuentra.strip()
    plugintools.log("*** Texto a buscar= "+encuentra)
    i = 0
    data = file.readline()
    if data.startswith("#EXTINF:-1,@") == True:
        epg_no = plugintools.get_setting("epg_no")
        plugintools.log("epg_no= "+epg_no)
        if epg_no == "0":  # No desactivado EPG
            pass
        else:
            data = data.replace("@", "")
    encuentra = encuentra.replace("@", "")    
    while i <=8:  # Control para EOF
        if data == "":
            i = i + 1
            data = file.readline().strip()
            if data.startswith("#EXTINF:-1,@") == True:
                data = data.replace("@", "")
            continue
        else:
            i = 0
            plugintools.log("A buscar: "+encuentra)
            plugintools.log("Leyendo... "+data)
            if data.startswith(encuentra) == True or data.startswith('#EXTINF:-1,@' + title.replace(" [COLOR lightyellow][Multi][/COLOR]","")) == True:
                data = file.readline().strip()
                if data == "#multi" or data == "#multilink":
                    #Leemos número de enlaces
                    i = 1  # Variable contador desde 1 porque nos servirá para nombrar los títulos
                    # Recopilamos enlaces en una lista
                    linea_url = file.readline().strip()
                    if linea_url.startswith("desc") == True:
                        linea_url = file.readline().strip()                        
                    title_options = []
                    url_options = []
                    while linea_url != "#multi" :
                        linea_url = linea_url.strip().split(",")
                        subcomas = len(linea_url)  # Parche para enlaces con comas (Stalker, Livestreamspro, etc)
                        url_option = linea_url[1:subcomas]
                        i = 0;hurl=""
                        for item in url_option:
                            if hurl == "":
                                hurl = url_option[i]
                            else:
                                hurl=hurl+','+url_option[i].strip()
                            i = i + 1
                        #plugintools.log("#multi: "+hurl)
                        url_option=hurl
                        # Fin del parche para enlaces con comas (plugin://)
                        title_option = linea_url[0]                        
                        if title_option.startswith("@") == True:
                            title_option = title_option.replace("@", "")

                            # Ejecutamos EPG...
                            epg_channel = []
                            epg_channel = epg_now(title_option)
                            if epg_now(title_option) == False:
                                pass
                            else:
                                try:
                                    ejemplo = epg_channel[0]
                                    title_option = title_option + " [COLOR orange][I][B] " + epg_channel[0] + "[/B] " + epg_channel[1] + "[/I][/COLOR] "
                                except:
                                    pass
                                
                        i = i + 1
                        title_options.append(title_option)
                        url_options.append(url_option)
                        linea_url = file.readline()
                        linea_url = linea_url.strip()
                num_items = i - 1                
                if title.startswith("@") == True:  # Para evitar que en el título del cuadro de diálogo aparezca el nombre del canal precedido por el símbolo arroba (@)
                    title = title.replace("@","")

                try:
                    i = 0
                    datamovie={}
                    datamovie["Plot"]=params.get("plot")
                    plot=params.get("plot")
                    #while i <= num_items:                        
                    for item in title_options:
                        url_opc = url_options[i]
                        descripcion = title_options[i]
                        thumbnail=params.get("thumbnail");fanart=params.get("fanart")
                        params["url"]=url_opc;params["title"]=title_options[i]
                        datamovie["plot"]=plot
                        params["page"]=parser_title(title).strip()
                        url_analyzer(params)
                        i = i + 1
                        
                except KeyboardInterrupt: pass;
                except IndexError: raise;
            else:
                data = file.readline().strip()        


# Esta función añade coletilla de tipo de enlace a los multilink
def multiparse_title(title, url):
    if url == "mundoplus":
        title = title + ' [COLOR blue][B][Guía[B]TV[/B][/COLOR]' 

    elif url.startswith("serie") == True:
        if url.find("seriesflv") >= 0:
            title = title + ' [COLOR blue][B][Series[B]FLV[/B]][/COLOR]'
        if url.find("seriesyonkis") >= 0:
            title = title + ' [COLOR blue][B][Series[B]Yonkis[/B]][/COLOR]'
        if url.find("seriesadicto") >= 0:
            title = title + ' [COLOR blue][B][Series[B]Adicto[/B]][/COLOR]'
        if url.find("seriesblanco") >= 0:
            title = title + ' [COLOR blue][B][Series[B]Blanco[/B]][/COLOR]'
        if url.find("series.mu") >= 0:
            title = title + ' [COLOR blue][B][Series[B].Mu[/B]][/COLOR]'
        if url.find("tv-vip.com") >= 0:
            title = title + ' [COLOR blue][B][TV-VIP][/B][/COLOR]'

    elif url.startswith("peli") == True:
        if url.find("oranline") >= 0:
            title = title + ' [COLOR blue][B][Oranline][/B][/COLOR]'
        if url.find("pelisadicto") >= 0:
            title = title + ' [COLOR blue][B][PelisAdicto][/B][/COLOR]'
        if url.find("pordede") >= 0:
            title = title + ' [COLOR blue][B][Pordede][/B][/COLOR]'
        if url.find("openload") >= 0:
            title = title + ' [COLOR blue][B][Openload][/B][/COLOR]'
        if url.find("tv-vip.com") >= 0:
            title = title + ' [COLOR blue][B][TV-VIP][/B][/COLOR]'
        if url.find("inkapelis") >= 0:
            title = title + ' [COLOR blue][B][Inkapelis][/B][/COLOR]'
        if url.find("descargacineclasico") >= 0:
            title = title + ' [COLOR blue][B][DescargaCineClásico][/B][/COLOR]'
        if url.find("pelisdanko") >= 0:
            title = title + ' [COLOR blue][B][PelisDanko][/B][/COLOR]'

    elif url.startswith("txt:") == True:
        title = title + ' [COLOR blue][B][TXT][/B][/COLOR]'

    elif url.startswith("epg-txt:") == True:
        title = title + ' [COLOR blue][B][EPG-TXT][/B][/COLOR]'        

    elif url.startswith("goear") == True:
        title = title + ' [COLOR blue][B][goear][/B][/COLOR]'        

    elif url.startswith("http") == True:        
        if url.find("allmyvideos") >= 0:
            title = title + ' [COLOR green][B][Allmyvideos][/B][/COLOR]'

        elif url.find("streamcloud") >= 0:
            title = title + ' [COLOR green][B][Streamcloud][/B][/COLOR]'

        elif url.find("vidspot") >= 0:
            title = title + ' [COLOR green][B][Vidspot][/B][/COLOR]'
            
        elif url.find("played.to") >= 0:
            title = title + ' [COLOR green][B][Played.to][/B][/COLOR]'       

        elif url.find("vk.com") >= 0:
            title = title + ' [COLOR green][B][Vk][/B][/COLOR]'

        elif url.find("nowvideo") >= 0:
            title = title + ' [COLOR green][B][Nowvideo.sx][/B][/COLOR]'            
        
        elif url.find("tumi") >= 0:
            title = title + ' [COLOR green][B][Tumi][/B][/COLOR]'

        elif url.find("streamin.to") >= 0:
            title = title + ' [COLOR green][B][Streamin.to][/B][/COLOR]'

        elif url.find("veehd") >= 0:
            title = title + ' [COLOR green][B][Veehd][/B][/COLOR]'
            
        elif url.find("tumi.tv") >= 0:
            title = title + ' [COLOR green][B][Tumi.tv][/B][/COLOR]'       

        elif url.find("novamov") >= 0:
            title = title + ' [COLOR green][B][Novamov][/B][/COLOR]'

        elif url.find("gamovideo") >= 0:
            title = title + ' [COLOR green][B][Gamovideo][/B][/COLOR]'            
        
        elif url.find("moevideos") >= 0:
            title = title + ' [COLOR green][B][Moevideos][/B][/COLOR]'

        elif url.find("movshare") >= 0:
            title = title + ' [COLOR green][B][Movshare][/B][/COLOR]'

        elif url.find("powvideo") >= 0:
            title = title + ' [COLOR green][B][Powvideo][/B][/COLOR]'

        elif url.find("mail.ru") >= 0:
            title = title + ' [COLOR green][B][Mail.ru][/B][/COLOR]'

        elif url.find("videobam") >= 0:
            title = title + ' [COLOR green][B][Videobam][/B][/COLOR]'
            
        elif url.find("videoweed") >= 0:
            title = title + ' [COLOR green][B][Videoweed][/B][/COLOR]'

        elif url.find("streamable") >= 0:
            title = title + ' [COLOR green][B][Streamable][/B][/COLOR]'

        elif url.find("rocvideo") >= 0:
            title = title + ' [COLOR green][B][Rocvideo][/B][/COLOR]'

        elif url.find("realvid") >= 0:
            title = title + ' [COLOR green][B][Realvid][/B][/COLOR]'

        elif url.find("netu") >= 0:
            title = title + ' [COLOR green][B][Netu][/B][/COLOR]'

        elif url.find("waaw") >= 0:
            title = title + ' [COLOR green][B][Waaw.tv][/B][/COLOR]'            

        elif url.find("videomega") >= 0:
            title = title + ' [COLOR green][B][Videomega][/B][/COLOR]'

        elif url.find("video.tt") >= 0:
            title = title + ' [COLOR green][B][Video.tt][/B][/COLOR]'

        elif url.find("flashx.tv") >= 0:
            title = title + ' [COLOR green][B][Flashx][/B][/COLOR]'

        elif url.find("ok.ru") >= 0:
            title = title + ' [COLOR green][B][Ok.ru][/B][/COLOR]'

        elif url.find("vidto.me") >= 0:
            title = title + ' [COLOR green][B][Vidto.me][/B][/COLOR]'

        elif url.find("turbovideos") >= 0:
            title = title + ' [COLOR green][B][Turbovideos][/B][/COLOR]'            

        elif url.find("openload") >= 0:
            title = title + ' [COLOR green][B][Openload][/B][/COLOR]'

        elif url.find("copiapop") >= 0:
            title = title + ' [COLOR green][B][Copiapop][/B][/COLOR]'                 

        elif url.find("www.youtube.com") >= 0:
            title = title + ' [COLOR red][B][Youtube][/B][/COLOR]'

        elif url.find("dailymotion.com/video") >= 0:
            title = title + ' [COLOR lightyellow][B][Dailymotion Video][/B][/COLOR]'

        elif url.find("dailymotion.com/playlist") >= 0:
            title = title + ' [COLOR lightyellow][B][Dailymotion Playlist][/B][/COLOR]'

        elif url.find("lolabits.es") >= 0:
            title = title + ' [COLOR lightyellow][B][Lolabits][/B][/COLOR]'

        elif url.find(".m3u8") >= 0:
            title = title + ' [COLOR green][B][M3u8][/B][/COLOR]'

        else:
            title = title + ' [COLOR blue][B][HD Exclusivex PM][/B][/COLOR]'
            
    elif url.startswith("rtmp") == True:        
        if url.find("iguide.to") >= 0:
            title = title + ' [COLOR lightyellow][B][iguide][/B][/COLOR]'
        elif url.find("mips") >= 0:
            title = title + ' [COLOR lightyellow][B][mips][/B][/COLOR]'            
        elif url.find("freetvcast.pw") >= 0:
            title = title + ' [COLOR lightyellow[B][freetvcast][/B][/COLOR]'
        elif url.find("pageUrl=http://privado.streamingfreetv.net") >= 0:
            title = title + ' [COLOR lightyellow][B][streamingfreetv][/B][/COLOR]'
        elif url.find("9stream") >= 0:
            title = title + ' [COLOR lightyellow][B][9stream][/B][/COLOR]'
        elif url.find("freebroadcast") >= 0:
            title = title + ' [COLOR lightyellow][B][freebroadcast][/B][/COLOR]'
        elif url.find("cast247") >= 0:
            title = title + ' [COLOR lightyellow][B][cast247][/B][/COLOR]'
        elif url.find("castalba") >= 0:
            title = title + ' [COLOR lightyellow][B][castalba][/B][/COLOR]'
        elif url.find("direct2watch") >= 0:
            title = title + ' [COLOR lightyellow][B][direct2watch][/B][/COLOR]'
        elif url.find("vaughnlive") >= 0:
            title = title + ' [COLOR lightyellow][B][vaughnlive][/B][/COLOR]'
        elif url.find("sawlive") >= 0:
            title = title + ' [COLOR lightyellow][B][sawlive][/B][/COLOR]'        
        elif url.find("shidurlive") >= 0:
            title = title + ' [COLOR lightyellow][B][shidurlive][/B][/COLOR]'
        elif url.find("vercosas") >= 0:
            title = title + ' [COLOR lightyellow][B][vercosas][/B][/COLOR]'
        elif url.find("pageUrl=http://rdmcast.com") >= 0:
            title = title + ' [COLOR lightyellow][B][rdmcast][/B][/COLOR]'
        elif url.find("businessapp1") >= 0:
            title = title + ' [COLOR lightyellow][B][businessapp1][/B][/COLOR]'
        elif url.find("broadcastlive") >= 0:
            title = title + ' [COLOR lightyellow][B][broadcastlive][/B][/COLOR]'               
        else:
            title = title + ' [COLOR green][B][rtmp][/B][/COLOR]'            
            
    elif url.startswith("udp") == True:
        title = title + ' [COLOR lightyellow][B][udp][/B][/COLOR]'         
    
    elif url.startswith("rtp") == True:
        title = title + ' [COLOR lightyellow][B][rtp][/B][/COLOR]'            
    
    elif url.startswith("mms") == True:
        title = title + ' [COLOR lightyellow][B][mms][/B][/COLOR]'      

    elif url.startswith("plugin") == True:
        if url.startswith("plugin://plugin.video.SportsDevil/") == True:
            title = title + ' [COLOR blue][B][SportsDevil][/B][/COLOR]'

        elif url.startswith("plugin://plugin.video.f4mTester") == True:
            title = title + ' [COLOR lightyellow][B][F4M][/B][/COLOR]'
                        
        elif url.startswith("plugin://plugin.video.youtube/") == True:
            if url.startswith("plugin://plugin.video.youtube/play/") == True:
                title = title + ' [COLOR red][B][Youtube Video][/B][/COLOR]'

            elif url.startswith("plugin://plugin.video.youtube/user/") == True:
                title = title + ' [COLOR lightyellow][B][Youtube User][/B][/COLOR]'

            elif url.startswith("plugin://plugin.video.youtube/channel/") == True:
                title = title + ' [COLOR lightyellow][B][Youtube Channel][/B][/COLOR]'
            
        elif url.find("plugin.video.p2p-streams") == True:                        
            if url.find("mode=1") >= 0 :  # Acestream
                title = title + ' [COLOR lightyellow][B][Acestream][/B][/COLOR]'
                            
            elif url.find("mode=2") >= 0 :  # Sopcast
                title = title + ' [COLOR lightyellow][B][Sopcast][/B][/COLOR]'

            elif url.find("mode=401") >= 0 :  # P2P-Streams Parser
                title = title + ' [COLOR lightyellow][B][p2p-streams parser][/B][/COLOR]'

        elif url.startswith("plugin://plugin.video.p2psport") == True:
            title = title + ' [COLOR lightyellow][B][P2P Sport][/B][/COLOR]'

        elif url.startswith("plugin://plugin.video.live.streamspro") == True:
            title = title + ' [COLOR lightyellow][B][Livestreams][/B][/COLOR]'

        elif url.startswith("plugin://plugin.video.stalker") == True:
            title = title + ' [COLOR lightyellow][B][Stalker][/B][/COLOR]'

        elif url.startswith("plugin://plugin.video.pelisalacarta/") == True:
            title = title + ' [COLOR blue][B][Pelisalacarta][/B][/COLOR]'            
            
        else:
            title = title + ' [COLOR lightyellow][B][Addon][/B][/COLOR]'
            
    elif url.startswith("magnet") == True:
        title = title + ' [COLOR lightyellow][B][Magnet][/B][/COLOR]'

    elif url.startswith("torrent") == True:
        title = title + ' [COLOR lightyellow][B][Torrent][/B][/COLOR]'        

    elif url.startswith("sop") == True:
        title = title + ' [COLOR lightyellow][B][Sopcast][/B][/COLOR]'        
        
    elif url.startswith("ace") == True:
        title = title + ' [COLOR lightyellow][B][Acestream][/B][/COLOR]'

    elif url.startswith("yt") == True:
        if url.startswith("yt_playlist") == True:
            title = title + ' [COLOR lightyellow][B][Youtube Playlist][/B][/COLOR]'

        elif url.startswith("yt_channel") == True:
            title = title + ' [COLOR lightyellow][B][Youtube Channel][/B][/COLOR]'

    elif url.startswith("bum") == True:
        title = title + ' [COLOR lightyellow][B][BUM+][/B][/COLOR]'        

    elif url.startswith("devil") == True:
        title = title + ' [COLOR blue][B][SportsDevil][/B][/COLOR]'

    elif url.startswith("short") == True:
        title = title + ' [COLOR lightyellow][B][ShortLink][/B][/COLOR]'        

    elif url.startswith("img") == True:
        title = title + ' [COLOR lightyellow][B][IMG][/B][/COLOR]'

    elif url.startswith("agendatv") == True:
        title = title + ' [COLOR lightyellow][B][Agenda TV][/B][/COLOR]'          
        
    else:
        plugintools.log("URL desconocida= "+url)
        title = title + ' [COLOR red][B][Desconocido][/B][/COLOR]'

    plugintools.log("title= "+title)
    return title


# Función modificada de show_image para multilinks para evitare rror en url = params.get("url") porque url es #multilink 
def show_image(url):
    plugintools.log('[%s %s].show_image %s' % (addonName, addonVersion, url))

    plugintools.log("Iniciando descarga desde..."+url)
    h=urllib2.HTTPHandler(debuglevel=0)  # Iniciamos descarga...
    request = urllib2.Request(url)
    opener = urllib2.build_opener(h)
    urllib2.install_opener(opener)
    filename = url.split("/")
    max_len = len(filename)
    max_len = int(max_len) - 1
    filename = filename[max_len]
    fh = open(__temp__ + filename, "wb")  #open the file for writing
    connected = opener.open(request)
    meta = connected.info()
    filesize = meta.getheaders("Content-Length")[0]
    size_local = fh.tell()
    print 'filesize',filesize
    print 'size_local',size_local
    while int(size_local) < int(filesize):
        blocksize = 100*1024
        bloqueleido = connected.read(blocksize)
        fh.write(bloqueleido)  # read from request while writing to file
        size_local = fh.tell()
        print 'size_local',size_local
    imagen = __temp__ + filename
    xbmc.executebuiltin( "ShowPicture("+imagen+")" )

def run_tube(url):    
    plugintools.log("RunPlugin = "+url)
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')

def run_tube2(params):    
    plugintools.log("RunPlugin = "+repr(params))
    url = params.get("url")
    xbmc.executebuiltin('XBMC.RunScript('+url+')')
    
