class Node:
  def __init__(self,initial):
    self.data = initial
    self.next = None
  def getData(self):
    return self.data
  def setData(self,data):
    self.data = data
  def getNext(self):
    return self.next
  def setNext(self,aNode):
    self.next = aNode 

class LinkedList:
  def __init__(self):
    self.head = None
  def add(self,item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
  def isEmpty(self):
    return self.head == None
  def size(self):
    current = self.head
    counts = 0
    while current != None:
      current = current.getNext()
      counts += 1
    return counts
  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found
  def remove(self,item):
  """这个remove只能移除能够search到的元素,而不是任合元素"""
    current = self.head
    previous = None
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
   
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())
    


if __name__=='__main__':
  ll=LinkedList()
  for i in range(90, 1, -10):
    ll.add(i)
  print ll.size()
  print ll.search(25),ll.search(10)
  ll.remove(100)
  print ll.size()
