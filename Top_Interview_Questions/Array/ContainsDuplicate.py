def containsDuplicate(self, nums: List[int]) -> bool:
    res = False
    nums.sort()
    for idx in range(len(nums)-1):
        if (nums[idx] == nums[idx+1]):
            return True
    return res