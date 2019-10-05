#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
train_data_path = "data/train_AUpWtIz/train.csv"
campaign_data_path = "data/train_AUpWtIz/campaign_data.csv"
coupon_item_mapping_data_path = "data/train_AUpWtIz/coupon_item_mapping.csv"
customer_demographics_data_path = "data/train_AUpWtIz/customer_demographics.csv"
customer_transaction_data_path = "data/train_AUpWtIz/customer_transaction_data.csv"
item_data_path = "data/train_AUpWtIz/item_data.csv"

train_df = pd.read_csv(train_data_path)
campaign_df = pd.read_csv(campaign_data_path)
coupon_item_df = pd.read_csv(coupon_item_mapping_data_path)
customer_demo_df = pd.read_csv(customer_demographics_data_path)
customer_trans_df = pd.read_csv(customer_transaction_data_path)
item_df =  pd.read_csv(item_data_path)


# In[2]:


train_df.describe()


# In[3]:


print(train_df.isnull().sum())
print("-------------------------------")
print(campaign_df.isnull().sum())
print("-------------------------------")
print(coupon_item_df.isnull().sum())
print("-------------------------------")
print(customer_demo_df.isnull().sum())
print("-------------------------------")
print(customer_trans_df.isnull().sum())
print("-------------------------------")
print(item_df.isnull().sum())
print("-------------------------------")


# In[4]:


customer_demo_df = customer_demo_df[['customer_id', 'age_range', 'rented', 'family_size','income_bracket']]


# In[5]:


#train_df has all the numeric columns
import datetime
campaign_df_1 = campaign_df.copy()
campaign_df_1['start_date'] = campaign_df_1['start_date'].apply(lambda x: datetime.datetime.strptime(x,"%d/%m/%y"))
campaign_df_1['end_date'] = campaign_df_1['end_date'].apply(lambda x: datetime.datetime.strptime(x,"%d/%m/%y"))
campaign_df_1['month'] = campaign_df_1['start_date'].dt.month


# In[6]:


#check the campaign dataframe
campaign_df.select_dtypes(exclude = ["number"])
#it gives three col "campaign_type" ,"start_date","end_date" are not numbers.

#USING GETDUMMIES FUNCTION
campaign_df_1 = pd.get_dummies(campaign_df_1,columns = ['campaign_type'])
#df_with_dummies = pd.get_dummies( df, columns = cols_to_transform )

#check the duration and month from the dates.
campaign_df_1['total_days'] = campaign_df_1['end_date'].values - campaign_df_1['start_date'].values


# In[7]:


#Desired columns from campaign_df csv = ['month',campaign_type_X,campaign_type_Y,total_days]
campaign_data_df = campaign_df_1.loc[:,["campaign_id",'month','campaign_type_X','campaign_type_Y','total_days']]
campaign_data_df['total_days'] = campaign_data_df['total_days'].dt.days
campaign_data_df.to_csv("campaign_data_df.csv")


# In[8]:


#lets numalarise   coupon_item_mapping_data_path csv 

#nothing is there to convert.


# In[9]:


#lets numalarise customer_demographics_data_path csv
customer_demo_df_1 = customer_demo_df.copy()
list1 = ['customer_id', 'age_range', 'rented', 'family_size', 'income_bracket']
list2 = ['age_range','rented','income_bracket']
#rented is categorical 
#age range is categorical
#income_bracket is categorical data 
#convert them to categorical variable.
customer_demo_df_1 = pd.get_dummies(customer_demo_df_1, columns = list2)
customer_demo_df_1.to_csv('customer_demo_df_1.csv')


# In[10]:


#lets move to customer_transaction_data_path
customer_transaction_data_path = "data/train_AUpWtIz/customer_transaction_data.csv"
customer_trans_df = pd.read_csv(customer_transaction_data_path)
#nothing to change here.


# In[11]:


#the last one is item_data_path
item_data_path = "data/train_AUpWtIz/item_data.csv"
item_df =  pd.read_csv(item_data_path)
item_df_1 = item_df.loc[:,['item_id', 'brand_type', 'category']]
list3 = ['brand_type', 'category']
#convert above list to categorical variables.
item_df_1 = pd.get_dummies(item_df_1, columns = list3)
item_df_1.to_csv("item_df_1.csv")


# In[2]:


# lets group them together customer_demo_df and customer_trans_df
#combine train and campaign type.
#two dataframes are -
import pandas as pd
demogra_df = pd.read_csv('customer_demo_df_1.csv')
c_trans_df = pd.read_csv('customer_transaction_data.csv')
df1 = pd.merge(demogra_df, c_trans_df, how = 'inner', on = 'customer_id')
df1.columns


# In[3]:


#lets merge train data and campaign data
t_df = pd.read_csv('train.csv')
c_df = pd.read_csv('campaign_data_df.csv')
df2 = pd.merge(t_df, c_df, how = 'inner', on = 'campaign_id')
df2.columns
@decorater


# In[ ]:


#lets combine df1 and df2 on custmor id
df3 = pd.merge(df1,df2,how='inner',on='customer_id')
df3.to_csv('df3.csv')


# In[ ]:




