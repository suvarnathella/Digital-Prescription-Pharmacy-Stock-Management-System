from pymysql import connect

def get_connection():
    connection = connect(
        host = 'localhost',
        user = 'root',
        password = 'YOUR_PASSWORD',
        database = 'pharmacy_db'
    )
    return connection