import sqlite3

# Connect to sqlite
connect = sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor = connect.cursor()

# Create table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARK INT
    )
''')

# Insert some records
cursor.execute('''INSERT INTO STUDENT VALUES('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('John', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mukesh', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Jacob', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh', 'DEVOPS', 'A', 35)''')

# Display all the records
print('The inserted records are:')
data = cursor.execute('SELECT * FROM STUDENT')

for row in data:
    print(row)

# Commit changes and close the connection
connect.commit()
connect.close()
