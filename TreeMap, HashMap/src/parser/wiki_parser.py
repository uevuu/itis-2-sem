"""parsing wiki"""
import re
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup as BS
from src.maps.hash_map import HashMap


def url_in_urls(url: str) -> bool:
    """checks for links in a data with links"""
    with open('urls.txt', 'r', encoding="utf-8") as file:
        if url + '\n' in set(file.readlines()):
            return True
    return False


def write_list_in_file(path: str, list_: list) -> None:
    """write list in file"""
    with open(path, 'w+', encoding="utf-8") as file:
        for element in list_:
            key, value = element[0], element[1]
            file.write(f"{key}: {value}\n")


def get_sorted_list_from_hashmap(hash_map: HashMap) -> list:
    """get sorted list from hashmap"""
    words = []
    for element in hash_map:
        words.append(element)
    words.sort(key=lambda x: x[0])
    return words


def add_url_in_urls(url: str) -> bool:
    """adding a link to a data with links"""
    if url_in_urls(url):
        print('Такая ссылка уже есть')
        return False
    with open('urls.txt', 'a', encoding="utf-8") as file:
        file.write(url + '\n')
        return True


def get_links(url: str) -> list:
    """gets all links"""
    wiki_damain = 'https://ru.wikipedia.org'
    req = requests.get(url)
    soup = BS(req.content, 'html.parser')
    result = set()
    for link_info in soup.find(name='div', attrs={'class': 'mw-body-content mw-content-ltr'}). \
            find_all('a', href=True):
        link = link_info.get('href')
        if check_url(link):
            result.add(wiki_damain + link)
    return list(result)


def check_url(url: str) -> bool:
    """checks the link click"""
    bad_endings = ['png', 'jpg', 'gif', 'pdf']
    if (not url.startswith('/wiki/')) or (url[-3:] in bad_endings) \
            or (url.endswith('#identifiers')) or \
            ('edit&section' in url) or (':' in url):
        return False
    return True


def wiki_parsing(url: str) -> list:
    """parsing wiki"""
    hash_map = HashMap(100)
    req = requests.get(url)
    soup = BS(req.content, 'html.parser')
    title_name = soup.find(name='h1', attrs={'class': 'firstHeading mw-first-heading'}).text
    p_text = list(
        map(lambda x: re.sub(r'[^a-zA-Zа-яА-Я0-9-]+', ' ', x.text),
            soup.find(name='div', attrs={'class': 'mw-body-content mw-content-ltr'}).find_all('p')))
    if add_url_in_urls(req.url):
        for text in p_text:
            for word in text.split():
                if hash_map[word] is None:
                    hash_map[word] = 0
                hash_map[word] += 1
        # это если хотим записать не сортированные слова
        # hash_map.write('data/' + title_name + '.txt')
        list_from_map = get_sorted_list_from_hashmap(hash_map)
        write_list_in_file('data/' + title_name + '.txt', list_from_map)

    return get_links(req.url)


def multi_parsing(url: str, mode: ThreadPoolExecutor or Pool, depth: int = 1) -> None:
    """multi parsing"""
    if mode is ThreadPoolExecutor or mode is Pool:
        urls_to_pars = [[url]]
        for _ in range(depth):
            urls_to_pars = [new_url for urls in urls_to_pars for new_url in urls]
            with mode(30) as executor:
                urls_to_pars = executor.map(wiki_parsing, urls_to_pars)


if __name__ == '__main__':
    WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
    multi_parsing(WIKI_RANDOM, ThreadPoolExecutor, 2)
