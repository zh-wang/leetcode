class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, i = len(gas), 0
        total_gas, total_cost = 0, 0 # check the total amount
        remain = 0 # remain gas if start at index 'ret'
        ret = -1 # start index of the tour, -1 mean empty
        while i < len(gas):
            total_gas += gas[i]
            total_cost += cost[i]
            remain += gas[i] - cost[i] # update remain at each slot
            if remain >= 0:
                ret = i if ret < 0 else ret # update ret if remain is positive
            else:
                remain, ret = 0, -1 # reset if remain is insufficient
            i += 1
        return ret if total_gas >= total_cost else -1
