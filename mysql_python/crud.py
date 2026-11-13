from conn import get_connection
c = get_connection()
cursor = c.cursor()

def create():
    tablename = input("Enter table name: ")
    c1 = input("Enter ID:")
    c2 = input("Enter name: ")
    c3 = input("Enter age:")
    c4 = input("Enter city: ")

    query = f"""CREATE TABLE {tablename}(
    {c1} int primary key AUTO_INCREMENT,
    {c2} VARCHAR(20),
    {c3} int,
    {c4} VARCHAR(20))"""

    cursor.execute(query)
    print("Table created")

def insert():
    tablename = input("Enter table name: ")
    c2 = input("Enter name: ")
    c3 = input("Enter age:")
    c4 = input("Enter city: ")

    v1 = input(f"Enter value for {c2}: ")
    v2 = input(f"Enter value for {c3}: ")
    v3 = input(f"Enter value for {c4}: ")

    query = f"""INSERT INTO {tablename}(
        {c2},{c3},{c4}) VALUES(%s,%s,%s)"""

    cursor.execute(query, (v1, v2, v3))
    c.commit()
    print("INSERTED")

def update():
    tablename = input("Enter table name: ")
    c2 = input("Enter name: ")
    c3 = input("Enter age:")
    c4 = input("Enter city: ")
    u1 = input("Enter name to update:")
    u2 = int(input("Enter new age: "))
    
    query = f"""UPDATE {tablename} SET {c3} = %s WHERE {c2} = %s"""
    cursor.execute(query, (u2, u1))
    c.commit()
    print("UPDATED")

def delete():
    tablename = input("Enter table name: ")
    c2 = input("Enter name column name: ")
    name = input("enter name to delete")

    query = f"DELETE FROM {tablename} WHERE {c2} = %s"
    cursor.execute(query, (name,))
    c.commit()
    print("DELETED")

def select():
    tablename = input("Enter table name: ")
    coloum = input("Enter coloum name: ")
    query = f"SELECT {coloum} FROM {tablename}"
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)

while True:
    print("\n1. Create Table")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Select Data")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create()
    elif choice == 2:
        insert()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        select()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
cursor.close()
c.close()