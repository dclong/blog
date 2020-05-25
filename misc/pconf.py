#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
from pelican_jupyter import markup as nb_markup
#-------------------------------------------------------------------------
# !!! http:// is necessary
HOME_URL = "http://www.legendu.net"
SITEURL = os.path.join(HOME_URL, "misc") 
#-------------------------------------------------------------------------
SITESUBTITLE = "It is never too late to learn."
AUTHOR = 'Ben Chuanlong Du'
SITENAME = "Ben Chuanlong Du's Blog"
# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
#-------------------------------------------------------------------------
PATH = Path(__file__).resolve().parent
BLOG_DIR = PATH.parent
DELETE_OUTPUT_DIRECTORY = True

# pages
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False

# Set the article URL
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Title menu options
MENUITEMS = [
    ('Home', HOME_URL),
    ('Blog', SITEURL), 
    ("Archives", os.path.join(SITEURL, 'archives.html')), 
    ('Links', os.path.join(SITEURL, 'pages/links.html')), 
]
NEWEST_FIRST_ARCHIVES = True

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

#Github include settings
GITHUB_USER = 'dclong'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/ben-chuanlong-du-1239b221/'),
    ('Twitter', 'https://twitter.com/longendu'),
    ('Facebook', 'https://www.facebook.com/chuanlong.du')
)

DEFAULT_PAGINATION = 6

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# This requires Pelican 3.3+
STATIC_PATHS = [
            'images', 
            'figures', 
            'downloads', 
            'favicon.png', 
            'media',
            'CNAME',
            'readme.md',
        ]

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


# theme and plugins
CSS_FILE = 'main_2.css'
THEME = os.path.join(BLOG_DIR, "themes/octopress_2")
# plugins
IPYNB_USE_METACELL = True
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = [os.path.join(BLOG_DIR, 'plugins'), BLOG_DIR / "plugins/ipynb"]
PLUGINS = [
        'latex',
        'nb_markup',
    ]
IGNORE_FILES = [".ipynb_checkpoints"]  

# disqus comment
DISQUS_SITENAME = "dclong"

# Sharing
TWITTER_USER = 'longendu'
GOOGLE_PLUS_USER = 'duchuanlong'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
# FEED_RSS = 


# Search
# SEARCH_BOX = True
# SITESEARCH = "http://www.google.com/search"
# SITESEARCH = "https://search.yahoo.com"
SITESEARCH = "https://www.bing.com/search"

# google analytics
GOOGLE_ANALYTICS = 'UA-30259661-1'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
