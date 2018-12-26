#You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in
#reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and
#returns the sum as a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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

    def sumLists(self, ll2):
        current = self.head
        secList = ll2.head
        q = 0
        while current != None and secList != None:
            sum = current.getData() + secList.getData() + q
            current.setData(sum % 10)
            q = sum // 10
            current = current.getNext()
            secList = secList.getNext()
        return self

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            if current.getNext() != None:
                print("-->", end=" ")
            current = current.getNext()
        print("\n")



if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    a = [7, 1, 6]
    b = [5, 9, 2]
    for i in a[::-1]:
        l1.insert(i)
    for j in b[::-1]:
        l2.insert(j)
    res = l1.sumLists(l2)
    res.print()

