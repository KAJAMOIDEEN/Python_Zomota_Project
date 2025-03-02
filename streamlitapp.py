import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL DB
def get_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='root', 
        database='zomoto'
    )
    return connection

# Function to execute queries
def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def display_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.title('Zomato - Food Delivery Data Insights')
options = st.sidebar.selectbox('Select an option', ['Add Data', 'Update Data', 'Delete Data', 'Create/Modify Table', 'View Insights'])

# Add Data Section
if options == 'Add Data':
    st.subheader("Add New Order")
    customer_id = st.number_input("Customer ID")
    restaurant_id = st.number_input("Restaurant ID")
    order_date = st.date_input("Order Date")
    delivery_time = st.date_input("Delivery Time")
    status = st.selectbox('Status', ['Pending', 'Delivered', 'Cancelled'])
    total_amount = st.number_input("Total Amount")
    payment_mode = st.selectbox('Payment Mode', ['Credit Card', 'Cash', 'UPI'])
    discount_applied = st.number_input("Discount Applied")
    feedback_rating = st.slider("Feedback Rating", 1, 5, 1)

    if st.button('Submit'):
        query = f"""
        INSERT into Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating)
        VALUES ({customer_id}, {restaurant_id}, '{order_date}', '{delivery_time}', '{status}', {total_amount}, '{payment_mode}', {discount_applied}, {feedback_rating});
        """
        execute_query(query)
        st.success("Order added successfully!")

# Update Data Section
elif options == 'Update Data':
    st.subheader("Update Order")
    order_id = st.number_input("Order ID to Update")
    new_status = st.selectbox('New Status', ['Pending', 'Delivered', 'Cancelled'])
    new_total_amount = st.number_input("New Total Amount")

    if st.button('Update'):
        query = f"""
        UPDATE Orders
        SET status = '{new_status}', total_amount = {new_total_amount}
        WHERE order_id = {order_id};
        """
        execute_query(query)
        st.success("Order updated successfully!")

# Delete Data Section
elif options == 'Delete Data':
    st.subheader("Delete Order")
    order_id_to_delete = st.number_input("Order ID to Delete")

    if st.button('Delete'):
        query = f"DELETE FROM Orders WHERE order_id = {order_id_to_delete};"
        execute_query(query)
        st.success("Order deleted successfully!")

# Create/Modify Table Section
elif options == 'Create/Modify Table':
    st.subheader("Create or Modify Table")
    new_table_name = st.text_input("Table Name")
    columns = st.text_area("Columns (name type, name type, ...)", "column1 VARCHAR(255), column2 number")

    if st.button('Create/Table'):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {new_table_name} ({columns});"
        execute_query(create_table_query)
        st.success(f"Table {new_table_name} created/modified successfully!")

# View Insights Section
elif options == 'View Insights':
    st.subheader("Delivery Insights")
    insight_query = "SELECT status, COUNT(*) AS Total_Orders, AVG(feedback_rating) AS Average_Rating FROM Orders GROUP BY status;"
    insights_df = display_data(insight_query)
    
    st.write(insights_df)

    # Visualizations
    fig, ax = plt.subplots()
    ax.bar(insights_df['status'], insights_df['Total_Orders'], color='blue')
    ax.set_xlabel('Order Status')
    ax.set_ylabel('Total Orders')
    ax.set_title('Total Orders by Status')
    st.pyplot(fig)