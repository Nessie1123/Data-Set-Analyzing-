#import
import matplotlib.pyplot as plt
import pandas as pd
#read
data = pd.read_csv('amazon.csv')
#print data
print(data.head())
print(data.shape)
print(data.job_title)
print(data['date'])
print(data.iloc[3:11, :1])
print(data.salary_in_usd.describe())
plt.boxplot(data.salary_in_usd)
plt.show()
x = data.job_title
y = data.salary_in_usd
plt.bar(x, y, color='red')
plt.xlabel('year')
plt.ylabel('month')
plt.show()
plt.hist(y, bins=30)
plt.xlabel('month ')
plt.ylabel('number')
plt.show()
