def singleNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    i = 0
    while i < len(nums):
        if i == (len(nums)-1):
            return nums[i]
        elif nums[i] == nums[i+1]:
            i = i + 2
        else:
            return nums[i]