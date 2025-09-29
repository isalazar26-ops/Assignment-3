class Node: 
    """
    Simple Node class for linked structures. 
    Attributes: 
    value: stored value 
    next: pointer to next node (None by default)
    """
    def _init_(sepf, value):
        self.value = value 
        self.next = None 

    def _repre_(self): 
        return f"Node({self.value!r})"
