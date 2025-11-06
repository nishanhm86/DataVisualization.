import matplotlib.pyplot as plt

x = [2,4,6,8,10,12,14,16,18,20]
y = [20,40,60,80,100,120,140,160,180,200]

department = ["Cardiology", "Emergency", "Maternity"]
patients = [35, 60, 15]

departments1 = ["Finance", "Operations", "HR"]
employees = [125, 275, 60]
color = ["red", "blue", "green"]

plt.figure(figsize = (15,15))

#create subplots
plt.subplot(2,2,1)

#first chart

plt.plot(x,y, color="skyblue", marker='o')
plt.title("Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.grid(True)


plt.subplot(2,2,2)
plt.bar(department, patients, color="pink")
plt.title("Department Chart")
plt.xlabel("Department ID")
plt.ylabel("Patient ID")
plt.grid(True)


plt.subplot(2,2,3)
plt.pie (employees, labels=departments1, colors=color, autopct="%1.1f%%")
plt.title("Employee Chart")
plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
