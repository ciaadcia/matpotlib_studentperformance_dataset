import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

avg = df.groupby('test preparation course')['math score'].mean()

plt.plot(avg.index, avg.values)
plt.title('Line Chart Math Score')
plt.show()