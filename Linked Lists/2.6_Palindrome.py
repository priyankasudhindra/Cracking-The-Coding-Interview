#Palindrome: Implement a function to check if a linked list is a palindrome.

from random import randint

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

    def checkPalindrome(self):
        palindrome = True
        original = LinkedList()
        current = self.head
        while current != None:
            original.insert(current.getData())
            current = current.getNext()
        o_current = original.head
        current = self.head
        while current != None and o_current != None:
            if o_current.getData() == current.getData():
                current = current.getNext()
                o_current = o_current.getNext()
            else:
                palindrome = False
                break
        if palindrome == True:
            print("Palindrome")
        else:
            print("Not a Palindrome")

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
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in l:
        myList.insert(i)
    myList.checkPalindrome()
