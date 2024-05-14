class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        length=len(nums)
        pos=0
        for i in range(length):
            if(nums[i]<=k):
                el=nums[i]
                nums[i]=51
                if(el in nums):
                    continue
                pos=i
                break
        return length-pos