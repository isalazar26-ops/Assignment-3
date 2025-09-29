from node import Node 

class Stack: 
    "Simple linked-list based stack using Node.""" 
    def _init_(self): 
        self.top = None 

    def push(self, value):
        node = Node(value)
        node.next = self.top 
        self.top = node 

    def pop(self): 
        if self.top is None: 
            return None
        node = self.top 
        self.top = node.next 
        node.next = None 
        return node.value 
    
    def peek(self): 
        return None if self.top is None else self.top.value 
    
    def is_empty(self):
        return self.top is None 
    
    def print_stack(self): 
        if self.top is None: 
            print("(empty)")
            return
        current = self.top
        items = []
        while current: 
            items.append(current.value)
            current = current.next
        for item in items: 
            print(f"- {item}")

def undo_redo_cli(): 
    undo_stack = Stack()
    redo_stack = Stack()

    menu = """- - - Undo/Redo Managerv - - -
1. Perform action
2. Undo
3. Redo 
4. View Undo Stack 
5. View Redo Stack 
6. Exit 
Select an option: """

    while True: 
        try: 
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt): 
            print("\nExiting.")
            break 

        if choice == "1": 
            action = input("describe the action (e.g., Insert 'a'):").rstrip()
            if action == "":
                print("No action entered.")
                continue 
            undo_stack.push(action) 
            # clear redo stack by creating a new Stack instance
            redo_stack = Stack()
            print(f"Action performed: {action}\n")

        elif choice == "2":
            val = undo_stack.pop()
            if val is None:
                print("No actions to redo.\n")
            else: 
                redo_stack.push(val)
                print(f"Undid action: {val}\n")

        elif choice == "3":
            val = redo_stack.pop()
            if val is None:
                print("No actions to redo.\n")
            else:
                undo_stack.push(val)
                print(f"Redid action: {val}\n")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()
            print()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()
            print()

        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invaid option. Choose 106.\n")

if __name__ == "__main__":
    undo_redo_cli()
