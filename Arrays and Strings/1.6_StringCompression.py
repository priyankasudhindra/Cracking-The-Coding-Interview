#String Compression: Implement a method to perform basic string compression using the counts of repeated characters.


from collections import Counter

def stringCompression(st):
    count = 0
    compressed_string = ""
    c = Counter(st)
    length = len(c)
    if length * 2 > len(st):
        return st
    else:
        i = 0
        ch = st[i]
        while i < len(st):
            if st[i] == ch:
                count += 1
                i += 1
            else:
                compressed_string += ch
                compressed_string += str(count)
                count = 0
                ch = st[i]
    compressed_string += ch
    compressed_string += str(count)
    return compressed_string


if __name__ == "__main__":
    s = input("Enter a string: ")
    s = s.lower()
    res = stringCompression(s)
    print(res)