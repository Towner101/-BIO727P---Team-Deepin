from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd

# Separate the gene expression data and the population labels
X = merged_data.drop(metadata.columns, axis=1)
y = merged_data['disease.state']

# Performing PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)

# Get the variance ratio
variance_ratio = pca.explained_variance_ratio_

# Creating a DataFrame for the PCA results
pca_df = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])
pca_df['Disease State'] = y.values

# Plotting
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Disease State', data=pca_df)
plt.title(f'PCA of Gene Expression Data\nPC1 explains {variance_ratio[0]*100:.2f}% variance, PC2 explains {variance_ratio[1]*100:.2f}% variance')
plt.xlabel(f'Principal Component 1 ({variance_ratio[0]*100:.2f}%)')
plt.ylabel(f'Principal Component 2 ({variance_ratio[1]*100:.2f}%)')
plt.show()
