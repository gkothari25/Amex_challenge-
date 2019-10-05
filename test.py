# lets group them together customer_demo_df and customer_trans_df
#combine train and campaign type.
#two dataframes are -
import pandas as pd
demogra_df = pd.read_csv('customer_demo_df_1.csv')
c_trans_df = pd.read_csv('customer_transaction_data.csv')
df1 = pd.merge(demogra_df,c_trans_df, on = 'customer_id')
print(df1.columns)


# In[3]:


#lets merge train data and campaign data
t_df = pd.read_csv('train.csv')
c_df = pd.read_csv('campaign_data_df.csv')
df2 = t_df.join(c_df, on = 'campaign_id')
print(df2.columns)


# In[ ]:


#lets combine df1 and df2 on custmor id
df3 = df2.merge(df1,on='customer_id')
df3.to_csv('df3.csv')
print("Done")
																																																																																																																																																																																																																		
