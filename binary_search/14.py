class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start) // 2
            if nums[mid] < target:
                start = mid 
            else:
                end = mid 
        
        if nums[start] == target:
            return start 
        elif nums[end] == target:
            return end
        return -1 