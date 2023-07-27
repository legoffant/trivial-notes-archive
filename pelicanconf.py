AUTHOR = 'Anthony Le Goff'
SITENAME = 'Trivial notes'
SITEURL = ''
THEME = "themes/pelican-themes/new-bootstrap2"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Kernel', 'https://www.kernel.org/'),
	 ('Proxmox VE', 'https://www.proxmox.com/en/proxmox-virtual-environment/overview'),
	 ('KVM', 'https://www.linux-kvm.org/page/Main_Page',),
         ('Apprendre le C en 20H', 'https://framabook.org/le-c-en-20-heures-2/'),
	 ('Red Language', 'https://www.red-lang.org/'),
         ('Python.org', 'https://www.python.org/'),
         ('Ruby', 'https://www.ruby-lang.org/en/'),
         ('Arch Linux', 'https://archlinux.org/'),
         ('Blackarch', 'https://www.blackarch.io/'),
	 ('Veracrypt', 'https://www.veracrypt.fr/en/Home.html'),
         ('Arduino', 'https://www.arduino.cc/'),
	 ('MangoPi', 'https://mangopi.org/'),
	 ('Sipeed 资料站', 'https://sipeed.com/'),
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