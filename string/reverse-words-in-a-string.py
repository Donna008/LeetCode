# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.strip().split()
#         words.reverse()
#         return ' '.join(words)

class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.strip()
        words=s.strip().split()
        words.reverse()
        return " ".join(words)






