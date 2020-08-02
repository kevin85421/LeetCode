def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nzero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nzero = nzero + 1
        else:
            nums[i-nzero] = nums[i]
    for i in range(nzero):
        nums[len(nums)-i-1] = 0