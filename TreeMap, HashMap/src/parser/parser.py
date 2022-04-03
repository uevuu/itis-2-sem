"""parsing wiki"""
import requests
from bs4 import BeautifulSoup as BS
from src.maps.hash_map import HashMap


def url_in_urls(url: str):
    """checks for links in a file with links"""
    with open('urls.txt', 'r', encoding="utf-8") as file:
        order_set = set(file.readlines())
    if url + '\n' in order_set:
        return True
    return False


def add_url_in_urls(url: str):
    """adding a link to a file with links"""
    if url_in_urls(url):
        print('Такая ссылка уже есть')
        return False
    with open('urls.txt', 'a', encoding="utf-8") as file:
        file.write(url + '\n')
        return True


def write_map_in_file(url: str):
    """write map in file"""
    hash_map = HashMap(100)
    req = requests.get(url)
    soup = BS(req.content, 'html.parser')
    if add_url_in_urls(req.url):
        all_a = soup.find_all('a')
        for element in all_a:
            element_text = element.text
            if 'https://ru.wikipedia.org/w/index.php?title=' not in element_text:
                if hash_map[element_text] is None:
                    hash_map[element_text] = 0
                hash_map[element_text] += 1
        wiki_title = soup.find(id="firstHeading").string.replace(' ', '') + '.txt'
        hash_map.write(wiki_title)


WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
write_map_in_file(WIKI_RANDOM)
