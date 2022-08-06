import sqlite3


connection = sqlite3.connect("to_do.db")

cursors = connection.cursor()
# cursors.execute("CREATE TABLE ToDo (id INTEGER, task TEXT, done INTEGER)")

def add_values():
    print("    ADD VALUES    ")
    tid = int(input("ID :- "))
    task = input("Task :- ")
    done = int(input("Done status(0,1):- "))
    qry = f"INSERT INTO ToDo VALUES ({tid}, '{task}', {done})"
    cursors.execute(qry)
    
def read():
    select = input("Show:- ")
    where = input("Condition :- ")
    result = cursors.execute(f"SELECT {select} FROM ToDo WHERE {where}").fetchall()
    print(result)

def update():
    print("    UPDATE    ")
    column = input("(Key = Value):- ")
    where = input("Condition :- ")
    qry = f"UPDATE ToDo SET {column} WHERE {where}"
    cursors.execute(qry)

def delete():
    print("   DELETE    ")
    where = int(input("ID =  "))
    qry = f"DELETE FROM ToDo WHERE id = {where}"
    cursors.execute(qry)


def home_menu():
    default = True
    while default:
        all_data = cursors.execute("SELECT * FROM ToDo").fetchall()
        print(f"\nALL data (id INT, task TEXT, done BOOL) : - \n{all_data}")
        option = int(input('''
        1. add
        2. read
        3. update
        4. delete\n>>'''))
        if option == 1:
            add_values()
            connection.commit()
        elif option == 2:
            read()
        elif option == 3:
            update()
            connection.commit()
        elif option == 4:
            delete()
            connection.commit()
        else:
            print("Quiting ...")
            default = False


if __name__ == "__main__":
    home_menu()
    connection.commit()
    connection.close()