import functools
def longestCommonPrefix(strs) -> str:
    minLen = len(functools.reduce(lambda x,y: x if len(x)< len(y) else y,strs))
    res = ""
    firstString = strs[0]
    for i in range(0,minLen):
        foundInAll = True
        for j in range(1,len(strs)):
            if strs[j][i] != firstString[i]:
                foundInAll = False
                break
        if foundInAll:
            res+=firstString[i]
        else:
            return res
    return res

strs = ["flower","flight","flow"]

print(f'result is : {longestCommonPrefix(strs)}')