import pandas as pd

# Creating the DataFrame
data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Sales': [100, 200, 150, 300, 250, 400],
    'Region': ['North', 'South', 'North', 'East', 'South', 'East']
}
df = pd.DataFrame(data)

# 1. Find the total sales per product
total_sales_per_product = df.groupby('Product')['Sales'].sum()

# 2. Find the highest sales value per region
highest_sales_per_region = df.groupby('Region')['Sales'].max()

# 3. Add a new column 'Discounted Price' which is 90% of the sales value
df['Discounted Price'] = df['Sales'] * 0.9

# Display results
print("Total Sales per Product:\n", total_sales_per_product)
print("\nHighest Sales per Region:\n", highest_sales_per_region)
print("\nUpdated DataFrame with Discounted Price:\n", df)