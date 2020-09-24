class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([])
            for j in range(i+1):
                if j == 0:
                    ans[-1].append(1)
                elif j == i:
                    ans[-1].append(1)
                else:
                    ans[-1].append(ans[-2][j-1] + ans[-2][j])
        return ans