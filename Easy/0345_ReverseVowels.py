class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vowel = 'aeiouAEIOU'
        i , j = 0 , len(word)-1
        while i < j:
            if word[i] in vowel and word[j] in vowel:
                word[i] , word[j] = word[j] , word[i]
                i += 1
                j -= 1
            elif word[i] not in vowel:
                i += 1
            else:
                j -= 1
        return ''.join(word)
