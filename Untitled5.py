#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.metrics import ConfusionMatrixDisplay


iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target
print("First 10 rows of the dataset:\n", data.head(10))




print("\n Information Of Dataset:")
print("\n Instances:", data.shape[0])
print("\n Features:", data.shape[1] - 1) 
print("\n Target_Classes:", len(np.unique(data['species'])))
print("\n Description:")
for column in data.columns[:-1]: 
    print(f"{column}: Type={data[column].dtype}, Min={data[column].min()}, Max={data[column].max()}")



    
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap ")
plt.show()



X = data.drop(columns=['species'])
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


X.hist(figsize=(10, 8), bins=10, edgecolor='red')
plt.suptitle("Feature Distributions Before Scaling")
plt.show()

scaled_df = pd.DataFrame(X_train_scaled, columns=iris.feature_names)
scaled_df.hist(figsize=(10, 8), bins=10, edgecolor='red')
plt.suptitle("Feature Distributions After Scaling")
plt.show()










    
    
    
    
    
    
    
    
    
    

