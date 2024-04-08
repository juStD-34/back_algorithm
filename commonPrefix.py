def longestCommonPrefix(self, strs) -> str:
    strs.sort()
    smallStr = strs[0]
    bigStr = strs[-1]
    ans = ""
    for i in range (min(len(smallStr), len(bigStr))):
        if (smallStr[i] != bigStr[i]):
            return ans
        ans += smallStr[i]
    return ans

print(longestCommonPrefix(0,["flower","flow","flight"]))