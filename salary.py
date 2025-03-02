import pandas as pd

# Загрузка данных из файла
df = pd.read_csv('dz.csv', encoding='utf-8')

# Выводим содержимое DataFrame
print("Данные:")
print(df)

# Очистка данных от пустых значений
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # Преобразовать Salary в числовой формат, игнорируя ошибки

# Рассчитываем среднюю зарплату по городу
average_salary = df.groupby('City')['Salary'].mean()

# Выводим результаты
print("\nСредняя зарплата по городу:")
print(average_salary)