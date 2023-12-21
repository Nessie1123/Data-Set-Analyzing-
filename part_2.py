#import
import matplotlib.pyplot as plt
import pandas as pd
#read
data = pd.read_csv('ds_salaries.csv')
#make graphs
plt.boxplot(data.salary_in_usd)
plt.show()
x = data.job_title
y = data.salary_in_usd
plt.bar(x, y, color='red')
plt.xlabel('Job ')
plt.ylabel('salary')
plt.show()
plt.hist(y, bins=30)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()
