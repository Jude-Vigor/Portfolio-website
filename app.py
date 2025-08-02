s = "madamy"
def palindrome(s):
    for i in range(len(s)):
        if s == s[::-1]:
            return True 
        print(palindrome(s))