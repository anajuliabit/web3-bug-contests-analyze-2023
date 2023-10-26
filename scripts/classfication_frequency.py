# Importing necessary libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Count the frequency of each 'Class'
class_frequency = df['Class'].value_counts()

# Plotting the frequency of each 'Class'
plt.figure(figsize=(12, 6))
sns.barplot(x=class_frequency.index, y=class_frequency.values, palette="viridis")
plt.title('Frequency of Each Class')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
