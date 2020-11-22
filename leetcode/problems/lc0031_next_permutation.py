from typing import List


class LC0031_Next_Permutation:

    def nextPermutation(self, nums: List[int]) -> None:

        swap1 = -1
        swap2 = len(nums) - 1

        # R to L: find first number going down (7 --> 4)
        for i in range(len(nums) - 1, 0, -1):  # loops until 1
            if nums[i - 1] < nums[i]:
                swap1 = i - 1
                break

        # L to R: from 7 to right to find first number bigger than 4 (5)
        if swap1 >= 0:
            for i in range(swap1 + 1, len(nums)):
                if nums[swap1] >= nums[i]:
                    swap2 = i - 1
                    break

            self.swap(nums, swap1, swap2)

        self.reversePartialArray(nums, swap1+1)

    def swap(self, nums, swap1, swap2):
        temp = nums[swap1]
        nums[swap1] = nums[swap2]
        nums[swap2] = temp

    def reversePartialArray(self, nums, start):
        iterations = (len(nums) - start) // 2
        for i in range(0, iterations):
            from_idx = start + i
            to_idx = len(nums) - i - 1
            self.swap(nums, from_idx, to_idx)
