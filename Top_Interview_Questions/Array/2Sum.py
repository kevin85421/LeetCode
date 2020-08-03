def twoSum(self, nums: List[int], target: int) -> List[int]:
    cursor_start = 0
    cursor_end = len(nums) - 1
    ans = []
    sorted_nums = nums.copy()
    sorted_nums.sort()
    while cursor_start < cursor_end:
        if (sorted_nums[cursor_start] + sorted_nums[cursor_end]) == target:
            break
        elif (sorted_nums[cursor_start] + sorted_nums[cursor_end]) > target:
            cursor_end = cursor_end - 1
        else:
            cursor_start = cursor_start + 1
    if sorted_nums[cursor_start] == sorted_nums[cursor_end]:
        ans.append(nums.index(sorted_nums[cursor_start]))
        ans.append(nums.index(sorted_nums[cursor_end],ans[0]+1))
    else:
        ans.append(nums.index(sorted_nums[cursor_start]))
        ans.append(nums.index(sorted_nums[cursor_end]))
    ans.sort()
    return ans