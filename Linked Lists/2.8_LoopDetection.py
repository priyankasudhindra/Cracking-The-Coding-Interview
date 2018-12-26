#Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
#beginning of the loop.

from collections import Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def loopDetection(self):
        a = []
        current = self.head
        while current != None:
            a.append(current.getData())
            current = current.getNext()
        c = Counter(a)
        for k, v in c.items():
            if v > 1:
                return k
        else:
            return "No Loop detected!"


if __name__ == "__main__":
    myList = LinkedList()
    l = ['A', 'B', 'C', 'D', 'E', 'C']
    for i in l:
        myList.insert(i)
    result = myList.loopDetection()
    print(result)