import pandas as pd

file_path = 'results/bugs.csv'

# Reload the dataset
df = pd.read_csv(file_path)

# Exploration
print(df.head())

# Basic statistics for numerical columns
numerical_stats = df.describe()
print("Numerical Stats:", numerical_stats)

# Unique values in each non-numeric column
unique_values = {col: df[col].nunique() for col in df.select_dtypes(include=['object']).columns}
print("Unique Values:", unique_values)


# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style
sns.set(style="whitegrid")

# Countplot for 'Protocol Category'
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x='Protocol Category', order=df['Protocol Category'].value_counts().index)
plt.title('Frequência de cada categoria de protocolo')
plt.xlabel('Categoria de protocolo')
plt.ylabel('Contagem de bugs')
plt.xticks(rotation=45)
plt.show()
plt.close()

# Countplot for 'Class'
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x='Class', order=df['Class'].value_counts().index)
plt.title('Frequência de cada classificação')
plt.xlabel('Classificação')
plt.ylabel('Contagem de bugs')
plt.show()
plt.close()

# Countplot for 'Protocol Category' with 'Class' as hue
plt.figure(figsize=(18, 8))
sns.countplot(data=df, x='Protocol Category', hue='Class', order=df['Protocol Category'].value_counts().index)
plt.title('Frequency of Each Protocol Category with Class as Hue')
plt.xlabel('Protocol Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
plt.close()
