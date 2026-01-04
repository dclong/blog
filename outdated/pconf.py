#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path
from pelican_jupyter import markup as nb_markup
from loguru import logger

HOME_URL = "https://www.legendu.net"
SITEURL = "https://outdated.legendu.net"
SITESUBTITLE = "Change is eternal."
AUTHOR = "Ben Chuanlong Du"
SITENAME = "Ben Chuanlong Du's Blog"
DEFAULT_DATE_FORMAT = "%b %d, %Y"
TIMEZONE = "US/Pacific"
DEFAULT_LANG = "en"
USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
MAIN_MENU = True
GITHUB_CORNER_URL = "https://github.com/dclong/outdated"
# BROWSER_COLOR = "#333333"
logger.debug("Site URL: {}", SITEURL)

# pages
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False

# set the article URL
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

# title menu options
MENUITEMS = (
    ("Home", HOME_URL),
    ("Blog", SITEURL),
    ("Archives", f"{SITEURL}/archives.html"),
    ("Categories", f"{SITEURL}/categories.html"),
    ("Tags", f"{SITEURL}/tags.html"),
    ("About", f"{HOME_URL}/pages/about"),
)
NEWEST_FIRST_ARCHIVES = True
ARTICLE_ORDER_BY = "reversed-modified"

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

# github include settings
GITHUB_USER = "legendu-net"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/ben-chuanlong-du-1239b221/"),
    ("github", "https://github.com/legendu-net/"),
    (
        "stack-overflow",
        "https://stackoverflow.com/users/7808204/benjamin-du?tab=profile",
    ),
    ("docker", "https://hub.docker.com/u/dclong"),
    ("twitter", "https://twitter.com/longendu"),
)

DEFAULT_PAGINATION = 6

STATIC_PATHS = [
    "images",
    "figures",
    "downloads",
    "favicon.png",
    "media",
    "CNAME",
    "ads.txt",
    "readme.md",
]
CODE_DIR = "downloads/code"
NOTEBOOK_DIR = "downloads/notebooks"

# theme and plugins
BLOG_DIR = Path(__file__).resolve().parent.parent
# CSS_FILE = "main_2.css"
THEME = BLOG_DIR / "themes/Flex"

# plugins
# PLUGINS = ["render_math"]
# jupyter
MARKUP = ("md", "ipynb")
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]
# mathjax
MATH_JAX = {
    "auto_insert": True,
    "tex_extensions": ["color.js", "mhchem.js"],
}

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

FEED_ALL_ATOM = None
# rss/atom feeds
# FEED_DOMAIN = SITEURL
# FEED_ATOM = "atom.xml"

DIRECT_TEMPLATE = ["search"]
# SEARCH_URL = "search"

# google analytics
MODERN_GOOGLE_ANALYTICS = "G-3STS9BVPF6"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = True
