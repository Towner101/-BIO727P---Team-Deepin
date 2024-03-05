import pymysql

# Define your MySQL connection details
db_uri = 'mysql+pymysql://root:Hallmark@127.0.0.1:3306/deepin'
# Splitting the URI to use with PyMySQL
user = 'deepinflaskapp'
password = 'Deepin0324'
host = 'localhost'
database = 'deepin'

try:
    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=database)
    
    with connection.cursor() as cursor:
        # Query the database version
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")
        
    connection.close()
    print("Connection successful.")
except Exception as e:
    print(f"Error connecting to the database: {e}")
