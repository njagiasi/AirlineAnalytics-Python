#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[76]:


path="data/Airline_Raw_data.csv"

#Create DataFrame
df = pd.read_csv(path)


#Print the first few rows of the DataFrame to inspect the data.
print("The first 5 rows of the dataframe") 
df.head(5)


# View the last 5 rows of the DataFrame
df.tail()


#reviewing columns and it's Data Types
df.info()


# Drop rows with missing values and create a new DataFrame
df = df.dropna()
df

#checking if columns contain any space
df.columns

# replace empty cells or strings with NaN values
df = df.replace(' ', np.nan)
df


# Calculate and print the number of missing values in each column
print(df.isnull().sum())


# Check for duplicates count
print(df.duplicated().sum())


#Print duplicate data
duplicates = df[df.duplicated(keep=False)]
print(duplicates)


# Calculate and print the number of duplicate rows
print(df.duplicated().sum())


# To remove duplicates
df = df.drop_duplicates()

# Calculate and print the number of duplicate rows
print(df.duplicated().sum())

#Count missing values in each column
missing_data = df.isnull()
missing_data.head(5)


#Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")   


#Check if the column contains any NaN values
print(df["num_passengers"].isna().sum())
print(df["sales_channel"].isna().sum())
print(df["trip_type"].isna().sum())
print(df["purchase_lead"].isna().sum())
print(df["length_of_stay"].isna().sum())
print(df["flight_hour"].isna().sum())
print(df["flight_day"].isna().sum())
print(df["route"].isna().sum())
print(df["booking_origin"].isna().sum())
print(df["wants_extra_baggage"].isna().sum())
print(df["wants_in_flight_meals"].isna().sum())
print(df["flight_duration"].isna().sum())
print(df["booking_complete"].isna().sum())


# Using data.dtypes to get the data types of columns
df.dtypes


# Using data.describe() to get the summary statistics
df.describe()


# describe all the columns in "df" 
df.describe(include = "all")

# write the data to an Excel file
df.to_excel('Airline_cleaned_data.xlsx', index=False)

# In[78]:

# Read the cleaned data
data = pd.read_excel('Airline_cleaned_data.xlsx')


# Histogram to know about the distribution of flight days
plt.figure(figsize=(8, 6))
plt.hist(data['flight_day'], bins=5, edgecolor='k', alpha=0.7)
plt.xlabel('Flight Day')
plt.ylabel('Frequency')
plt.title('Histogram: Distribution of Flight Days')
plt.grid(True)
plt.show()


# In[79]:


# Stacked bar chart for the no of passengers by booking origin and trip type
data = pd.DataFrame(data)
passengers_by_origin_trip = data.groupby(['booking_origin', 'trip_type'])['num_passengers'].sum().unstack()
passengers_by_origin_trip.plot(kind='bar', stacked=True, figsize=(50, 30))
plt.xlabel('Booking Origin')
plt.ylabel('Number of Passengers')
plt.title('Stacked Bar Chart: Number of Passengers by Booking Origin and Trip Type')
plt.show()


# In[80]:


# Pie chart for sales channels
df = pd.DataFrame(data)
sales_channel_counts = df['sales_channel'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(sales_channel_counts, labels=sales_channel_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.axis('equal')
plt.title('Distribution of Sales Channels')
plt.show()


# In[81]:


#Bar graph to compare which route is preferred by passengers
values = {
     'route': ['AKLKUL', 'PENTPE', 'MELSGN', 'ICNSIN', 'DMKKIX', 'ICNSYD', 'DMKPER', 'DPSICN', 'DMKOOL', 'MELPEN', 'MELTPE', 'SGNSYD', 'DMKSYD', 'COKSYD'],
     'count': [2680, 924, 842, 801, 744, 695, 679, 666, 655, 649, 644, 614, 532, 511]
 }
graph = pd.DataFrame(values)
graph.plot(x='route', y='count', kind='bar')
plt.xlabel('Route')
plt.ylabel('No of passengers')
plt.title('Bar Graph: Most frequently used routes by the passengers')
plt.show()


# In[82]:


# Heat map for the average flight hour in each day
data = pd.DataFrame(data)
avg_flight_hour = data.groupby('flight_day')['flight_hour'].mean()
avg_flight_hour
avg_flight_hour_df = pd.DataFrame(avg_flight_hour)
sns.heatmap(avg_flight_hour_df, annot=True, cmap='YlGnBu')
plt.show()


# In[83]:


# Bubble chart to know the relationship between flight duration and length of stay
data['category_column'] = pd.cut(data['length_of_stay'], bins=3, labels=['Low', 'Medium', 'High'])
sns.scatterplot(data=data, x='flight_duration', y='length_of_stay', hue='category_column', size='flight_duration', sizes=(50, 200), alpha=0.7)
plt.xlabel('Flight Duration')
plt.ylabel('Length of Stay')
plt.title('Bubble Chart for flight duration and length of stay')
plt.show()

