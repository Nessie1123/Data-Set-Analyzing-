#imports
import matplotlib.pyplot as plt
import pandas as pd
#read
data = pd.read_csv('amazon.csv')
#graphs
plt.boxplot(data.salary_in_usd)
plt.show()
x = data.job_title
y = data.salary_in_usd
plt.bar(x, y, color='red')
plt.xlabel('yeah ')
plt.ylabel('month')
plt.show()
plt.hist(y, bins=30)
plt.xlabel('month')
plt.ylabel('number')
plt.show()
