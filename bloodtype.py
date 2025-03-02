import chardet

# Открываем файл в бинарном режиме и считываем первые 10000 байтов
with open('blood_type_distribution_by_country.csv', 'rb') as file:
    raw_data = file.read(10000)
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f'Определённая кодировка: {encoding}')

import pandas as pd

# Пример чтения csv
df = pd.read_csv('blood_type_distribution_by_country.csv', encoding='ISO-8859-1')

# Создание списка с длиной, равной количеству строк в DataFrame
df['Test'] = list(range(len(df)))  # Длина списка будет равна количеству строк в df

# Теперь столбец 'Test' будет успешно добавлен
print(df.head())  # Проверка первых нескольких строчек DataFrame

print(df.info())
print(df.describe())
