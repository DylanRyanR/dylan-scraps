import re

import requests
from bs4 import BeautifulSoup

import liuli_scrap


def get_magnet_link(text):
    pattern = r'[0-9a-zA-Z]{40}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

# 获取解析详情
def get_liuli_info(soup):
    item = {}
    all_content = ''
    bt_link = ''
    articles = soup.find('div', id='main')
    if articles != ''  and articles is not None:
        content = articles.find('div', class_='entry-content')
        if content != '' and content is not None:
            p_list = content.find_all('p')
            for p in p_list:
                all_content = all_content + p.text
                link = get_magnet_link(p.text)
                if link is not None:
                    bt_link = link
    print(bt_link)
    print(all_content)
    item = {'btLink': bt_link, 'allContent': all_content}
    return item


if __name__ == '__main__':
    url = 'https://hacg.uno/wp/all/anime/%e3%80%90%e7%94%9f%e8%82%89%e3%80%91ova-%e3%81%bf%e3%81%a0%e3%82%8c%e3%81%86%e3%81%a1-%ef%bc%832/'
    soup = liuli_scrap.get_request_content(url=url)
    if soup != '' or soup is not None:
        get_liuli_info(soup=soup)
    else:
        print("未查询到相关内容")

    # print(get_magnet_link('0e6180cz57090f8088f6aa4a48d305220d3a936c'))


