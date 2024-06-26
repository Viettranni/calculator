# Connecting to the 'calculator' database
import mysql.connector
from mysql.connector import Error

# If the database is not created yet we can initialise it with this function. Call it at the top of the main loop
def create_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS calculator_db")
        cursor.execute("USE calculator_db")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_input INT,
                second_input int,
                operation VARCHAR(255),
                answer FLOAT
            )
        ''')
        conn.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def save_to_database(first_input, second_input, operation, answer):
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            database = 'calculator_db',
            user = 'root',
            password = 'root'
        )
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO history (first_input, second_input, operation, answer)
            VALUES (%s, %s, %s, %s)
        ''', (first_input, second_input, operation, answer))
        conn.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def get_history():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='calculator_db',
            user='root',
            password='root'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history")
        rows = cursor.fetchall()
        if rows:
            for idx, row in enumerate(rows, start=1):
                id, first_input, second_input, operation, answer = row
                print(
                    f"{idx}. First input = {first_input}, Second input = {second_input}, Operation = {operation}, Answer = {answer}")
        else:
            print("No history found.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()