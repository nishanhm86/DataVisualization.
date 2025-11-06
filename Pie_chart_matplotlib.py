import matplotlib.pyplot as plt

departments = ["Finance", "Trading", "Personal Banking" ]
turnover = [125, 500, 350]
color = ['blue', 'red', 'green']
explode = [0.05, 0.05, 0.05]


plt.pie(turnover, labels=departments, colors = color, autopct='%1.1f%%', startangle=90, shadow=True, explode = explode)
plt.axis('equal')
plt.title("Turnover of each department")

plt.show()