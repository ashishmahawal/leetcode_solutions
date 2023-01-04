# password generator
import random
import string

def generate_password(password_len):
    lc = list(string.ascii_lowercase)
    uc = list(string.ascii_uppercase)
    nums = list(range(0,10))
    sc = ['@','#','^','&','!']
    passowrd = ''
    bowl = [lc,uc,nums,sc]
    for i in range(0,password_len):
        r_index_bowl = random.randrange(0,len(bowl))
        picked_list = bowl[r_index_bowl]

        r_index_picked_list = random.randrange(0,len(picked_list))
        r_element = picked_list[r_index_picked_list]

        passowrd += str(r_element)
    return passowrd


# take input from user password len
password_len = int(input("Please input password length: "))
print(generate_password(password_len))
