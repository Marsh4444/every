"""
Given an integer array nums, return true if any value appears
at least twice in the array,
and return false if every element is distinct.

understanding the question;

the question is trying to say if we are given an array that contains int
nums i.e [1,2,3,4], we are to return true if any array contains duplicate
or false if there isnt
"""
"""
class Solution:

    def not_duplicate(self, nums):

        b = len(nums)
        
        
        for x in range(b):
            for y in range(x+1, b):
                if nums[x] == nums[y] :
                    return True
            
        return False


nums = [1,2,4,5]
a = Solution()
b = a.not_duplicate(nums)
print(b)
"""
class Solution:
    def has_duplicate(self, nums):
        seen = {}
        
        for num in nums:
            # TODO: Check if num is in seen
            if num in seen:
            # If yes, return True
                return True
            else:   
            # If no, add it to seen
                seen.add(num) 
        
        return False

numbers = [1,2,3,4,1]
a = Solution()
print(a.has_duplicate(numbers))
print(type(seen))














































