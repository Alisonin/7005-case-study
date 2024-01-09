import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the uploaded file
file_path = 'E:\deskop\um datascience\7005 case study\E-commerce Customer Behavior - Sheet1.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Analyzing the provided dataset
summary_stats = data.describe()

# Plotting distributions and counts
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
sns.histplot(data['Age'], bins=30, kde=True, ax=axs[0, 0])
axs[0, 0].set_title('Age Distribution')
sns.histplot(data['Total Spend'], bins=30, kde=True, ax=axs[0, 1])
axs[0, 1].set_title('Total Spend Distribution')
sns.countplot(x='Membership Type', data=data, ax=axs[1, 0])
axs[1, 0].set_title('Membership Type Distribution')
sns.countplot(x='Gender', data=data, ax=axs[1, 1])
axs[1, 1].set_title('Gender Distribution')
plt.tight_layout()

correlation_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Generating the synthetic dataset
num_entries = 20000
age_mean, age_std = summary_stats.loc['mean', 'Age'], summary_stats.loc['std', 'Age']
total_spend_mean, total_spend_std = summary_stats.loc['mean', 'Total Spend'], summary_stats.loc['std', 'Total Spend']
items_purchased_mean, items_purchased_std = summary_stats.loc['mean', 'Items Purchased'], summary_stats.loc['std', 'Items Purchased']
locations = ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami']
categories = ['Electronics', 'Clothing', 'Home Goods']
occupations = ['Engineer', 'Teacher', 'Doctor', 'Artist', 'Salesperson', 'Manager']

np.random.seed(0)
synthetic_data = {
    'CustomerID': np.arange(1, num_entries + 1),
    'Age': np.random.normal(age_mean, age_std, num_entries).astype(int).clip(lower=18),
    'Gender': np.random.choice(['Male', 'Female'], num_entries),
    'Location': np.random.choice(locations, num_entries),
    'MembershipLevel': np.random.choice(['Bronze', 'Silver', 'Gold'], num_entries),
    'TotalPurchases': np.random.poisson(items_purchased_mean, num_entries),
    'TotalSpent': np.random.normal(total_spend_mean, total_spend_std, num_entries).clip(lower=0),
    'FavoriteCategory': np.random.choice(categories, num_entries),
    'LastPurchaseDate': [datetime.now() - timedelta(days=int(np.random.rand()*365)) for _ in range(num_entries)],
    'Occupation': np.random.choice(occupations, num_entries),
    'FrequencyOfWebsiteVisits': np.random.poisson(5, num_entries),
    'Churn': np.random.choice([0, 1], num_entries, p=[0.7, 0.3])
}
synthetic_data_df = pd.DataFrame(synthetic_data)

# Introducing missing values
missing_value_columns = ['TotalPurchases', 'TotalSpent', 'Occupation']
missing_percentage = 0.01  # 1% missing values
for col in missing_value_columns:
    synthetic_data_df.loc[synthetic_data_df.sample(frac=missing_percentage).index, col] = np.nan

# Saving the dataset
synthetic_data_df.to_csv('updated_synthetic_e_commerce_customer_behavior.csv', index=False)
