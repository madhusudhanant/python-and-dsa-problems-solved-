class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating
def create():
    n = int(input("Enter count: "))
    nodes = []
    for i in range(n):
        v = int(input('enter value: '))
        x = node(v)
        nodes.append(x)
    
    for i in range(len(nodes) - 1): #link
        nodes[i].next = nodes[i+1]
    return nodes[0]

'''
[ [data] [ [data] [ [ data] [none]]] 


'''
#display

def display(first):
    if first is None:
        print("linked list empty")
        return
    temp = first
    while temp:
        print(temp.data,end="-->")
        temp = temp.next
    print("None")

# insert

def insert(first):
    v = int(input('enter value to insert: '))
    newnode = node(v)

    if first is None:
        first = newnode
        return first
    temp = first

    while temp.next:
        temp = temp.next
    temp.next = newnode
    print("INSERTED")
    return first


# SEARCH
def search(first):
    search = int(input('enter value to search: '))
    temp = first
    found = 0
    while temp:
        if temp.data == search:
            found = 1
            break
        temp = temp.next
    if found == 1:
        print('value found')
    else:
        print('value not found')

#Update
def update(first):
    old = int(input('enter old value: '))
    new = int(input('enter new value: '))
    temp = first
    updated = 0
    while temp:
        if temp.data == old:
            temp.data = new
            updated = 1
            break
        temp = temp.next
    if updated == 1:
        print("value updated")
    else:
        print("value not found")

#Delete
def delete(first):
    delete_val = int(input("Enter value to delete"))
    temp = first
    prev = None
    deleted = 0

    #Delete first node
    if first and first.data == delete_val:
        first = first.next
        deleted = 1
    else:
        while temp:
            if temp.data == delete_val:
                prev.next = temp.next
                deleted = 1
                break
            prev = temp
            temp = temp.next
    if deleted == 1:
        print("value deleted")
    else:
        print("value not found")
    return first

while True:

    print("\n----- LINKED LIST MENU -----")
    print("1. Create")
    print("2. Display")
    print("3. Insert")
    print("4. Search")
    print("5. Update")
    print("6. Delete")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        first = create()

    elif choice == 2:
        display(first)

    elif choice == 3:
        first = insert(first)

    elif choice == 4:
        search(first)

    elif choice == 5:
        update(first)

    elif choice == 6:
        first = delete(first)

    elif choice == 7:
        print("Program End")
        break

    else:
        print("Invalid Choice")































