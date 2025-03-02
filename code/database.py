class Database:
    def __init__(self):
        self.connection = get_connection()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def fetch_data(self, query):
        return pd.read_sql(query, self.connection)

    def close(self):
        self.connection.close()

# Usage
db = Database()
db.execute_query("YOUR_QUERY")
data = db.fetch_data("SELECT * FROM Orders")
db.close()