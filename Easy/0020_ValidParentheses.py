class Solution:
    def isValid(self, s: str) -> bool:
        brac={'(':')','[':']','{':'}'}
        stack=[]
        for ch in s:
            if ch in brac:
                stack.append(brac[ch])
            elif len(stack)!=0:
                if stack[-1]==ch:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
