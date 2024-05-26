AUTHOR = 'VoidStar Security'
SITENAME = 'VoidStar Security Blog'
SITEURL = 'https://wrongbaud.github.io/newblog'
PLUGIN_PATHS = ['/home/wrongbaud/projects/vss/blog-resources/pelican-plugins', ]
PLUGINS = ['i18n_subsites','pelican_just_table','tag_cloud']
JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
            }

PATH = 'content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

SIDEBAR_ON_LEFT=True
# Blogroll
LINKS = (('VoidStar Security Website', 'https://voidstarsec.com/'),
         ('VoidStar Security Training', 'https://www.voidstarsec.training/'),
        ('Build a Hardware Hacking Lab', 'https://www.voidstarsec.wiki/'),
         ('Free Ghidra Course', 'https://hackaday.io/course/172292-introduction-to-reverse-engineering-with-ghidra'),
         ('Wrongbauds Blog (fun intro hacks)', 'https://www.wrongbaud.github.io/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/voidstarsec'),
          ('linkedin', 'http://www.linkedin.com/in/voidstarsec'),
          ('github', 'http://github.com/voidstarsec'),)

# Uncomment following line if you want document-relative URLs when developing
DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_SIDEBAR=True
DISPLAY_ARTICLE_INFO_ON_INDEX=True
SHOW_ARTICLE_AUTHOR=True
SHOW_ARTICLE_CATEGORY=True
 # journal lumen spacelab
BOOTSTRAP_THEME='spacelab'