from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Case 1 -- If the cache is not full then add to fill
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
       
        # Case 2 -- If the cache is at its capacity remove head
        # and replace it with a new value
        elif self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        
        #to retain appropriate order
        else:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        #First we must loop through the cache 
        while current is not None:
            #append to fill the list
            list_buffer_contents.append(current.value)
            #repeat appending
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
