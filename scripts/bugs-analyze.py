import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'results/bugs.csv'

# Reload the dataset
df = pd.read_csv(file_path)

# Drop the last line from the dataset
df = df.iloc[:-1]

# Filter out bugs classified with the class 'O'
df = df[df['Class'] != 'O']

# Exploration
print(df.head())

# Basic statistics for numerical columns
numerical_stats = df.describe()
print("Numerical Stats:", numerical_stats)

# Unique values in each non-numeric column
unique_values = {col: df[col].nunique() for col in df.select_dtypes(include=['object']).columns}
print("Unique Values:", unique_values)

# Análise da frequência de bugs por categoria de protocolo
bug_count_by_category = df['Protocol Category'].value_counts()

print("Frequencia por categoria", bug_count_by_category)

# Relação entre o número de auditores e a classificação do bug
bug_difficulty_revised = df.groupby('Class')['Auditors'].mean().sort_values()

print("Dificuldade", bug_difficulty_revised)

# Visualization: Set the style
sns.set(style="whitegrid")

# Function to add labels on bars
def add_labels(ax):
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height())}", (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

# Countplot for 'Protocol Category'
plt.figure(figsize=(14, 6))
ax = sns.countplot(data=df, x='Protocol Category', order=df['Protocol Category'].value_counts().index)
plt.title('Frequência de cada categoria de protocolo')
plt.xlabel('Categoria de protocolo')
plt.ylabel('Contagem de bugs')
add_labels(ax)
plt.xticks(rotation=45)
plt.show()
plt.close()

# Countplot for 'Class'
plt.figure(figsize=(14, 6))
ax = sns.countplot(data=df, x='Class', order=df['Class'].value_counts().index)
plt.title('Frequência de cada classificação')
plt.xlabel('Classificação')
plt.ylabel('Contagem de bugs')
add_labels(ax)
plt.show()
plt.close()

# Countplot for 'Protocol Category' with 'Class' as hue
plt.figure(figsize=(18, 8))
ax = sns.countplot(data=df, x='Protocol Category', hue='Class', order=df['Protocol Category'].value_counts().index)
plt.title('Frequency of Each Protocol Category with Class as Hue')
plt.xlabel('Protocol Category')
plt.ylabel('Count')
add_labels(ax)
plt.xticks(rotation=45)
plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
plt.close()
