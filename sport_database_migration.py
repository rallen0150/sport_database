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
    fieldnames = ["id","first_name","last_name","age","position","points_per_game","rebounds_per_game",
                  "assists_per_game","steals_per_game","blocks_per_game","college"]
    contents = csv.DictReader(open_file, fieldnames=fieldnames)
    for row in contents:
        cursor.execute("INSERT INTO celtics_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                       (row["id"],row["first_name"],row["last_name"],row["age"],row["position"],row["points_per_game"],
                       row["rebounds_per_game"],row["assists_per_game"],row["steals_per_game"],row["blocks_per_game"],row["college"]))

connection.commit()
cursor.close()
connection.close()
