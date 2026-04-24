import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

avg = df.groupby('test preparation course')['math score'].mean()

plt.figure()

plt.subplot(1, 3, 1)
plt.scatter(df['reading score'], df['math score'])

plt.subplot(1, 3, 2)
plt.hist(df['math score'])

plt.subplot(1, 3, 3)
plt.plot(avg.index, avg.values)

plt.tight_layout()
plt.show()