# find out num is palindrome or not?

num = int(input("Enter number: "))

def isPalindrome(num):
    tmp = num
    r_num = 0
    if num < 0: 
        return False 

    while num != 0:
        r_num = num%10 + 10* r_num
        num = num // 10
    
    if tmp == r_num:
        return True
    else:
        return False

res = isPalindrome(num)

print(f'Is Palindrome: {res}')