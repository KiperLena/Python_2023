import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('food.csv', 'a') as f:
        writer = csv.writer(f, delimiter=";", lineterminator='\r')

        writer.writerow((data['name'], data['url'], data['like']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    f1 = soup.find_all('div', class_='row-span')[1]
    foods = f1.find_all('div', class_='span-4')

    for food in foods:
        name = food.find('div', class_='recept-item-in').find('h4').text
        url = "https://gotovim-doma.ru" + food.find('div', class_='recept-item-in').find("a")['href']
        like = food.find('span', class_='recept-info').find('span').text
        data = {'name': name, "url": url, "like": like}
        write_csv(data)


def main():
    url = 'https://gotovim-doma.ru/category/17-salaty'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

