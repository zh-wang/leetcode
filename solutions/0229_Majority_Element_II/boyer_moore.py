class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        m1, m2 = None, None
        c1, c2 = 0, 0
        for v in nums:
            if m1 == v: # m1 is already voted
                c1 += 1
                continue
            if m2 == v: # m2 is already voted
                c2 += 1
                continue
            if c1 == 0: # m1 is empty and can be voted
                m1, c1 = v, 1
                continue
            if c2 == 0: # m2 is empty and can be voted
                m2, c2 = v, 1
                continue
            # no empty, we have to remove both votes
            # why?
            c1 -= 1
            c2 -= 1

        c1 = nums.count(m1)
        c2 = nums.count(m2)

        ret = []
        if c1 > len(nums) // 3:
            ret += [m1]
        if c2 > len(nums) // 3:
            ret += [m2]

        return ret
