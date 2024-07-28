import pymysql

try:
    # Connect to the MySQL server
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        cursorclass=pymysql.cursors.DictCursor  # Optional, but recommended
    )
    print("MySQL server is running")

except pymysql.Error as e:  # Use the base exception class
    print(f"Error: {e}")

finally:
    if connection:
        connection.close()

           
