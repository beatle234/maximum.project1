def checkPalindrome(n):
    centr = len(n)//2
    for i in range(centr):
        if n(i)!=n[len(n)-i]:
            return False
    return True

print(checkPalindrome('лепсспел'))


