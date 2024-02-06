from sqlalchemy import create_engine
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
import umap
import matplotlib.pyplot as plt
import seaborn as sns

# For SQLite: 'sqlite:///your_database_name.db'
# For MySQL: 'mysql+pymysql://user:password@hostname/database_name'
db_connection_str = 'database_connection_string'

# Creating a database engine
db_engine = create_engine(db_connection_str)

# SQL query to select data - needs adjusting
sql_query = """
SELECT * FROM your_table_name WHERE Population IN ('Population1', 'Population2');
"""

# Loading data from the SQL database
data = pd.read_sql(sql_query, db_engine)

# Separate the gene expression data and the population labels
X = data.drop(['Population', 'Superpopulation'], axis=1)  # Adjust column names when needed
y = data['Population']  # Use 'Superpopulation' if needed for clustering

### PCA ###

# Performing PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)

# Get the variance ratio
variance_ratio = pca.explained_variance_ratio_

# Creating a DataFrame for the PCA results
pca_df = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])
pca_df['Population'] = y.values  # Use 'Superpopulation' if needed

# Save PCA plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Population', data=pca_df)
plt.title(f'PCA of Gene Expression Data\nPC1 explains {variance_ratio[0]*100:.2f}% variance, PC2 explains {variance_ratio[1]*100:.2f}% variance')
plt.xlabel(f'Principal Component 1 ({variance_ratio[0]*100:.2f}%)')
plt.ylabel(f'Principal Component 2 ({variance_ratio[1]*100:.2f}%)')
plt.savefig('static/pca_plot.png')  # Save to static directory
plt.close()  # Close the plot to free memory


### MDS ###

# Perform MDS on the same data (X) obtained from PCA
mds = MDS(n_components=2)
mdsComponents = mds.fit_transform(X)

# Creating a DataFrame for the MDS results
mds_df = pd.DataFrame(data=mdsComponents, columns=['MDS1', 'MDS2'])
mds_df['Population'] = y.values  # Use 'Superpopulation' if needed

# Plotting MDS results
plt.figure(figsize=(10, 8))
sns.scatterplot(x='MDS1', y='MDS2', hue='Population', data=mds_df)
plt.title('MDS Analysis of Gene Expression Data')
plt.xlabel('MDS Component 1')
plt.ylabel('MDS Component 2')
plt.savefig('static/mds_plot.png') # Save to static directory 
plt.close()

### UMAP ###

# Perform UMAP on the same data (X) obtained from PCA
umap_model = umap.UMAP(n_components=2)
umapComponents = umap_model.fit_transform(X)

# Creating a DataFrame for the UMAP results
umap_df = pd.DataFrame(data=umapComponents, columns=['UMAP1', 'UMAP2'])
umap_df['Population'] = y.values  # Use 'Superpopulation' if needed

# Plotting UMAP results
plt.figure(figsize=(10, 8))
sns.scatterplot(x='UMAP1', y='UMAP2', hue='Population', data=umap_df)
plt.title('UMAP Analysis of Gene Expression Data')
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.savefig('static/umap_plot.png') # Save to static directory 
plt.close()


