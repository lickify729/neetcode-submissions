class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fish = {}
        for i in nums:
            if i not in fish:
                fish[i] = 1
            else:
                fish[i] += 1

        sorted_by_frequency = sorted(
            fish.items(), key=lambda x: x[1]
        )
        return [x[0] for x in sorted_by_frequency[-k:]]