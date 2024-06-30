#!/usr/bin/env python
# coding: utf-8

# In[8]:
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)  # For reproducibility
months = pd.date_range(start='2015-01-01', periods=100, freq='M')
sales = np.random.randint(200, 500, size=len(months))  # Sales in thousands of dollars
marketing_spend = np.random.randint(50, 150, size=len(months))  # Marketing spend in thousands of dollars
employees = np.random.randint(10, 50, size=len(months))  # Number of employees

# Create DataFrame
data = {
    'Month': months,
    'Sales': sales,
    'Marketing Spend': marketing_spend,
    'Employees': employees
}
df = pd.DataFrame(data)

# Save DataFrame to CSV on Desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # for Windows
csv_file_path = os.path.join(desktop, 'CompanyXYZ_SalesData.csv')
df.to_csv(csv_file_path, index=False)

print(f"Dataset saved to {csv_file_path}")

# Display the DataFrame
print(df.head())


# In[ ]:


import statsmodels.api as sm

# Prepare the data for regression
X = df['Marketing Spend']
Y = df['Sales']
X = sm.add_constant(X)  # Adds a constant term to the predictor

# Fit the regression model
model = sm.OLS(Y, X).fit()

# Print the regression results
print(model.summary())


# In[9]:


# Step 2.1: Create scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Marketing Spend', y='Sales', data=df, ci=None)
plt.title('Sales vs Marketing Spend with Regression Line')
plt.xlabel('Marketing Spend (in thousands of dollars)')
plt.ylabel('Sales (in thousands of dollars)')
plt.show()


# In[10]:


# Step 2.2: Plot residuals
df['Residuals'] = model.resid
plt.figure(figsize=(10, 6))
sns.histplot(df['Residuals'], kde=True)
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()


# In[11]:


# Step 2.3: Residuals vs Fitted values
df['Fitted Values'] = model.fittedvalues
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Fitted Values', y='Residuals', data=df)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Fitted Values')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()


# In[12]:


# Step 3: Calculate and Visualize Variance
variance_sales = df['Sales'].var()
variance_marketing_spend = df['Marketing Spend'].var()
variance_employees = df['Employees'].var()


# In[13]:


print(f"\nVariance in Sales: {variance_sales}")
print(f"Variance in Marketing Spend: {variance_marketing_spend}")
print(f"Variance in Employees: {variance_employees}")


# In[14]:


# Step 3.1: Line plot to show trends over time
plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Sales'], label='Sales')
plt.plot(df['Month'], df['Marketing Spend'], label='Marketing Spend')
plt.plot(df['Month'], df['Employees'], label='Employees')
plt.title('Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Value (in thousands or units)')
plt.legend()
plt.show()


# In[15]:


# Step 3.2: Box plot to visualize the distribution and variance
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Sales', 'Marketing Spend', 'Employees']])
plt.title('Box Plot of Sales, Marketing Spend, and Employees')
plt.ylabel('Value (in thousands or units)')
plt.show()


# In[ ]:




