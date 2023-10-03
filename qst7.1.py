import seaborn as sns
import matplotlib.pyplot as plt
marks = [24, 18, 37, 25, 30, 35, 40, 45, 32, 54, 60]
plt.figure(figsize=(8, 6))
sns.boxplot(y=marks, color='blue')
plt.title('Quartile Plot Marks')
plt.ylabel('Marks')
plt.show()
