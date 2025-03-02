import pandas as pd

# Load the generated CSV files
customers_df = pd.read_csv('customers.csv')
restaurants_df = pd.read_csv('restaurants.csv')
orders_df = pd.read_csv('orders.csv')
deliveries_df = pd.read_csv('deliveries.csv')

# Display basic information
print(customers_df.info())
print(restaurants_df.info())
print(orders_df.info())
print(deliveries_df.info())

# Viewing the first few rows of each dataframe
print(customers_df.head())
print(restaurants_df.head())
print(orders_df.head())
print(deliveries_df.head())

# Example: Average rating of restaurants by cuisine type
avg_rating_by_cuisine = restaurants_df.groupby('cuisine_type')['rating'].mean()
print(avg_rating_by_cuisine)