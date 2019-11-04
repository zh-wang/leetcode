class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        # modify heaters array to use the following method easier
        heaters.insert(0, -1 << 32)
        heaters.append(1 << 32)
        ret = 0
        i, j = 0, 1 # a pair of heaters where a house should locate between them
        for pHouse in houses:
            if pHouse <= heaters[i]: # house is left to i-th heater
                ret = max(ret, heaters[i] - pHouse) # so the left heater is the best result
            elif pHouse <= heaters[j]: # house is between i-th and j-th heater
                ret = max(ret, min(heaters[j] - pHouse, pHouse - heaters[i]))
            else: # house is right to j-th heater
                # then we will move i, j to fit the house
                while j < len(heaters) and pHouse > heaters[j]:
                    i, j = i+1, j+1
                ret = max(ret, min(heaters[j] - pHouse, pHouse - heaters[i]))
        return ret
