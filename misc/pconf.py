#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path
from pelican_jupyter import markup as nb_markup
HOME_URL = "http://www.legendu.net"
SITEURL = f"{HOME_URL}/misc"
SITESUBTITLE = "It is never too late to learn."
AUTHOR = "Ben Chuanlong Du"
SITENAME = "Ben Chuanlong Du's Blog"
DEFAULT_DATE_FORMAT = "%b %d, %Y"
TIMEZONE = "US/Pacific"
DEFAULT_LANG = "en"
DELETE_OUTPUT_DIRECTORY = True

# pages
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False

# Set the article URL
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Title menu options
MENUITEMS = [
    ("Home", HOME_URL),
    ("Blog", SITEURL), 
    ("Archives", f"{SITEURL}/archives.html"),
    ("Links", f"{SITEURL}/pages/links.html"),
]
NEWEST_FIRST_ARCHIVES = True

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

# github include settings
GITHUB_USER = "dclong"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/ben-chuanlong-du-1239b221/"),
    ("Twitter", "https://twitter.com/longendu"),
    ("Facebook", "https://www.facebook.com/chuanlong.du")
)

DEFAULT_PAGINATION = 6

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# This requires Pelican 3.3+
STATIC_PATHS = [
            "images", 
            "figures", 
            "downloads", 
            "favicon.png", 
            "media",
            "CNAME",
            "readme.md",
        ]

CODE_DIR = "downloads/code"
NOTEBOOK_DIR = "downloads/notebooks"

# theme
BLOG_DIR = Path(__file__).resolve().parent.parent
CSS_FILE = "main_2.css"
THEME = BLOG_DIR / "themes/octopress_2"
# plugins
MARKUP = ("md", "ipynb")
PLUGIN_PATHS = [str(BLOG_DIR / "plugins")]
PLUGINS = ["render_math"]
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]  

# disqus comment
DISQUS_SITENAME = "dclong"

# sharing
TWITTER_USER = "longendu"
GOOGLE_PLUS_USER = "duchuanlong"
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = "false"
TWITTER_SHOW_FOLLOWER_COUNT = "true"

# rss/atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = "atom.xml"

SITESEARCH = "https://www.bing.com/search"

# google analytics
GOOGLE_ANALYTICS = "UA-30259661-1"
