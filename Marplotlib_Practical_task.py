import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
patients_per_month = [120, 150, 180, 170, 200, 220]

departments = ["Cardiology", "Neurology", "Maternity", "Emergency"]
patients_in_dept = [50, 40, 30, 80]

staff_roles = ["Doctors", "Nurses", "Admin", "Support"]
staff_count = [20, 40, 10, 15]
color= ["skyblue", "pink", "lightgreen", "orange"]

ages = [22, 25, 28, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75]
recovery_days = [3, 4, 4, 5, 6, 7, 6, 8, 9, 10, 11, 12, 13, 15]

plt.figure(figsize=(20,20))

plt.suptitle("Hospital Data Visualization Dashboard", fontsize=22, color='darkblue', fontweight='bold')

plt.subplot(3, 2, 1) #Subplotting

#Line Chart

plt.plot(months, patients_per_month, color="yellow", marker="s")
plt.title("Patient Growth Over Months")
plt.xlabel("Month")
plt.ylabel("Patient Per Month")
plt.grid(True)

#Bar Chart

plt.subplot(3, 2, 2)
plt.bar(departments, patients_in_dept, color="skyblue", label=patients_in_dept)
plt.title("Patients per Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.grid(True)

#Pie Chart

plt.subplot(3, 2, 3)
plt.pie(staff_count, colors=color, autopct="%1.1f%%", shadow=True, startangle=90, labels=staff_roles, textprops={'fontsize': 10})
plt.title("Staff Distribution")
plt.grid(True)

#Histogram Chart

plt.subplot(3, 2, 4)
plt.hist(ages, bins=5 ,color="red", edgecolor="black", label=patients_in_dept)
plt.title("Patient Recovery Analysis")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.grid(True)

#Scatter Plot

plt.subplot(3, 2, 5)
plt.scatter(ages, recovery_days, color="purple", marker="o")
plt.title("Patient Recovery Analysis")
plt.xlabel("Age")
plt.ylabel("Number of Days to Recover")
plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.subplots_adjust(hspace=0.6, wspace=0.2)
plt.show()



