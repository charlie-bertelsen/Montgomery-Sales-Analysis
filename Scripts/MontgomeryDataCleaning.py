import pandas as pd

df = pd.read_csv("Warehouse_and_Retail_Sales.csv")


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#combine year and month columns
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-01')

#remove duplicate values
df.drop_duplicates(inplace=True)

df = df[['date','year','month','supplier','item_code','item_description','item_type','retail_sales','retail_transfers','warehouse_sales']]


#check the number of NULL values
df.isnull().sum()

#very small number of NULL values so I will just remove the rows with NULL values

df.dropna(subset=['supplier', 'item_type', 'retail_sales'], inplace=True)

df.to_csv('cleaned_alcohol_sales.csv', index=False)