from node import Node

class Queue:
    """Linked-list based queue with front and rear pointers."""
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value) 
        if self.rear is None: 
            self.front = self.rear = node
        else: 
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        self.front = node.next
        if self.front is None: 
            self.rear = None
        node.next = None
        return node.value 
        
    def peek(self):
        return None if self.front is None else self.front.value
        
    def is_empty(self):
        return self.front is None
        
    def print_queue(self):
        if self.front is None: 
            print("(no waiting customers)")
            return
        current = self.front
        while current: 
            print(f"- {current.value}")
            current = current.next 

def help_desk_cli():
    queue = Queue()
    menu = """ - - - Help Desk Ticketing System - - -
1. Add customer
2. Help next customer 
3. View next customer
4. View all waiting customers 
5. Exit 
Select an option:"""

    while True: 
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name == "":
                print("No name entered.")
                continue 
            queue.enqueue(name)
            print(f"{name} added to the queue.\n")

        elif choice == "2": 
            name = queue.dequeue()
            if name is None:
                print("No customers to help.\n")
            else: 
                print(f"Helped: {name}\n")

        elif choice == "3":
            nxt = queue.peek()
            if nxt is None: 
                print("No next customer.\n")
            else: 
                print(f"Next customer: {nxt}\n")
        
        elif choice == "4": 
            print("Waiting customers:")
            queue.print_queue()
            print()

        elif choice == "5":
            print("Exiting.")
            break
        else: 
            print("Invalid option. Choose 1-5.\n")

if __name__ == "__main__":
    help_desk_cli()
        
