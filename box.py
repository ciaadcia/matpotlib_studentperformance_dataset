import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.boxplot(df['math score'])
plt.title('Boxplot Math Score')
plt.show()