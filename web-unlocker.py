import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url="https://codeavecjonathan.com/scraping/techsport"

import urllib.request
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler(
        {'http': 'http://brd-customer-hl_fb6b9e4a-zone-unblocker:wlh54hu6udp9@brd.superproxy.io:22225',
        'https': 'http://brd-customer-hl_fb6b9e4a-zone-unblocker:wlh54hu6udp9@brd.superproxy.io:22225'}))
print(opener.open('http://lumtest.com/myip.json').read())