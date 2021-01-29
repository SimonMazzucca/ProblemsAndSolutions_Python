from typing import List


class LC0088_Merge_Sorted_Array:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        last = m + n - 1

        for p in range(last, -1, -1):

            if p2 < 0:
                break
            elif p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

