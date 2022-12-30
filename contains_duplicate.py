#input
nums = [1,2,3,4,5]

# brute force solution

def loop_find_duplicate(nums):
    for i in range(0,len(nums)-1):
        if nums[i] in nums[i+1::]:
            return True
    return False

# sort based solution

def sort_find_duplicate(nums):
    sorted_list = sorted(nums)
    for i in range(0,len(sorted_list) -1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False

# hash table/dict based solution

def dict_find_duplicate(nums):
    hash_table = {}
    # build hash table or dict
    for i in range(0,len(nums)-1):
        if nums[i] in hash_table.keys():
            return True
        else:
            hash_table[nums[i]] = 1
    return False

# using set

def set_find_duplicate(nums):
    nums_set = set(nums)
    # convert set again to a list to make comparison
    # else you will not be able to compare set with a list
    nums_set = list(nums_set)
    if nums_set == nums:
        return False
    else:
        return True


# print results like below
print(f'Brute force result: {loop_find_duplicate(nums)}')



