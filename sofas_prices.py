import pandas as pd
import matplotlib.pyplot as plt
import re


def analyze_prices(filename='divan_prices.csv'):
    """Анализирует цены: вычисляет среднюю цену и строит гистограмму."""
    try:
        # Укажите разделитель и обработку ошибок парсинга
        df = pd.read_csv(filename, encoding='utf-8', sep=',', on_bad_lines='skip')

        # Предварительная обработка столбца 'Price'
        def clean_price(price_str):
            # Удаляем все символы, кроме цифр
            price_str = re.sub(r'\D', '', str(price_str))
            # Преобразуем в целое число, если строка не пустая, иначе возвращаем NaN
            return int(price_str) if price_str else None

        df['Price'] = df['Price'].apply(clean_price)

        # Преобразуем столбец 'Price' в числовой формат
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        # Удаляем строки с пропущенными значениями в столбце 'Price'
        df.dropna(subset=['Price'], inplace=True)

        if df.empty:
            print("CSV файл пуст или не содержит данных о ценах после обработки.")
            return

        average_price = df['Price'].mean()
        print(f"Средняя цена дивана: {average_price:.2f}")

        # Гистограмма цен
        plt.figure(figsize=(10, 6))
        plt.hist(df['Price'], bins=30, color='skyblue', edgecolor='black')
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Цена')
        plt.ylabel('Количество')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при анализе данных: {e}")

    analyze_prices()
