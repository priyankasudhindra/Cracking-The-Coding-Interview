#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
#A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
#The palindrome does not need to be limited to just dictionary words.


from collections import Counter


def palindromePermutation(st):
    odd = 0
    st = list(st)
    while ' ' in st:
        st.remove(' ')
    c = Counter(st)
    c = list(c.values())
    for i in c:
        if i % 2 != 0:
            odd += 1
            if odd > 1:
                return "False"
    else:
        return "True"



if __name__ == "__main__":
    s = input("Enter a string: ")
    s = s.lower()
    res = palindromePermutation(s)
    print(res)
