import matplotlib.pyplot as plt
import numpy as np

departments = ["Accounting", "Marketing", "IT", "Academic"]
employees_2024 = [5, 20, 8, 50]
employees_2025 = [6, 23, 10, 65]
color1 = ['blue', 'red', 'green', 'yellow']
color2 = ['lightblue', 'orange', 'lightgreen', 'gold']

x = np.arange(len(departments))
width = 0.4

fig, axs = plt.subplots(2,2, figsize=(10,10))
fig.suptitle('Analysis of Employees per departments', fontsize=18)

axs[0,0].barh(departments, employees_2024, color='orange', edgecolor='black')
axs[0,0].set_title('Employees allocation 2024')
axs[0,0].set_xlabel('Number of Employees')
axs[0,0].set_ylabel('Departments')
axs[0,0].grid(axis='x', linestyle = '--', alpha = 0.7)
for i, val in enumerate(employees_2024):
    axs[0,0].text(val + 0.3, i, str(val), va='center')  # right of bar



axs[0,1].bar(departments, employees_2024, color='lightblue', edgecolor='black')
axs[0,1].set_title('Employees allocation 2024')
axs[0,1].set_xlabel('Departments')
axs[0,1].set_ylabel('Number of Employees')
axs[0,1].grid(axis='x', linestyle = '--', alpha = 0.7)
for i, val in enumerate(employees_2024):
    axs[0,1].text(i, val + 0.5, str(val), ha='center')

axs[1,0].bar(departments, employees_2024, color=color1, edgecolor='black')
axs[1,0].set_title('Employees allocation 2024')
axs[1,0].set_xlabel('Departments')
axs[1,0].set_ylabel('Number of Employees')
axs[1,0].grid(axis='x', linestyle = '--', alpha = 0.7)
for i, val in enumerate(employees_2024):
    axs[1,0].text(i, val + 0.5, str(val), ha='center')

axs[1,1].bar(x - width/2, employees_2024, color=color1, edgecolor='black', width=width, label='2024')
axs[1,1].bar(x + width/2, employees_2025, color=color2, edgecolor='black', width=width, label='2025')
axs[1,1].set_xticks(x)
axs[1,1].set_xticklabels(departments)
axs[1,1].set_title('Employees Comparison')
axs[1,1].set_xlabel('Departments')
axs[1,1].set_ylabel('Number of Employees')
axs[1,1].legend()
axs[1,1].grid(axis='y', linestyle = '--', alpha = 0.7)
for i in range(len(departments)):
    # Week 2024 bars
    axs[1,1].text(x[i]-width/2, employees_2024[i]+0.5, '2024', ha='center')
    # Week 2025 bars
    axs[1,1].text(x[i]+width/2, employees_2025[i]+0.5, '2025', ha='center')


fig.subplots_adjust(top=0.9, hspace=0.4, wspace=0.3)
plt.show()