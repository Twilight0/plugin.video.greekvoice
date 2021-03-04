# -*- coding: utf-8 -*-

'''
    Greek Voice Addon
    Author Twilight0

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
'''

import json
from sys import argv
from tulip import control, directory, client
from tulip.compat import parse_qsl
from youtube_registration import register_api_keys
from zlib import decompress
from base64 import b64decode
from os import path

sysaddon = argv[0]
syshandle = int(argv[1])
params = dict(parse_qsl(argv[2][1:]))
action = params.get('action')
url = params.get('url')


lc = [
    {
        'title': 'Greek Voice',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV1_icon.png'),
        'url': 'http://wpso.com:1936/hls/wzra.m3u8',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_TV1_fanart.jpg'),
        'plot': u'Greek Voice 1'
    }
    ,
    # {
    #     'title': 'Greek Voice 2',
    #     'icon': join(addonmedia, 'GV2_icon.png'),
    #     'url': 'http://stream.ssh101.com:1935/live/greekvoice/playlist.m3u8',
    #     'fanart': join(addonmedia, 'GV_TV2_fanart.jpg'),
    #     'plot': u'Greek Voice 2'
    # }
    # ,
    {
        'title': 'TILEMOUSIKI 1 SD',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='TILEMOUSIKI1SD.png'),
        'url': 'mmsh://wpso.com:200/music',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg'),
        'plot': u'Εκπέμπει Παλαιά Τραγούδια και κονσέρτα σε ποιότητα SD'
    }
    ,
    {
        'title': 'TILEMOUSIKI 2 HD',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='TILEMOUSIKI2HD.png'),
        'url': 'http://wpso.com:1936/hls/music.m3u8',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg'),
        'plot': u'Μουσικό κανάλι εκπέμπει 24/7 σε σύστημα HD'
    }
    ,
    {
        'title': 'WZRA KIDS 1',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='WZRA_KIDS_icon.png'),
        'url': 'mmsh://wpso.com:200/kids',
        'fanart': control.addonInfo('fanart'),
        'plot': u'Παιδικό Κανάλι 24/7'
    }
    ,
    {
        'title': 'WZRA KIDS 2',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='WZRA_KIDS_icon.png'),
        'url': 'http://wpso.com:1936/hls/kidshd.m3u8',
        'fanart': control.addonInfo('fanart'),
        'plot': u'Παιδικό Κανάλι 24/7'
    }
    ]


rc = [
    {
        'title': 'WPSO Greek Voice Radio',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='wpso_icon.png'),
        'url': 'http://wpso.com:8000/',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_Radio_fanart.jpg'),
        'plot': u'Ραδιοφωνικός σταθμός Φωνή Των Ελλήνων, παγκοσμία κάλυψη'
    }
    ,
    {
        'title': 'WXYB Radio GR IT ES',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='wxyb_icon.png'),
        'url': 'http://wpso.com:7071/',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_Radio_fanart.jpg'),
        'plot': 'Radio WXYB 1520Khz Greek Italian & Spanish'
    }
    ,
    {
        'title': 'XAMOS Youth Radio',
        'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='xamos_icon.png'),
        'url': 'http://xamosam.com:9050',
        'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='xamos_fanart.jpg'),
        'plot': 'XAMOS Youth Radio 1500 KHz AM'
    }
]

channel_id = 'UC0HzJJlSxjhhN4OAXHHQIOg'
SCRAMBLE = (
            'eJwVy80KgjAAAOBXkZ1TdCrTbmIhogVhYHUR24Yzl1ubP1n07uH9+75AU6zoALYGaNLkUJ6YyXEWeTebDZdsHqGHwcYAtWyrji4ri9JPXS'
            'yxSooS7eTcPsg9z0O2XI/v86vak1HESPBgXS1ZA7Rtzw2RGyAfmRPjyPFdSBWRsCGOpoSzafJF1wVKt8SqpdRWI0TD6aipwqIfaD9YWDzB'
            '7w/HIjj4'
        )

# Build Root Menu:
def main_menu():

    menu = []

    menu_items = [
            {
                'title': control.lang(30001),
                'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='television.png'),
                'url': '{0}?action={1}'.format(sysaddon, 'live'),
                'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_TV2_fanart.jpg')
            }
            ,
            {
                'title': control.lang(30002),
                'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='radio.png'),
                'url': '{0}?action={1}'.format(sysaddon, 'radio'),
                'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg')
            }
            ,
            {
                'title': control.lang(30014),
                'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_YT_icon.png'),
                'url': 'plugin://plugin.video.youtube/channel/{0}/?addon_id={1}'.format(channel_id, control.addonInfo('id')),
                'fanart': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='GV_TV2_fanart.jpg')
            }
            # ,
            # {
            #     'title': control.lang(30004),
            #     'icon': control.addonmedia(addonid='resource.images.greekvoice.artwork', icon='settings.png'),
            #     'url': '{0}?action={1}'.format(sysaddon, 'settings'),
            #     'fanart': control.addonInfo('fanart')
            # }
    ]

    for item in menu_items:
        li = control.item(label=item['title'])
        li.setInfo('video', {'title': item['title']})
        li.setArt({'fanart': item['fanart'], 'icon': item['icon'],'thumb': item['icon']})
        _url = item['url']
        if item['url'].endswith('settings'):
            _isFolder = False
        else:
            _isFolder = True
        menu.append((_url, li, _isFolder))

    control.addItems(syshandle, menu)
    control.directory(syshandle)


def constructor(channels):

    menu = []

    for item in channels:

        li = control.item(label=item['title'], iconImage=item['icon'], thumbnailImage=item['icon'])
        li.setInfo('video', {'title': item['title'], 'plot': item['plot']})
        li.setArt({'fanart': item['fanart'], 'icon': item['icon'],'thumb': item['icon']})
        li.setProperty('IsPlayable', 'true')
        _url = '{0}?action=play&url={1}'.format(sysaddon, item['url'])
        _isFolder = False
        menu.append((_url, li, _isFolder))

    control.addItems(syshandle, menu)
    control.directory(syshandle)


def txt_box(heading, announce):

    window_id = 10147
    control_id1 = 1
    control_id2 = 5
    gui_window = control.window(window_id)

    control.execute('ActivateWindow(%d)' % window_id)
    control.sleep(200)

    gui_window.getControl(control_id1).setLabel(heading)

    gui_window.getControl(control_id2).setText(announce)


def guide():

    raw = client.request('http://pastebin.com/raw/8euL4fNM')

    txt_box('Greek Voice TV Guide', raw)


def keys_registration():

    filepath = control.transPath(
        control.join(control.addon('plugin.video.youtube').getAddonInfo('profile'), 'api_keys.json')
    )

    setting = control.addon('plugin.video.youtube').getSetting('youtube.allow.dev.keys') == 'true'

    if path.exists(filepath):

        f = open(filepath)

        jsonstore = json.load(f)

        no_keys = control.addonInfo('id') not in jsonstore.get('keys', 'developer').get('developer')

        if setting and no_keys:

            keys = json.loads(decompress(b64decode(SCRAMBLE)))

            register_api_keys(control.addonInfo('id'), keys['api_key'], keys['id'], keys['secret'])

        f.close()


if action is None:

    main_menu()

elif action == 'live':

    constructor(lc)

elif action == 'radio':

    constructor(rc)

elif action == 'play':

    directory.resolve(url)

elif action == 'guide':

    guide()

elif action == 'settings':

    control.openSettings()

if __name__ == '__main__':

    keys_registration()
