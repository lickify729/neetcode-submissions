class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()

        for index, num in enumerate(nums):
            if (target - num) in num_set:
                return [nums.index(target - num), index]
            else:
                num_set.add(num)
            