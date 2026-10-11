class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        key1 = set('qwertyuiop')
        key2 = set('asdfghjkl')
        key3 = set('zxcvbnm')
        result = []
        for i in range(len(words)):
            word = set(words[i].lower())
            if word.issubset(key1) or word.issubset(key2) or word.issubset(key3):
                result.append(words[i])
        return result
