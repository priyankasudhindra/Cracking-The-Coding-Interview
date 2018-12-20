#URLify: Write a method to replace all spaces in a string with '%20'.
#You may assume that the string has sufficient space at the end to hold the additional characters,
#and that you are given the "true" length of the string.


def URLify(st):
    st = st.replace(' ', '%20')
    return st


if __name__ == "__main__":
    s = input("Enter a string: ")
    c = int(input("Enter the number of characters: "))
    if len(s) > c:
        s = s[:c]
    res = URLify(s)
    print(res)
