"""
Problem:
You are given two strings word1 and word2. Merge the strings
by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional
letters onto the end of the merged string.
"""

class Solution:
    def merge_alternately(self, word1, word2):


        result = ""
        max_length = max(len(word1), len(word2))

        for i in range(max_length):

            if  i < len(word1) :
                result = result + word1[i]
            #else:
            #    result = result + word2[i]

            if i < len(word2)  :
                result = result + word2[i]
            #else:
            #    result = result + word1[i]

        return result


word1 = "abcer"
word2 = "def"

a = Solution()
b = a.merge_alternately(word1, word2)
print(b)