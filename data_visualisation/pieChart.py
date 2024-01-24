import matplotlib.pyplot as plt 
import numpy as np

#sample data
x = np.array([35,25,25,15])
mylabels = ["Data Structures","c","Python","Javascript"]

#plotting the pie chart
plt.pie(x, labels = mylabels, startangle = 90)

plt.title('Number of students opted for following subjects')
#Display the plot
plt.show()