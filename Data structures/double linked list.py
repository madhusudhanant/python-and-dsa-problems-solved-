
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # CREATE / INSERT
    def insert(self, data):
        new_node = Node(data)
        # Empty list
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    # DISPLAY
    def display(self):
        temp = self.head
        print("\nDoubly Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

    # FORWARD PRINT
    def forward_print(self):
        temp = self.head
        print("\nForward Printing:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
    def backward_print(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        # Move to last node
        while temp.next:
            temp = temp.next
        print("\nBackward Printing:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.prev
        print("None")
    def update(self, old_value, new_value):
        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                print(f"{old_value} updated to {new_value}")
                return
            temp = temp.next

        print("Value not found")
    def delete(self, value):
        # Empty list
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        # Delete first node
        if temp.data == value:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"{value} deleted")
            return
        # Search node
        while temp and temp.data != value:
            temp = temp.next
        # Value not found
        if temp is None:
            print("Value not found")
            return
        # Delete middle / last node
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        print(f"{value} deleted")



dll = DoublyLinkedList()
while True:
    print("\n===== DOUBLY LINKED LIST MENU =====")
    print("1. Create / Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Forward Print")
    print("6. Backward Print")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("How many nodes: "))
        for i in range(n):
            value = int(input("Enter value: "))
            dll.insert(value)
        print("Nodes inserted successfully")
    elif choice == 2:
        dll.display()
    elif choice == 3:
        old_value = int(input("Enter old value: "))
        new_value = int(input("Enter new value: "))
        dll.update(old_value, new_value)
    elif choice == 4:
        value = int(input("Enter delete value: "))
        dll.delete(value)
    elif choice == 5:
        dll.forward_print()
    elif choice == 6:
        dll.backward_print()
    elif choice == 7:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
