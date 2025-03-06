import numpy as np
import matplotlib.pyplot as plt

# Количество точек данных
num_points = 5

# Генерация двух наборов случайных данных
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Создание диаграммы рассеяния
plt.figure(figsize=(8, 6))  # Устанавливаем размер графика
plt.scatter(x, y, c='red', marker='o', label='Случайные точки')

# Настройка графика
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('Значения по оси X')
plt.ylabel('Значения по оси Y')
plt.grid(True)  # Включаем сетку

plt.show()