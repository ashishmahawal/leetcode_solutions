def lengthOfLongestSubstring(s: str) -> int:
    max_win = 0
    win_list = []
    size = 0
    for char in s:
        if size > max_win:
                max_win = size
        if char in win_list:
            while char in win_list:
                win_list.pop(0)
                size-=1 
            win_list.append(char)
            size += 1
        else:
            win_list.append(char)
            size+=1
    return max_win if max_win > size else size

res = lengthOfLongestSubstring("dvdf")
print(res)