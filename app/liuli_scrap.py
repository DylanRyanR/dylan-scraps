import requests
from bs4 import BeautifulSoup


# 提取内容
def get_request_content(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# 提取列表内容
def get_news_list(soup):
    articles = soup.find_all('article')

    info_list = []

    for article in articles:
        title = article.find('h1', class_='entry-title')
        if title is None:
            continue
        title = title.text
        publish_time = article.find('time', class_='entry-date').text
        author = article.find('span', class_='author vcard').text
        image_origin = article.find('img')
        image = ''
        if image_origin is not None:
            image = image_origin['src']
        description = article.find('div', class_='entry-content').text
        cat = ''
        cat_origin = article.find('span', class_='cat-links')
        if cat_origin is not None:
            cat = cat_origin.find('a').text
        tag = []
        tag_origin = article.find('span', class_='tag-links')
        if tag_origin is not None:
            tag = [x.text for x in tag_origin.find_all('a')]
        link = article.find('a', class_='more-link')['href']

        print('标题:', title)
        print('发布时间:', publish_time)
        print('发布人:', author)
        print('图片链接:', image)
        print('文字描述:', description)
        print('分类：', cat)
        print('标签：', tag)
        print('跳转链接:', link)
        print('\n')

        info_item = {'title': title, 'publishTime': publish_time, 'author': author, 'imgLink': image, 'desc': description, 'cat': cat, 'tags': tag, 'infoLink': link}
        info_list.append(info_item)

    return info_list


if __name__ == '__main__':
    url = 'https://hacg.uno/wp/'
    soup = get_request_content(url=url)
    if soup != '' or soup is not None:
        get_news_list(soup=soup)
    else:
        print("未查询到相关内容")