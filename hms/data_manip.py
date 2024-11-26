import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API Endpoints
doctor_url = "http://127.0.0.1:8000/doctors"
patient_url = "http://127.0.0.1:8000/patients"

# Fetching data
doctor_data = requests.get(doctor_url).json()
patient_data = requests.get(patient_url).json()

df_a = pd.DataFrame(doctor_data)
df_b = pd.DataFrame(patient_data)

df_a.to_csv('doctors.csv', index=False)
df_b.to_csv('patients.csv', index=False)

print("Doctors DataFrame:")
print(df_a.head())
print("\Patients DataFrame:")
print(df_b.head())

merged_df = pd.merge(df_a, df_b, left_on='name', right_on='product', how='outer')
print("Merged DataFrame:")
print(merged_df.head())

concatenated_df = pd.concat([df_a, df_b], axis=0)
print("Concatenated DataFrame:")
print(concatenated_df.head())

print("Data Information:")
print(merged_df.info())

print("\nDescriptive Statistics:")
print(merged_df.describe())

print("\nMissing Values Count:")
print(merged_df.isnull().sum())


# VISUALIZATION

# Histogram
merged_df['price'].hist(bins=10)
plt.title('Price Distribution')
plt.show()

# Boxplot for detecting outliers
sns.boxplot(data=merged_df, y='price')
plt.title('Price Boxplot')
plt.show()

# Detecting missing values
print("Missing Values Count:")
print(merged_df.isnull().sum())

# Fill with Mean/Median/Mode
merged_df['age'] = merged_df['age'].fillna(merged_df['age'].mean())
merged_df['city'] = merged_df['city'].fillna(merged_df['city'].mode()[0])

# Forward/Backward Fill
merged_df = merged_df.fillna(method='ffill')  # Forward fill
merged_df = merged_df.fillna(method='bfill')  # Backward fill

# Drop Missing Rows
merged_df = merged_df.dropna()

# ENCODINGS

# One hot Encoding
one_hot_df = pd.get_dummies(merged_df, columns=['city', 'category'])
print("One-Hot Encoded DataFrame:")
print(one_hot_df.head())

# Label Encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
merged_df['city_encoded'] = le.fit_transform(merged_df['city'].astype(str))
print("Label Encoded DataFrame:")
print(merged_df.head())

#Binary encoding
import category_encoders as ce

binary_encoder = ce.BinaryEncoder(cols=['category'])
binary_encoded = binary_encoder.fit_transform(merged_df)
print("Binary Encoded DataFrame:")
print(binary_encoded.head())

# Frequency encoding
frequency_encoding = merged_df['category'].value_counts(normalize=True)
merged_df['category_freq_encoded'] = merged_df['category'].map(frequency_encoding)
print("Frequency Encoded DataFrame:")
print(merged_df.head())


# Target encoding
target_mean = merged_df.groupby('category')['price'].mean()
merged_df['category_target_encoded'] = merged_df['category'].map(target_mean)
print("Target Encoded DataFrame:")
print(merged_df.head())


# Reversing the label encoding
merged_df['city_decoded'] = le.inverse_transform(merged_df['city_encoded'])
print("Decoded City Column:")
print(merged_df[['city', 'city_encoded', 'city_decoded']].head())


# Saving the processed dataset
merged_df.to_csv('processed_data.csv', index=False)
print("Processed dataset saved.")


# Correlation analysis
correlation_matrix = merged_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# Pivot Tables
pivot_table = merged_df.pivot_table(values='price', index='city', columns='category', aggfunc='mean')
print("Pivot Table:")
print(pivot_table)


"""
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
BASE_URL = "http://127.0.0.1:8000"
# 1. Fetch Data from API
def fetch_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}/")
    response.raise_for_status()
    return response.json()
# Fetch data for freelancers, projects, and clients
freelancers = fetch_data("freelancers")
projects = fetch_data("projects")
clients = fetch_data("clients")
# 2. Load Data into DataFrames
freelancers_df = pd.DataFrame(freelancers)
projects_df = pd.DataFrame(projects)
clients_df = pd.DataFrame(clients)
# Preview the data
print("Freelancers DataFrame:")
print(freelancers_df.head())
print("Projects DataFrame:")
print(projects_df.head())
print("Clients DataFrame:")
print(clients_df.head())
random_ids = random.sample(range(1, 11), len(clients_df["project_id"].isnull()))
clients_df.loc[clients_df["project_id"].isnull(), "project_id"] = random_ids
# Convert 'project_id' to integers
clients_df["project_id"] = clients_df["project_id"].astype(int)
# 3. Perform Joins
# Left join freelancers with clients on a hypothetical column, assuming 'project_id'
fused_df = pd.merge(freelancers_df, clients_df, left_on="id", right_on="project_id", how="left")
print("Fused DataFrame (Freelancers + Clients):")
print(fused_df.head())
# Right join clients with projects on 'id' and 'project_id'
clients_projects_df = pd.merge(clients_df, projects_df, left_on="project_id", right_on="id", how="right")
print("Clients and Projects DataFrame:")
print(clients_projects_df.head())
# 4. Merge All Data
merged_df = pd.merge(fused_df, projects_df, left_on="project_id", right_on="id", how="inner")
print("Merged DataFrame:")
print(merged_df.head())
# 5. Compute Statistics
print("Statistics for Hourly Rates:")
print(freelancers_df["hourly_rate"].describe())
numerical_cols = freelancers_df.select_dtypes(include=[np.number])
correlation_matrix = numerical_cols.corr()
# Plot the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
# 6. Export Data to CSV
merged_df.to_csv("merged_data.csv", index=False)
print("Merged data exported to 'merged_data.csv'.")
# 7. Simple Machine Learning Example
# Predict hourly_rate based on other features
freelancers_df = freelancers_df.dropna(subset=["hourly_rate"])
X = freelancers_df[["id"]]  # Hypothetical feature
y = freelancers_df["hourly_rate"]











Message year3d










"""

