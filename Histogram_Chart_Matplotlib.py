import matplotlib.pyplot as plt


age = [14,18, 20, 22, 25, 22, 40, 27, 72, 72, 75, 80, 80, 83,28, 82, 75, 74, 73, 27, 56, 55, 55, 24, 26, 29, 33, 37, 36, 35, 25, 29, 39,40, 42, 47, 52, 58, 60, 62, 65, 67, 69, 70]

plt.hist(age, bins = 5, color = 'darkblue', edgecolor = 'black')
plt.title("Age of people in the room")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle = '--', alpha=0.75)

plt.show()