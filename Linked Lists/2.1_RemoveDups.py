#Remove Dups! Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?


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

    def removeDups(self):
        temp = []
        previous = None
        current = self.head

        while current != None:
            if current.getData() not in temp:
                temp.append(current.getData())
                previous = current
                current = current.getNext()
            else:
                previous.setNext(current.getNext())
                current = current.getNext()

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            if current.getNext() != None:
                print("-->", end=" ")
            current = current.getNext()
        print("\n")


if __name__ == "__main__":
    myList = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    print("Enter the elements:")
    for i in range(n):
        x = input()
        myList.insert((x))
    myList.removeDups()
    myList.print()
