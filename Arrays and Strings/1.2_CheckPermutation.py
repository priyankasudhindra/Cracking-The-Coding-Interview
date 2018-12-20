#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def checkPermutation(st1, st2):
    st1 = list(st1)
    st2 = list(st2)
    st1.sort()
    st2.sort()
    if st1 == st2:
        return "Permutation"
    else:
        return "Not a Permutation"


if __name__ == "__main__":
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if len(s1) != len(s2):
        print("Not a Permutation")
    else:
        res = checkPermutation(s1, s2)
        print(res)
