import pandas as pd
from unicodedata import numeric

# Создание DataFrame с данными
data = {
    'Ученик': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
               'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [5, 4, 3, 5, 4, 2, 3, 5, 4, 3],
    'Русский язык': [4, 5, 5, 3, 4, 2, 5, 5, 4, 3],
    'История': [3, 4, 4, 5, 4, 3, 5, 4, 5, 2],
    'Физика': [4, 4, 3, 5, 5, 3, 4, 3, 4, 3],
    'Иностранный язык': [5, 3, 4, 5, 4, 2, 3, 4, 5, 4]
}
df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())
# Вычисление средней оценки по каждому предмету
average_scores = df.mean(numeric_only=True)
print("nСредняя оценка по каждому предмету:")
print(average_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("nМедианная оценка по каждому предмету:")
print(median_scores)

#Вычисление Q1 и Q3 для оценки по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:",Q3_math)

# Рассчет IQR
IQR_math = Q3_math - Q1_math
print("IQR для оценок по математике:", IQR_math)

# Вычисление стандартного отклонения по каждому предмету
std_deviation = df.std(numeric_only=True)
print("nСтандартное отклонение по каждому предмету:")
print(std_deviation)

