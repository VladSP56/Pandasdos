from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Опции для работы с Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
chrome_options.add_argument("--no-sandbox")  # Для Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Для Linux

# Путь к chromedriver, если он не в PATH
service = Service('/path/to/chromedriver')  # Замените '/path/to/chromedriver' на путь к вашему chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL страницы для парсинга
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

# Загружаем страницу
driver.get(url)

# Задержка для загрузки страницы (возможно, потребуется увеличение)
time.sleep(5)

# Ищем элементы с ценами
prices = driver.find_elements(By.CLASS_NAME, 'c6e8ba-0')  # Меняйте класс в зависимости от актуальных классов на сайте

# Извлекаем и выводим цены
price_list = []
for price in prices:
    price_list.append(price.text)

# Закрываем драйвер
driver.quit()

# Выводим список цен
for i, price in enumerate(price_list, start=1):
    print(f"{i}. {price}")