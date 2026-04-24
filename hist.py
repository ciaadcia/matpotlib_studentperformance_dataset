import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.hist(df['math score'])
plt.title('Histogram Math Score')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()