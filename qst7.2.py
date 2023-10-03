from matplotlib import pyplot as plt
dr = pd.read_csv('Student.csv')
df = pd.DataFrame(dr,index=None)
# Creating histogram
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(df, bins=[0, 25, 50, 75, 100])

# Show plot
plt.show()
