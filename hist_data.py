import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))  # Задаем размер фигуры
plt.hist(data, bins=30, density = True, alpha = 0.5, color='blue', edgecolor='black')

plt.title('Гистограмма случайных данных, распределенных по нормальному распределению')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.grid(axis='y', alpha=0.7)

plt.show()