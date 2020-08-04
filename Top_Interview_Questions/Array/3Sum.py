def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] + nums[i+1] + nums[i+2] > 0:
            break
        if nums[i] + nums[len(nums)-2] + nums[len(nums)-1] < 0:
            continue
        # Skip duplicate
        if i>0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if (tmp == 0):
                ans.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
                while (j<k and nums[j] == nums[j-1]):
                    j += 1
                while (j<k and nums[k] == nums[k+1]):
                    k -= 1
            elif (tmp < 0):
                j += 1
            else:
                k -= 1
    return ans