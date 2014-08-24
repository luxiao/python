class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
    def getData(self):
        return self.data
    def setData(self,value):
        self.data = value
    def getNext(self):
        return self.next
    def setNext(self,node):
        self.next = node

class OrderedList:
    def __init__(self):
        self.head = None   
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        s = 0
        while current != None:
            s += 1
            current = current.getNext()

        return s
    def search(self, item):
        cur = self.head
        found = False
        stop = False
        while cur !=None and not found and not stop:
            if cur.getData() == item:
                found = True
            elif cur.getData() > item:
                stop = True
            else:
                cur = cur.getNext()
                
        return found
    def add(self, item):
        cur = self.head
        stop = False
        previous = None
        while cur != None and not stop:
            if cur.getData() > item:
                stop = True
            else:
                previous = cur
                cur = cur.getNext()
        tmp = Node(item)
        if previous == None:
            tmp.setNext(self.head)
            self.head = tmp
        else:
            tmp.setNext(previous.getNext())
            previous.setNext(tmp)

if __name__ == '__main__':
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    print mylist.head.getData()
    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
    mylist.add(26)
    print mylist.head.getData()
    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
    mylist.add(54)
    print mylist.head.getData()
    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
            
        
