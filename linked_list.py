class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    def print_list(self):
        current = self.head
        num_of_nodes = 0
        while current:
         print current.data
         current = current.get_next()
         num_of_nodes = num_of_nodes + 1
        print "Total nodes: " + str(num_of_nodes)

     
    def has_cycle(self): 
      slow_p = self.head 
      fast_p = self.head 
      while(slow_p and fast_p and fast_p.next): 
       slow_p = slow_p.next 
       fast_p = fast_p.next.next 
       if slow_p == fast_p: 
         print "Found Loop"
      return

ll = LinkedList() 
ll.insert("node1")
ll.insert("node2")
ll.insert("node3")
ll.insert("node4")
ll.insert("node5")
ll.print_list()
print ll.has_cycle()
