class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r1 = (C - A) * (D - B)
        r2 = (G - E) * (H - F)
        if C < E or G < A or D < F or H < B:
            return r1 + r2
        overlap = (min(C, G) - max(A, E)) * (min(H, D) - max(B, F))
        return r1 + r2 - overlap
