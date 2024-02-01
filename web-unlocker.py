import sys
import ssl
from personalurl import Personnal

ssl._create_default_https_context = ssl._create_unverified_context
url="https://codeavecjonathan.com/scraping/techsport"

import urllib.request
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler(
        {'http': Personnal.url,
        'https': Personnal.url}))

html=opener.open(url).read().decode('utf-8')
f=open('web-unlocker.html','w')
f.write(html)
f.close()