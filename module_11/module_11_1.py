import matplotlib.pyplot as plt
import numpy as np

f, ax = plt.subplots(2, 2)  # создаем поле 2 на 2 для графиков

f.set_size_inches(7, 4)  # задаем размер 7 на 4 дюйма
f.set_facecolor('#eee')  # задаем цвет фона окна на светло серый

ax[0, 0].plot(np.arange(0, 5, 0.15))  # создаем график с параметрами для оси y: от 0 до 5 с шагом 0.15
ax[0, 0].grid()  # включаем сетку в графике
ax[0, 1].plot(np.arange(10, 5, -0.5))
ax[0, 1].grid()
ax[1, 0].plot(np.arange(2, -4, -0.1))
ax[1, 1].plot(np.arange(2, 8, 0.34))
plt.show()
