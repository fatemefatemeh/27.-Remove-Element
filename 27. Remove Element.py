class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size=len(nums)
        while val in nums:
                nums.remove(val)
        return size
        
        