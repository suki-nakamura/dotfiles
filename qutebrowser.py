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
