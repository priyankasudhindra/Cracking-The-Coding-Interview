#Is Unique: Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?


def isUnique(st):
    s.sort()
    i = 0
    j = 1
    while j < len(st):
        if st[i] != st[j]:
            i += 1
            j += 1
        else:
            return "Not Unique"
    return "Unique"


if __name__ == "__main__":
    s = input("Enter a string: ")
    s = s.lower()
    s = list(s)
    res = isUnique(s)
    print(res)
