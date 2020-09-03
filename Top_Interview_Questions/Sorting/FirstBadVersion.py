# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        low = 1
        high = n
        while True:
            ans = int((low + high)/2)
            if isBadVersion(ans):
                if not isBadVersion(ans-1):
                    return ans
                high = ans
            else:
                if isBadVersion(ans+1):
                    return ans + 1
                low = ans
        return ans