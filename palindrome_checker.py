def palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def main():
    user_string = input("input the string:") 
    s = user_string.lower()
    if palindrome(s):
        print("yes.")
    else:
        print("no.")
        

main() 