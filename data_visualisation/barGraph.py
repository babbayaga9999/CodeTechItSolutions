import matplotlib.pyplot as plt 

#data
categories = ["Indian","German","Russian","Italian"]
values = [24,10,18,15]

#plotting bar graph
plt.bar(categories, values, color = 'purple')

#adding labels and titles

plt.xlabel('Nationality')
plt.ylabel('Employees')
plt.title('Bar graph')

#Display the data
plt.show()