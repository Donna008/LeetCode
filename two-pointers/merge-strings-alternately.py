class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                # move the pointer to next
                i+=1
            if j < len(word2):
                result += word2[j]
                j +=1
        return result
