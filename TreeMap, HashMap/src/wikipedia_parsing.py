"""parsing wiki"""
from urllib.request import urlopen
import re
from src.hash_map import HashMap

WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
WIKI_DOMAIN = "https://ru.wikipedia.org"
hash_map = HashMap(50)
response = urlopen(WIKI_RANDOM)
response_bytes = response.read()
txt = response_bytes.decode("utf8")
urls = re.findall(r'href=[\'"]?([^\'" >]+)', response_bytes.decode("utf8"))
filtered_urls = filter(lambda url: url.startswith('/wiki/'), urls)
corrected_urls = map(lambda url: WIKI_DOMAIN + url, filtered_urls)
words = list(map(lambda s: s.lower().strip(), filter(lambda s: s.isalpha(), txt.split())))

for i in words:
    if hash_map[i] is None:
        hash_map[i] = 0
    hash_map[i] += 1
print(hash_map)
