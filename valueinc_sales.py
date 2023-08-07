import pandas as pd

# Read the CSV file
data = pd.read_csv('transaction2.csv', sep=';')

# Get info about the data
data.info()

# Define variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Calculate profit and cost per transaction
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem

# Add columns to the DataFrame
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = SellingPricePerItem * NumberofItemsPurchased
data['ProfitPerTransaction'] = ProfitPerTransaction

# Calculate and add Markup column
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']
data['Markup'] = data['Markup'].round(2)

# Transform data and manipulate columns
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Split ClientKeywords column and create new columns
split_col = data['ClientKeywords'].str.split(',', expand=True)
data['ClientAge'] = split_col[0].str.replace('(', '')
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2].str.replace(')', '')

# Merge with seasons data
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
data = pd.merge(data, seasons, on='Month')

# Drop unnecessary columns
columns_to_drop = ['ClientKeywords', 'Day', 'Year', 'Month']
data = data.drop(columns_to_drop, axis=1)

# Export cleaned data to CSV
data.to_csv('ValueInc_Cleaned.csv', index=False)
