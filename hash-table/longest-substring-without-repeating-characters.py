# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        # print(s)
        # i=0
        # j=0
        # record = {}
        # blocking = None
        
        # if len(s) == 0:
        #     return 0
        # max = 1
        # record[s[0]] = 1
        # while(j<len(s)):
        #     print(i,j)
        #     if blocking == None:
        #         j += 1
        #         if j >= len(s):
        #             break
        #         if s[j] in record:
        #             print('blocking', s[j])
        #             blocking = s[j]
        #             continue
        #         else:
        #             print('record add', s[j])
        #             record[s[j]] = 1
        #             if (j-i + 1) > max:
        #                 max = j - i + 1
        #     else:
        #         if blocking == s[i]:
        #             print('deblocking', blocking)
        #             blocking = None
        #         else:
        #             print('record del', s[i])
        #             del record[s[i]]
        #         i += 1
        #         if (j-i + 1) > max:
        #                 max = j - i + 1
        #     pass
        # return max

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # method 2 sliding window + hash set
        chars= set()
        i = 0
        max_length = 0
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            max_length = max(max_length, j-i+1)
        return max_length
        # method 1 brute force
        # max_length = 0
       
        # for i in range(len(s)):
        #     chars = set()
        #     for j in range(i,len(s)):
        #         if s[j] in chars:
        #             break
        #         chars.add(s[j])
        #         max_length = max(max_length, j-i+1)
        # return max_length






