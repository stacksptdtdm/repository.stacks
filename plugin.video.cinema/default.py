

import xbmc, xbmcgui, xbmcplugin
import os, urllib, os
import re, urllib2


HOME         = xbmc.translatePath('special://home')
regex1       = os.path.join(HOME,'regex1.txt')
regex2       = os.path.join(HOME,'regex2.txt')
regexonline  = 'https://archive.org/download/regex2/regex1.txt'

# xbmcpligin.setContent(addon_handle, 'movies')

# player       = xbmcgui.Player()
video1       = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Ghost%20in%20The%20Shell/Ghost%20in%20the%20Shell.2017.1080p.mkv'
video2       = 'http://dl.dlfile.pro/6/Movie%20HD/Despicable.Me.3.2017.720p.x265.RMT.mkv'
video3       = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Wonder%20Woman/Wonder%20Woman.2017.HDRip.720p.mkv'
video4       = 'http://dl.dlfile.pro/6/Movie%20HD/Transformers.The.Last.Knight.2017.HDRip.720p.MkvCage.mkv'
icon1        = 'https://initiate.alphacoders.com/images/854/cropped-985-1500-854786.jpg?5258'
icon2        = 'https://initiate.alphacoders.com/images/853/cropped-985-1500-853982.jpg?7785'
icon3        = 'https://initiate.alphacoders.com/images/812/cropped-985-1500-812454.png?4707'
icon4        = 'https://initiate.alphacoders.com/images/869/cropped-985-1500-869850.jpg?9393'
addon_handle = int(sys.argv[1])

def addDir(url, title, icon, fanart):
    li = xbmcgui.ListItem(title, iconImage=icon)
    li.setProperty( "Fanart_Image", fanart )
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

def read_file(filename):
    readfile = open(filename, 'r')
    content  = readfile.read()
    readfile.close()
    return content


def Open_URL(url):
   req = urllib2.Request(url)
   req.add_header('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; Windows NT 5.1; en-GB; rv:1.9.0.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 Gecko/2008092417 Firefox/3.0.3')
   response    =   urllib2.urlopen(req)
   link        =   response.read()
   response.close()
   return link.replace('\n', '').replace('\t', '').replace('\r', '')

# content     = read_file(regex1)
content    = Open_URL(regexonline)
xbmc.log('#### CONTENTS: %s' % content)
matches    = re.compile('name="(.+?)"path="(.+?)"thumb="(.+?)"fanart="(.+?)"').findall(content)
for item in matches:
    name   = item[0]
    path   = item[1]
    thumb  = item[2]
    fanart = item[3]
    addDir(title = name, icon = thumb, url = path, fanart = fanart)


# matches    = re.compile('name="(.+?)"\npath="(.+?)"\nthumb="(.+?)"\nfanart="(.+?)"').findall(content)


# matches    = re.compile('name="(.+?)"').findall(content)
# xbmc.log(str(matches))


# addDir(video1, 'GHOST IN THE SHELL', icon1)
# addDir(video2, 'DESPICABLE ME 3', icon2)
# addDir(video3, 'WONDER WOMAN', icon3)
# addDir(video4, 'TRANSFORMERS THE LAST KNIGHT', icon4)   

xbmcplugin.endOfDirectory(addon_handle)




# li = xbmcgui.ListItem('DESPICABLE ME 3', iconImage='DefaultVideo.png')
# xbmcplugin.addDirectoryItem(handle=addon_handle, url=video2, listitem=li)

# li = xbmcgui.ListItem('WONDER WOMAN', iconImage='DefaultVideo.png')
# xbmcplugin.addDirectoryItem(handle=addon_handle, url=video3, listitem=li)

# li = xbmcgui.ListItem('TRANSFORMERS THE LAST KNIGHT', iconImage='DefaultVideo.png')
# xbmcplugin.addDirectoryItem(handle=addon_handle, url=video4, listitem=li)







# dialog = xbmcgui.Dialog()
# video = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Ghost%20in%20The%20Shell/Ghost%20in%20the%20Shell.2017.1080p.mkv'
# video = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Despicable%20Me%203/Despicable%20Me%203.2017.TS.mkv'
# video = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Wonder%20Woman/Wonder%20Woman.2017.HDRip.720p.mkv'
# video = 'http://mc1.dl3enter.in/files/d2/Movie/2017/Transformers%20The%20Last%20Knight/Transformers%20The%20Last%20Knight.2017.HDTC.720p.mkv'
# video = ''
# video =
# video =
# video =
# video =
# video =
# icon =
# icon =
# icon =
# icon =
# icon =
# icon =
# icon =
# icon =
# icon =
# icon =


# dialog.ok('GREEN OR RED PILL','THIS IS A TEST, CLICK OK TO CONTINUE')
# choice = dialog.yesno('PLAY MOVIE?','DO YOU WANT TO WATCH THE MOVIE?',yeslabel='HELL YEAH!!', nolabel='HELL NO!!')
# if choice == 1:
#     dialog.ok('CONTINUE','YOU PRESSED:', '[COLOR=green]CONTINUE[/COLOR]')
#     xbmc.Player().play(video)    
# else:
#     dialog.ok('CONTINUE','YOU PRESSED:', '[COLOR=red]STOP[/COLOR]')
