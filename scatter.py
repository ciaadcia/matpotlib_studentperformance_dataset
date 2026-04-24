import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.scatter(df['reading score'], df['math score'])
plt.xlabel('Reading Score')
plt.ylabel('Math Score')
plt.title('Scatter Plot')
plt.show()