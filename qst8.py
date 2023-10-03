import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#random data instaed of dataset
np.random.seed(42)
data = pd.DataFrame({
 'Income': np.random.normal(50000, 15000, 100),
 'Education': np.random.normal(16, 3, 100)
})

# Distribution charts
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(data['Income'], kde=True, color='blue')
plt.title('Income Distribution')

plt.subplot(1, 2, 2)
sns.histplot(data['Education'], kde=True, color='green')
plt.title('Education Distribution')

plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Income', y='Education', data=data, color='red')
plt.title('Income vs. Education Scatter Plot')
plt.xlabel('Income')
plt.ylabel('Education')
plt.show()

correlation = data['Income'].corr(data['Education'])
print(f"Correlation between Income and Education: {correlation}")