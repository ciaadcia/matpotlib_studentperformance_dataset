import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

avg = df.groupby('test preparation course')['math score'].mean()

plt.bar(avg.index, avg.values)
plt.title('Average Math Score by Test Preparation')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Math Score')
plt.show()