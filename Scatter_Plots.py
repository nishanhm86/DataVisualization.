import matplotlib.pyplot as plt

male_age = []
male_income = []
female_age = []
female_income = []

while True:
    print("=" * 20)
    print("1. Add male age group")
    print("2. Add male income group")
    print("3. Add female age group")
    print("4. Add female income group")
    print("5. Exit")
    print("=" * 20)
    choice = input("Enter your choice(1-5): ")
    if choice == "1":
        mag = int(input("Enter the size of age group: "))
        for i in range(mag):
            num = int(input(f"Enter age{i+1}: "))
            male_age.append(num)
    elif choice == "2":
        mig = int(input("Enter the size of income group: "))
        for i in range(mig):
            num = int(input(f"Enter income{i+1}: "))
            male_income.append(num)

    elif choice == "3":
        fag = int(input("Enter the size of age group: "))
        for i in range(fag):
            num = int(input(f"Enter age{i + 1}: "))
            female_age.append(num)

    elif choice == "4":
        fig = int(input("Enter the size of income group: "))
        for i in range(fig):
            num = int(input(f"Enter income{i + 1}: "))
            female_income.append(num)
    elif choice == "5":
        print("Leaving the system")
        break

    else:
        print("Please enter a valid choice.")

if len(male_age) == len(male_income) and len(female_age) == len(female_income):
    plt.scatter(male_age, male_income, color="blue", label="Male", marker='o')
    plt.scatter(female_age, female_income, color='pink', label="Female", marker = 's')
    plt.title("Income level by age group")
    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.grid(True)
    plt.show()

else:
    print("Number of age group and income group must be equal before plotting.")