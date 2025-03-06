import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/moskva/divany'


def get_max_page():
    resp = requests.get(url).text
    soup = bs(resp, 'lxml')

    pagination_items = soup.find_all('a', class_="pagination__item")

    if pagination_items:
        last_page_number = pagination_items[-1].text
        max_page = int(last_page_number)
    else:
        # Если элементы пагинации не найдены, предполагаем, что страница всего одна
        max_page = 1

    return max_page


def get_info_about_divans(max_page):
    page_number = 1
    all_info = []

    while page_number <= max_page:
        url_page = url + f'?page={page_number}'
        resp = requests.get(url_page).text
        soup = bs(resp, 'lxml')

        divans_list = soup.find_all('div', class_="product-card")

        for divan in divans_list:
            try:
                title = divan.find('span', class_="product-card__title").text
                price_str = divan.find('span', class_="product-card__price-new").text
                price = int(re.sub(r'[^0-9]', '', price_str))
                link = 'https://www.divan.ru' + divan.find('a', class_='product-card__image-link')['href']

                all_info.append([title, price, link])

            except:
                pass  # Обработка исключений

        if page_number % 5 == 0:
            print(f'Парсинг страницы {page_number}')

        page_number += 1

    return all_info


def to_csv(all_info):
    df = pd.DataFrame(all_info, columns=['Title', 'Price', 'Link'])
    df.to_csv('divan_prices.csv', index=False, encoding='utf-8')
    print("Данные успешно сохранены в divan_prices.csv")


max_page = get_max_page()
all_info = get_info_about_divans(max_page)
to_csv(all_info)

# Чтение данных из CSV файла
df = pd.read_csv('divan_prices.csv', encoding='utf-8')

# Обработка данных: удаление строк с пропущенными значениями и преобразование типов
df.dropna(inplace=True)  # Удаляем строки с отсутствующими значениями
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Преобразуем цены в числа
df.dropna(subset=['Price'], inplace=True)  # Удаляем строки с некорректными ценами

# Вычисление средней цены
average_price = df['Price'].mean()
print(f"Средняя цена дивана: {average_price:.2f}")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)
plt.show()