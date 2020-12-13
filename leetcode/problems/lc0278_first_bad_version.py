# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# This is here just to compile, but can only be run from here:
# https://leetcode.com/problems/first-bad-version/
def isBadVersion(n):
    return True

class LC0278_First_Bad_Version:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            if not isBadVersion(mid):
                left = mid + 1
            elif mid == 1 or not isBadVersion(mid - 1):
                return mid
            else:
                right = mid - 1

        return -1