"""
Given an integer array nums of size n, 
return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the 
largest value.
"""
class solution:
    """
understanding the question we are given an array which contains a list of num
with a size n , now we are asked to return the num thats closest to zero 
"""
    
    def findClosestNumber(self, nums):#, nums: list[int]):
        """
using a class we defined a function and we created a variable closest , here this
variable we assume that the first item is the nearest to zero 
"""        
        

        closest = nums[0]
        """
so for us to comfirm this we have to actually loop through all our item , now as we loop
through each item we have to pass a condition that if the absolute value of each item is less
than that of our initial closest item then if its true we then have a new smallest item
but if dont nothing happens 
"""
        for _ in nums:
            if abs(_) < abs(closest):
                closest = _
        """
now to comfirm our smallest number it passes a last condition since the question states if
there are repeated elements , now if the abs value of the item and the absolute value closest
to zero is in nums(the array given) we should then return the abs closest else we return the
closest.
"""
        if abs(_) < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest


nums = [-4,-2,1,4,8]
a =solution()
print(a.findClosestNumber(nums))
 
