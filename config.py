c.colors.webpage.darkmode.enabled 

my_search_engine = 'https://search.brave.com'

c.url.start_pages = [my_search_engine]
c.url.default_page = my_search_engine

c.url.searchengines = {
    'DEFAULT': f'{my_search_engine}/search?q=' + '{}',
    ':g':       'https://www.google.com/search?q={}',
    ':gh':      'https://github.com/search?q={}',
    ':libgen':  'http://libgen.rs/search.php?req={}',
    ':sx':      'https://www.searx.bar/search?q={}',
    ':ub':      'https://www.urbandictionary.com/define.php?term={}',
    ':udemy':       'https://www.udemy.com/courses/search/?src={}',
    ':yt':      'https://www.youtube.com/results?search_query={}',
    ':wiki':       'https://en.wikipedia.org/wiki/{}',
}

# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')

