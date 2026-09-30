class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        res = ''
        j = len(str_list)-1
        while j>=0:
            res+=str_list[j]
            j-=1
            if j>=0:
                res += ' '
        return res
