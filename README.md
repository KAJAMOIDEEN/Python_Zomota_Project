# Python Zomato Project

This project is a custom-developed restaurant data application built using Python, Streamlit, and MySQL. The dataset was generated using Python libraries such as Faker and NumPy, then imported into a MySQL database. The application provides an interactive interface to explore restaurant information and delivery insights.

## Description

The Python Zomato Project simulates a real-world restaurant data platform. It utilizes a synthetic dataset created with Faker and NumPy to mimic restaurant details like name, location, cuisine, ratings, and costs. Additionally, the project includes delivery insights, offering analysis on delivery times, order volumes, and customer preferences. The data is stored in a MySQL database, and the frontend is built with Streamlit for seamless interaction.

## Features

- **Data Generation:** Use of Faker and NumPy to generate realistic restaurant data.
- **Database Integration:** Importing data into MySQL for efficient storage and retrieval.
- **Interactive UI:** Streamlit app for searching, filtering, and viewing restaurant details.
- **Delivery Insights:** Visualizations and analysis on delivery performance, order trends, and customer behavior.
- **Data Exploration:** Users can filter restaurants based on various parameters such as location, cuisine, ratings, and cost.

## Technologies Used

- **Python:** Main programming language for data generation, database interaction, and app development.
- **Faker & NumPy:** Libraries used to generate synthetic restaurant data.
- **MySQL:** Database system to store and manage the dataset.
- **Streamlit:** Framework for building the interactive web app.
- **SQL:** For querying and managing data in MySQL.

## Setup and Usage

Follow these steps to set up and run the project locally:

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/KAJAMOIDEEN/Python_Zomota_Project.git
   ```  

2. **Install dependencies:**  
   Make sure you have Python installed, then install required packages:  
   ```bash
   pip install pandas mysql-connector-python streamlit faker numpy
   ```  

3. **Set up MySQL database:**  
   - Create a database named `restaurant_db` (or your preferred name).  
   - Import the generated CSV data into MySQL or run the provided scripts to populate the database.  
   - Update database connection details in the `app.py` or relevant configuration files.

4. **Run the Streamlit app:**  
   ```bash
   streamlit run streamlitapp.py
   ```  


## Contribution

Contributions are welcome! Feel free to fork the repository, improve the data generation scripts, enhance the app features—including the delivery insights—or fix bugs. Pull requests are appreciated.

## Contact

For support or questions, please contact the repository owner via GitHub.

---

Enjoy exploring the restaurant data and delivery insights through this interactive Streamlit app!
