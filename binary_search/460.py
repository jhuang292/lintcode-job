class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        right = self.find_uppper_closet(A, target)
        left = right - 1 
        
        results = []
        for _ in range(k):
            if self.is_left_closer(A, left, right, target):
                results.append(A[left])
                left -= 1 
            else:
                results.append(A[right])
                right += 1 
        return results
                

    def find_uppper_closet(self, A, target):
        
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid 
            else:
                start = mid
            
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end 
        return end + 1 
        
    def is_left_closer(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
            
