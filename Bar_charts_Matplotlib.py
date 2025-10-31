import matplotlib.pyplot as plt
import numpy as np

#horizontal bar chart
department = ["Cardiology", "Maternity", "OPD"]
patients =[ 35, 10, 76]

plt.barh(department, patients, color='blue')

plt.title("Number of Patients per Department(Horizontal Bar Chart)")
plt.xlabel("Number of Patients")
plt.ylabel("Department")

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

#vertical bar chart
department = ["Cardiology", "Maternity", "OPD"]
patients =[ 35, 10, 76]

plt.bar(department, patients, color='orange')

plt.title("Number of Patients per Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")


plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

#multicolored bar chart
department = ["Cardiology", "Maternity", "OPD"]
patients =[ 35, 10, 76]
color = ['blue', 'orange', 'red']
plt.bar(department, patients, color=color, edgecolor='black')

plt.title("Number of Patients per Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.grid()

plt.show()

department = ["Cardiology", "Maternity", "OPD"]
week1 = [35, 10, 76]
week2 = [30, 12, 98]

x = np.arange(len(department))
width = 0.4

color1 = ['blue', 'red', 'green']
color2 = ['lightblue', 'orange', 'lightgreen']

plt.bar( x - width/2, week1, color=color1, edgecolor='black', width=width, label = week1)
plt.bar( x + width/2, week2, color=color2, edgecolor='black', width=width, label = week2)

plt.xticks(x, department)
plt.title("Number of Patients per Week")
plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.legend()

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


