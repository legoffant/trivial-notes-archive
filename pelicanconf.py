#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Anthony Le Goff'
SITENAME = 'Trivial notes'
SITEURL = ''
THEME = "themes/pelican-themes/new-bootstrap2"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Ajout dossier d'accès aux images
STATIC_PATHS = ['img']

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Apprendre le C en 20H', 'https://framabook.org/le-c-en-20-heures-2/'),
         ('Arch Linux', 'https://archlinux.org/'),
         ('Blackarch', 'https://www.blackarch.io/'),
         ('Kernel', 'https://www.kernel.org/'),
         ('Arduino', 'https://www.arduino.cc/'),
         ('BeagleBoard', 'https://beagleboard.org/bone'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/legoffant'),
       ('Twitter', 'https://twitter.com/anth_lg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}