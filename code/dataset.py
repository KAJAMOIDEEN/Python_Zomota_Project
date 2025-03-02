from faker import Faker
import random
import pandas as pd

fake = Faker()

# Constants
NUM_CUSTOMERS = 100
NUM_RESTAURANTS = 50
NUM_ORDERS = 300
NUM_DELIVERIES = 300

### 1. Generate Customers
def generate_customers(num):
    customers = []
    for _ in range(num):
        customers.append({
            "customer_id": _ + 1,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "location": fake.address(),
            "signup_date": fake.date_time_this_decade(),
            "is_premium": random.choice([1, 0]),  # Generate 1 or 0 instead of True/False
            "preferred_cuisine": random.choice(['Indian', 'Chinese', 'Italian', 'Mexican']),
            "total_orders": random.randint(1, 50),
            "average_rating": round(random.uniform(1, 5), 1)
        })
    return pd.DataFrame(customers)

customers_df = generate_customers(NUM_CUSTOMERS)
customers_df.to_csv('customers.csv', index=False)

### 2. Generate Restaurants
def generate_restaurants(num):
    restaurants = []
    for _ in range(num):
        restaurants.append({
            "restaurant_id": _ + 1,
            "name": fake.company(),
            "cuisine_type": random.choice(['Indian', 'Chinese', 'Italian', 'Mexican']),
            "location": fake.city(),
            "owner_name": fake.name(),
            "average_delivery_time": random.randint(20, 60),
            "contact_number": fake.phone_number(),
            "rating": round(random.uniform(1, 5), 1),
            "total_orders": random.randint(10, 200),
            "is_active": random.choice([1, 0])  # Generate 1 or 0 instead of True/False
        })
    return pd.DataFrame(restaurants)

restaurants_df = generate_restaurants(NUM_RESTAURANTS)
restaurants_df.to_csv('restaurants.csv', index=False)

### 3. Generate Orders
def generate_orders(num):
    orders = []
    for _ in range(num):
        orders.append({
            "order_id": _ + 1,
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "restaurant_id": random.randint(1, NUM_RESTAURANTS),
            "order_date": fake.date_time_this_year(),
            "delivery_time": fake.date_time_this_year(),
            "status": random.choice(['Pending', 'Delivered', 'Cancelled']),
            "total_amount": round(random.uniform(10, 100), 2),
            "payment_mode": random.choice(['Credit Card', 'Cash', 'UPI']),
            "discount_applied": round(random.uniform(0, 20), 2),
            "feedback_rating": round(random.uniform(1, 5), 1)
        })
    return pd.DataFrame(orders)

orders_df = generate_orders(NUM_ORDERS)
orders_df.to_csv('orders.csv', index=False)

### 4. Generate Deliveries
def generate_deliveries(num):
    deliveries = []
    for _ in range(num):
        deliveries.append({
            "delivery_id": _ + 1,
            "order_id": random.randint(1, NUM_ORDERS),
            "delivery_person_id": random.randint(1, NUM_CUSTOMERS),  # Simplified
            "delivery_status": random.choice(['On the way', 'Delivered']),
            "distance": round(random.uniform(1, 10), 2),
            "delivery_time": random.randint(10, 120),
            "estimated_time": random.randint(10, 120),
            "delivery_fee": round(random.uniform(1, 10), 2),
            "vehicle_type": random.choice(['Bike', 'Car'])
        })
    return pd.DataFrame(deliveries)

deliveries_df = generate_deliveries(NUM_DELIVERIES)
deliveries_df.to_csv('deliveries.csv', index=False)