import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('book.csv', 'a', encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";", lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['price'], data['autor'], data['autor_url']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    element = soup.find_all('div', class_='row book-item')
    for el in element:
        try:
            name = el.find('div', class_='col-xs-7').find('a').text
        except ValueError:
            name = ''

        try:
            url = "https://litnet.com" + el.find('a').get('href')
        except ValueError:
            url = ''

        try:
            price = el.find('div', class_='item-price').find('span').text.strip()
        except ValueError:
            price = ''

        try:
            autor = el.find('div', class_='col-xs-7').find('p').text
        except ValueError:
            autor = ''


        try:
            autor_url = "https://litnet.com" + el.find('p', class_='author-wr').find('a').get('href')
        except ValueError:
            autor_url = ''

        data = {
            'name': name,
            'url': url,
            'price': price,
            'autor': autor,
            'autor_url': autor_url
        }
        write_csv(data)


def main():
    for i in range(1, 20):
        url = f'https://litnet.com/ru/top/fantastika?alias=fantastika&page={i}'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
