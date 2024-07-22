class Node:                 #Node Blueprint
    def __init__ (self,d):  #initialising Node structure 
        self.data = d       #Data
        self.next = None    # Next pointer address

class Main:                 
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,d):
        newN = Node(d)
        if (self.head == None):
            self.head = newN
            self.tail = newN
        else:
            self.tail.next = newN
            self.tail = newN
    def traversing(self):
        temp = self.head
        print("The linkedList datas are: ")
        while temp != None:
            print("->",temp.data, end = ' ')
            temp = temp.next
    def delete_first(self):
        if(self.head != None):
            self.head = self.head.next
    def delete_last(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next



obj = Main() #calling class and created instance object (obj)
#taking input
print("Enter Input:")
n = int(input())
while n > 0 :
    obj.insert(n)
    n = int(input())
#calling traversing
obj.traversing()
