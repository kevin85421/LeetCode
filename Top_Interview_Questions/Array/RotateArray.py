def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    nstep =  k % len(nums)
    if nstep == 0:
        return
    while nstep > 0:
        # iterStep
        iterStep = int(math.pow(10,int(math.log10(nstep))))
        for i in range(int(nstep / iterStep)):
            cur = nums[:iterStep]
            prev = nums[:iterStep]
            for idx in range(len(nums)):
                prev[idx%iterStep] = nums[(idx+iterStep)%len(nums)]
                nums[(idx+iterStep)%len(nums)] = cur[idx%iterStep]
                cur[idx%iterStep] = prev[idx%iterStep]
        nstep = nstep % iterStep