class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        if len(strs)!=0:
            short=min(strs,key=len)
            for i in range(len(short)):
                if all(short[i]==word[i] for word in strs):
                    result+=short[i]
                else:
                    return result
            return result
        else:
            return result
