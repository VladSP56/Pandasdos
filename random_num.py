import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))  # Установка размера фигуры
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)  # Рисуем гистограмму
plt.title('Гистограмма случайных данных с нормальным распределением')  # Заголовок
plt.xlabel('Значения')  # Подпись по оси X
plt.ylabel('Частота')  # Подпись по оси Y
plt.grid(axis='y', alpha=0.75)  # Добавление сетки
plt.show()  # Отображение гистограммы