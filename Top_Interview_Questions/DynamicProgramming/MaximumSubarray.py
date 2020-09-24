class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_value = nums[0]
        for i in range(len(nums)-1):
            if max_so_far > 0:
                max_so_far = max_so_far + nums[i+1]
            else:
                max_so_far = nums[i+1]
            if max_value < max_so_far:
                max_value = max_so_far
        return max_value