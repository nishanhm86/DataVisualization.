import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

#create a line plot

plt.plot( x,y, marker='o', color='blue', linestyle='dashed')

#Add title and label

plt.title('Simple line chart')
plt.xlabel('x Values')
plt.ylabel('y Values')


#Add grid

plt.grid()

#display the chart

plt.show()

departments = ["Cardiology", "Maternity", "Pediatric"]
patients = [35, 25, 10]

plt.plot(departments, patients, marker='o', color='black', linestyle='solid')

plt.title("Line Chart Available Patients")
plt.xlabel('Departments')
plt.ylabel('Patients')

plt.grid()

plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
c = 5

y = [num + c for num in x * 2]

plt.plot(x,y, marker='o', color='red', linestyle='dashed')

plt.title("Line Chart Available Patients")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid()

plt.show()