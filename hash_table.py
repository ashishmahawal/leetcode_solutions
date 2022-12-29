# implementing hash table using dict

hash_table = {
    0:1,
    1:1,
    3:0
}

hash_table_2 = {
    "a":"apple",
    "b":"banana"
}

check = "b"

if check in hash_table_2.keys():
    print(hash_table_2[check])
else:
    print(f'Missing {check} key')