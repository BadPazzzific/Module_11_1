import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 4, 8, 16]
y = [1, 3, 9, 27, 81]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

import requests

response = requests.get('https://api.github.com')

print(response.json())  # Печатает JSON-ответ от GitHub API
print("\n код requests завершён \n")

