# lets group them together customer_demo_df and customer_trans_df
#combine train and campaign type.
#two dataframes are -
import pandas as pd
demogra_df = pd.read_csv('customer_demo_df_1.csv')
c_trans_df = pd.read_csv('customer_transaction_data.csv')
df1 = pd.merge(demogra_df, c_trans_df, how = 'inner', on = 'customer_id')
print(df1.columns)


# In[3]:


#lets merge train data and campaign data
t_df = pd.read_csv('train.csv')
c_df = pd.read_csv('campaign_data_df.csv')
df2 = pd.merge(t_df, c_df, how = 'inner', on = 'campaign_id')
print(df2.columns)


# In[ ]:


#lets combine df1 and df2 on custmor id
df3 = pd.merge(t_df,df1,how='inner',on='customer_id')
df3.to_csv('df3.csv')
print("Done")
																																																																																																																																																																																																																		
