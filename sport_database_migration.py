import psycopg2
import csv

connection = psycopg2.connect("dbname=sports_database user=sports_database")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS celtics_data;")

create_table_command = """
CREATE TABLE celtics_data (
    id serial PRIMARY KEY,
    first_name VARCHAR (15),
    last_name VARCHAR (15),
    age SMALLINT,
    position VARCHAR(2),
    points_per_game REAL,
    rebounds_per_game REAL,
    assists_per_game REAL,
    steals_per_game REAL,
    blocks_per_game REAL,
    college VARCHAR(5)
);
"""

cursor.execute(create_table_command)
with open("sport_database.csv") as open_file:
    contents = csv.reader(open_file)
    for row in contents:
        cursor.execute("INSERT INTO celtics_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                       (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

connection.commit()
cursor.close()
connection.close()
