#String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring of another.
#Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring


from collections import Counter


def stringRotation(st1, st2):
    if len(st1) != len(st2):
        return False
    else:
        c1 = Counter(st1)
        c2 = Counter(st2)
        if c1 != c2:
            return False
        else:
            st3 = st1 + st1
            if st3.find(st2) == -1:
                return False
            else:
                return True


if __name__ == "__main__":
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    s1.lower()
    s2.lower()
    res = stringRotation(s1, s2)
    print(res)
