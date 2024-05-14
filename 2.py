class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=0
        for i in nums:
            for j in range(index+1,len(nums)):
                if(nums[j]+i==target):
                    return [index,j]
            index=index+1