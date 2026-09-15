class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        rom={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        for i in range(len(s)-1):
            first=rom[s[i]]
            second=rom[s[i+1]]
            if first<second:
                result-=first
            else:
                result+=first
        result+=rom[s[-1]]
        return result
