#!/usr/bin/env python
# coding: utf-8

# #About Dataset
# salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# # Features
# - 'Id'
# - 'EmployeeName'
# - 'JobTitle'
# - 'BasePay'
# - 'OvertimePay'
# - 'OtherPay'
# - 'Benefits'
# - 'TotalPay' -> salary
# - 'TotalPayBenefits'
# - 'Year'
# - 'Notes'
# - 'Agency'
# - 'Status'
# 

# # Tasks
# 
# 1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.
# 
# 2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
# 
# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.
# 
# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.
# 
# 5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.
# 
# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
# 
# 8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# # Very Important Note
# There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[1]:


# Load your dataset
df = pd.read_csv(r'D:/quetions/archive/Salaries.csv')
df.head()


# In[2]:


df.columns


# In[3]:


df.info()


# In[4]:


num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")


# In[5]:


data_types = df.dtypes
print("\nData types of each column:")
print(data_types)


# In[6]:


df.isnull().sum()


# Since 'Notes' and 'Status' are completely empty, i dropping these columns altogether as they may not provide any useful information.

# In[7]:


df.drop(['Notes', 'Status'], axis=1, inplace=True)


# Imputing with mean/median/mode helps maintain the overall distribution of the data and is a simple way to replace missing values with a representative value.

# In[8]:


df['BasePay'].fillna(df['BasePay'].mean(), inplace=True)
df['Benefits'].fillna(df['Benefits'].median(), inplace=True)


# In[10]:


df['OvertimePay'].fillna(df['OvertimePay'].mean(), inplace=True)
df['OtherPay'].fillna(df['OtherPay'].median(), inplace=True)


# In[11]:


df.isnull().sum()


# In[12]:


selected_columns = ['Id', 'EmployeeName', 'JobTitle', 'BasePay', 'OvertimePay',
                    'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits',
                    'Year','Agency']
selected_df = df[selected_columns]
selected_df


# In[13]:


basic_stats = selected_df.describe()


# In[14]:


basic_stats


# In[15]:


mode_values = selected_df.mode().iloc[0]
mode_values


# In[16]:


salary_range = selected_df['TotalPay'].max() - selected_df['TotalPay'].min()
salary_range


# In[17]:


std_deviation = selected_df['TotalPay'].std()
std_deviation


# In[20]:


sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df['TotalPay'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Salaries')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.show()


# In[29]:


df['Agency'].unique()


# In[21]:


department_counts = df['Agency'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Proportion of Employees in Different Departments')
plt.show()


# Group the data by 'JobTitle' and calculate average salaries

# In[30]:


grouped_data = df.groupby('JobTitle')['TotalPay'].mean().reset_index()
print("Summary Statistics for Average Salaries by Job Title:")
print(grouped_data)


# In[31]:


plt.figure(figsize=(15, 8))
sns.barplot(x='TotalPay', y='JobTitle', data=grouped_data.sort_values('TotalPay', ascending=False).head(10), palette='viridis')
plt.title('Average Salaries Across Different Job Titles')
plt.xlabel('Average Total Pay')
plt.ylabel('Job Title')
plt.show()


# In[32]:


numerical_columns = ['TotalPay', 'BasePay']
correlation_matrix = df[numerical_columns].corr()


# In[33]:


correlation_matrix


# In[34]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='BasePay', y='TotalPay', data=df)
plt.title('Scatter Plot: TotalPay vs BasePay')
plt.xlabel('BasePay')
plt.ylabel('TotalPay')
plt.show()


# In[ ]:




