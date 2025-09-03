# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

# Set style for better looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Task 1: Load and Explore the Dataset
print("="*50)
print("TASK 1: LOAD AND EXPLORE THE DATASET")
print("="*50)

try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    print("✅ Dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    
    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Explore dataset structure
    print("\nDataset information:")
    print(df.info())
    
    print("\nData types:")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing values:")
    missing_values = df.isnull().sum()
    print(missing_values)
    
    # Clean dataset (though Iris dataset typically has no missing values)
    if missing_values.sum() > 0:
        print("\nCleaning missing values...")
        # Fill numerical columns with mean, categorical with mode
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        print("Missing values handled!")
    else:
        print("✅ No missing values found!")
        
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\n" + "="*50)
print("TASK 2: BASIC DATA ANALYSIS")
print("="*50)

# Basic statistics
print("Basic statistics for numerical columns:")
print(df.describe())

# Group by species and compute mean of numerical columns
print("\nMean values by species:")
species_stats = df.groupby('species').mean()
print(species_stats)

# Additional analysis - find patterns
print("\nInteresting findings:")
# Find which species has the largest sepal length
max_sepal_species = species_stats['sepal length (cm)'].idxmax()
print(f"- {max_sepal_species.capitalize()} has the largest average sepal length")

# Find which species has the smallest petal width
min_petal_species = species_stats['petal width (cm)'].idxmin()
print(f"- {min_petal_species.capitalize()} has the smallest average petal width")

# Check correlation between features
correlation = df.corr(numeric_only=True)
print("\nCorrelation matrix:")
print(correlation)

# Task 3: Data Visualization
print("\n" + "="*50)
print("TASK 3: DATA VISUALIZATION")
print("="*50)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Iris Dataset Analysis - Visualizations', fontsize=16, fontweight='bold')

# 1. Line chart - Trends of measurements by species (using index as pseudo-time)
plt.subplot(2, 2, 1)
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data.index[:30], species_data['sepal length (cm)'][:30], 
             marker='o', label=species, linewidth=2)
plt.title('Trend of Sepal Length by Species (First 30 Samples)')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Bar chart - Average measurements by species
plt.subplot(2, 2, 2)
species_means = df.groupby('species').mean()
x = np.arange(len(species_means.index))
width = 0.2

plt.bar(x - width, species_means['sepal length (cm)'], width, label='Sepal Length', alpha=0.8)
plt.bar(x, species_means['sepal width (cm)'], width, label='Sepal Width', alpha=0.8)
plt.bar(x + width, species_means['petal length (cm)'], width, label='Petal Length', alpha=0.8)

plt.xlabel('Species')
plt.ylabel('Average Measurement (cm)')
plt.title('Average Measurements by Species')
plt.xticks(x, species_means.index)
plt.legend()
plt.grid(True, alpha=0.3)

# 3. Histogram - Distribution of sepal length
plt.subplot(2, 2, 3)
plt.hist(df['sepal length (cm)'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# Add vertical lines for mean and median
plt.axvline(df['sepal length (cm)'].mean(), color='red', linestyle='--', label=f'Mean: {df["sepal length (cm)"].mean():.2f}')
plt.axvline(df['sepal length (cm)'].median(), color='green', linestyle='--', label=f'Median: {df["sepal length (cm)"].median():.2f}')
plt.legend()

# 4. Scatter plot - Relationship between sepal length and petal length
plt.subplot(2, 2, 4)
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal length (cm)'], species_data['petal length (cm)'], 
                alpha=0.7, label=species, c=colors[species])

plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

# Add correlation coefficient
corr_coef = np.corrcoef(df['sepal length (cm)'], df['petal length (cm)'])[0, 1]
plt.text(0.05, 0.95, f'Correlation: {corr_coef:.2f}', transform=plt.gca().transAxes, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.tight_layout()
plt.show()

# Additional visualizations
print("\nAdditional visualizations...")

# Boxplot to show distribution by species
plt.figure(figsize=(12, 6))
df_melted = pd.melt(df, id_vars="species", var_name="features", value_name="value")
plt.subplot(1, 2, 1)
sns.boxplot(x="features", y="value", hue="species", data=df_melted)
plt.title('Distribution of Features by Species')
plt.xticks(rotation=45)

# Heatmap of correlations
plt.subplot(1, 2, 2)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Pairplot for comprehensive view
print("\nGenerating pairplot (this may take a moment)...")
sns.pairplot(df, hue='species', palette='husl')
plt.suptitle('Pairplot of Iris Dataset Features', y=1.02)
plt.show()

print("\n" + "="*50)
print("ANALYSIS COMPLETE!")
print("="*50)
print("Key Insights:")
print("1. Setosa species has distinctly smaller petals compared to other species")
print("2. Virginica has the largest sepals on average")
print("3. Petal length and sepal length show strong positive correlation")
print("4. Each species forms distinct clusters in the feature space")
print("5. The dataset is well-balanced with no missing values")