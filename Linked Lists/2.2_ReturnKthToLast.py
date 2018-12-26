#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

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

    def print(self, k):
        current = self.head
        while k != 1:
            current = current.getNext()
            k -= 1
        while current != None:
            print(current.getData(), end=" ")
            if current.getNext() != None:
                print("-->", end=" ")
            current = current.getNext()
        print("\n")


if __name__ == "__main__":
    myList = LinkedList()
    l = [33, 56, 34, 89, 20, 13, 5, 79]
    k = int(input("Enter the value of k: "))
    while k > len(l) or k < 1:
        print("Invalid input. The value of k should be between 1 and " + str(len(l)))
        k = int(input("Enter the value of k: "))
    for i in l:
        myList.insert(i)
    myList.print(k)
