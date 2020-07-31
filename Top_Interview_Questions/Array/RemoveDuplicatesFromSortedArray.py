class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curLength = 0
        for i in range(len(nums)):
            if(nums[curLength] != nums[i]):
                curLength = curLength + 1
                nums[curLength] = nums[i]
        nums = nums[:curLength+1]
        return len(nums)