import psycopg2

def print_table():
    if choice == 't':
        cursor.execute("SELECT * FROM celtics_data ORDER BY id;")
        results = cursor.fetchall()
        print("id name age position points rebounds assists steals blocks college\n")
        for row in results:
            print('{} {} {} {} {} {} {} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

def print_name():
    if choice == 'n':
        first_name = input("What is the first name?\n>").title()
        last_name = input("What is the last name?\n>").title()
        cursor.execute("SELECT * FROM celtics_data where first_name = %s and last_name = %s;", (first_name, last_name))
        results = cursor.fetchall()
        print(*results)

def show_positions():
    if choice == 'po':
        new_choice = input("Select one of these positions: C PF SF SG PG\n>").upper()
        cursor.execute("SELECT first_name, last_name, position FROM celtics_data where position = %s;", (new_choice,))
        results = cursor.fetchall()
        print_out_stats(results)


def print_points():
    if choice == "p":
        cursor.execute("SELECT first_name, last_name, points_per_game FROM celtics_data ORDER BY points_per_game DESC;")
        results = cursor.fetchall()
        print("Points Per Game")
        print_out_stats(results)

def print_rebounds():
    if choice == "r":
        cursor.execute("SELECT first_name, last_name, rebounds_per_game FROM celtics_data ORDER BY rebounds_per_game DESC;")
        results = cursor.fetchall()
        print("Rebounds Per Game")
        print_out_stats(results)

def print_assists():
    if choice == "a":
        cursor.execute("SELECT first_name, last_name, assists_per_game FROM celtics_data ORDER BY assists_per_game DESC;")
        results = cursor.fetchall()
        print("Assists Per Game")
        print_out_stats(results)

def print_steals():
    if choice == "s":
        cursor.execute("SELECT first_name, last_name, steals_per_game FROM celtics_data ORDER BY steals_per_game DESC;")
        results = cursor.fetchall()
        print("Steals Per Game")
        print_out_stats(results)

def print_blocks():
    if choice == "b":
        cursor.execute("SELECT first_name, last_name, blocks_per_game FROM celtics_data ORDER BY blocks_per_game DESC;")
        results = cursor.fetchall()
        print("Blocks Per Game")
        print_out_stats(results)

def print_age():
    if choice == "age":
        cursor.execute("SELECT first_name, last_name, age FROM celtics_data ORDER BY age;")
        results = cursor.fetchall()
        print("Age")
        print_out_stats(results)

def print_college():
    if choice == "c":
        cursor.execute("SELECT first_name, last_name, college FROM celtics_data ORDER BY college;")
        results = cursor.fetchall()
        print("College")
        print_out_stats(results)


def add_player():
    if choice == "add":
        id_num = 16
        first_name = input("Enter the first name: ").title()
        last_name = input("Enter the last name: ").title()
        age = input("Enter the age: ")
        position = input("Enter the position: ").upper()
        points_per_game = input("Enter the points per game average: ")
        rebounds_per_game = input("Enter the rebounds per game average: ")
        assists_per_game = input("Enter the assists per game average: ")
        steals_per_game = input("Enter the steals per game average: ")
        blocks_per_game = input("Enter the blocks per game average: ")
        college = input("What college did the player go to? ")

        cursor.execute("SELECT * FROM celtics_data;")
        results = cursor.fetchall()
        for row in results:
            while id_num == row[0]:
                id_num += 1

        cursor.execute("""INSERT INTO celtics_data (id, first_name, last_name, age, position, points_per_game,
                       rebounds_per_game, assists_per_game, steals_per_game, blocks_per_game, college) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                       (id_num, first_name, last_name, age, position, points_per_game,
                        rebounds_per_game, assists_per_game, steals_per_game, blocks_per_game, college))

def update():
    if choice == 'u':
        player = input("Enter the ID number of the player you want to update information for:\n>")
        cursor.execute("SELECT * FROM celtics_data where id = %s;", (player,))
        results = cursor.fetchall()
        print(*results)
        update_choice = input("Which information would you like to update from the original search?\n>")
        update_info(player, update_choice)

def update_info(player, update_choice):
    if update_choice == 'n':
        first_name = input("Enter the first name: ").title()
        last_name = input("Enter the last name: ").title()
        cursor.execute("UPDATE celtics_data SET first_name = %s, last_name = %s where id = %s;", (first_name, last_name, player))
    elif update_choice == 'po':
        position = input("Enter the updated position: ").upper()
        cursor.execute("UPDATE celtics_data SET position = %swhere id = %s;", (position, player))
    elif update_choice == 'p':
        points = input("Enter the new points per game average: ")
        cursor.execute("UPDATE celtics_data SET points_per_game = %s where id = %s;", (points, player))
    elif update_choice == 'r':
        rebounds = input("Enter the new rebounds per game average: ")
        cursor.execute("UPDATE celtics_data SET rebounds_per_game = %s where id = %s;", (rebounds, player))
    elif update_choice == 'a':
        assists = input("Enter the new assists per game average: ")
        cursor.execute("UPDATE celtics_data SET assists_per_game = %s where id = %s;", (assists, player))
    elif update_choice == 's':
        steals = input("Enter the new steals per game average: ")
        cursor.execute("UPDATE celtics_data SET steals_per_game = %s where id = %s;", (steals, player))
    elif update_choice == 'b':
        blocks = input("Enter the new blocks per game average: ")
        cursor.execute("UPDATE celtics_data SET blocks_per_game = %s where id = %s;", (blocks, player))
    elif update_choice == 'age':
        age = input("Update the player's age: ")
        cursor.execute("UPDATE celtics_data SET age = %s where id = %s;", (age, player))
    elif update_choice == 'c':
        college = input("Update the college that the player attended: ")
        cursor.execute("UPDATE celtics_data SET college = %s where id = %s;", (college, player))


def print_out_stats(results):
    for row in results:
        print('{} {} --> {}'.format(row[0], row[1], row[2]))

def exit_database():
    if choice == "q":
        print("Thanks for looking into the stats from the 2007 Boston Celtics!")

connection = psycopg2.connect("dbname=sports_database")
cursor = connection.cursor()

choice = ''

while choice != 'q':

    choice = input("""Would you like to search the 2007 Boston Celtics roster by looking at the (t)able, (n)ame, (po)sition, (p)oints per game, (r)ebounds per game
                   (a)ssists per game, (s)teals_per_game, (b)locks per game, (age), (c)ollege, (add) a player, (u)pdate any information or (q)uit the database?\n>""").lower()

    print_table()
    print_name()
    show_positions()
    print_points()
    print_rebounds()
    print_assists()
    print_steals()
    print_blocks()
    print_age()
    print_college()
    add_player()
    update()
    exit_database()


cursor.close()
connection.close()
