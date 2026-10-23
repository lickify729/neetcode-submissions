class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums2 = []
        #for i in nums:
            #if i in nums2:
                #return True
            #nums2.append(i)
        #return False

        num_set = set()

        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False