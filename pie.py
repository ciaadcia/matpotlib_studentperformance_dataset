import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

counts = df['test preparation course'].value_counts()

plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title('Pie Chart Test Preparation')
plt.show()