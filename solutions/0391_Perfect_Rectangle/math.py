import collections

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        xmin, xmax = 1 << 32, 0
        ymin, ymax = 1 << 32, 0
        area = 0
        for rec in rectangles:
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            xmin, xmax = min(rec[0], xmin), max(rec[2], xmax)
            ymin, ymax = min(rec[1], ymin), max(rec[3], ymax)
        if area != (xmax - xmin) * (ymax - ymin):
            return False

        corners = collections.defaultdict(int)
        # add the out most four corners
        corners[(xmin, ymin)] += 1
        corners[(xmax, ymin)] += 1
        corners[(xmin, ymax)] += 1
        corners[(xmax, ymax)] += 1

        for rec in rectangles:
            corners[(rec[0], rec[1])] += 1
            corners[(rec[0], rec[3])] += 1
            corners[(rec[2], rec[1])] += 1
            corners[(rec[2], rec[3])] += 1
        return not any(map(lambda g: g % 2, corners.values()))
