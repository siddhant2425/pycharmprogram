#
#
#
# def palindrome(s):
#     temp=s[::-1]
#     if s==temp:
#         print("palindrome")
#     else:
#         print("not palindrome")
#
# palindrome('aba')

def no_check(n):
    prime = True
    for i in range(2,n):
        if (n % i == 0):
            prime = False

        if prime:
            print("prime no")
            break
        else:
            print("not")
            break

no_check(12)
