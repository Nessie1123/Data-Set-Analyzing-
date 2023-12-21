#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('ds_salaries.csv')
#generation
x = data.experience_level
x = pd.get_dummies(data=x, drop_first=True)
y = data.salary_in_usd
X_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
re = LinearRegression()
re.fit(X_train, y_train)
y_pre = re.predict(x_test)
print(y_pre)
print(re.score(x_test, y_test))
