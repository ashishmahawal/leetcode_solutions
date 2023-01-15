def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    charSet = set()
    max_size = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        max_size = max(max_size,r - l + 1)
    return max_size

res = lengthOfLongestSubstring("dvdf")
print(res)