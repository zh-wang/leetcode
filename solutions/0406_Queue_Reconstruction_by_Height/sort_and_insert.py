// ⭐️

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort input array by descending order on the first element,
        # and ascending order on the sceond element
        people.sort(key=lambda x: (-x[0], x[1]))
        ret = []
        # inserting people from tallest to lowest,
        # into position pair[1]
        for pair in people:
            ret.insert(pair[1], pair)
        return ret
