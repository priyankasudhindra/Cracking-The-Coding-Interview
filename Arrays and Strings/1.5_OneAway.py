#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
#or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.


def oneAway(st1, st2):
    st1 = set(st1)
    st2 = set(st2)
    diff = st1 - st2
    if len(diff) > 1:
        return False
    else:
        return True


if __name__ == "__main__":
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    s1.lower()
    s2.lower()
    res = oneAway(s1, s2)
    print(res)
