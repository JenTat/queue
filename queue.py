'''
@author: Jen Tat

'''


class ListNode:
##    '''
##    Class of listNode is a data type which holds a value and a link to the next
##    node in a list. This object is used in conjunction with linked list
##    '''
    
    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return self._value


    

class Queue:
    
    def __init__(self):
##    '''
##    Create an empty queue.
##    '''
        self._length = 0
        self._top = None
        self._tail = None

    
    def empty(self):
##    '''
##    Determine if the queue is empty.
##
##    Returns
##    True if queue is empty, False if not.
##    '''
        return self._length == 0


    
    def insert(self, value):
##    '''
##    Insert a value at the tail of the queue.
##    Similar code to the insertNewLastNode function from LinkedLists
##
##    Params
##    value is any data type to be added to queue.
##    '''
        newNode = ListNode(value)
        
        if (self._top == None):
            self._top = newNode
            self._tail = newNode

        else:
            self._tail.newlink(newNode)
            self._tail = newNode
            
        self._length += 1
    


    def remove(self):
##    '''
##    Remove the first item from the head of the queue.
##    If list is empty then return None.
##    Similar to the removeFirstNode function from LinkedList
##
##    Returns
##    value at the head of the queue. If queue is empty return None.
##    '''
        if (self._top == None):
            return None
        elif (self._top == self._tail):
            n = self._top
            self._top = None
            self._tail = None
            self._length -= 1
            return n.value()
        else:
            n = self._top
            self._top = self._top.link()
            self._length -= 1
            return n.value()
    
    
    def peek(self):
##    '''
##    Return the value of the item at the head of the queue without removing it.
##    If queue is empty return None.
##
##    Returns
##    The value of the first item. If empty return None.
##    '''
        if (self._top == None):
            return None
        else:
            n = self._top
            return n.value()

    
    def __str__(self):
##    '''
##    Provide the string representation for the queue to appear
##    as a Python List. Used with Python's built in print function.
##    [item, item, item]
##
##    Returns
##    String
##    '''
       n = self._top
       s = ""
       while (n != None):
           s += str(n.value())+ " "
           n = n.link()
       return s     
    
  
