class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            v = data[i]
            if v < 0 or v > 255:
                return False
            if v & 128 == 0: # 0xxxxxxx (1-byte length)
                i += 1
            else:
                k1, k2, k3 = False, False, False
                if i + 1 < len(data) and data[i + 1] >> 6 == 0b10:
                    k1 = True
                if i + 2 < len(data) and data[i + 2] >> 6 == 0b10:
                    k2 = True
                if i + 3 < len(data) and data[i + 3] >> 6 == 0b10:
                    k3 = True
                if v >> 5 == 0b110 and k1:
                    i += 2
                    continue
                elif v >> 4 == 0b1110 and k1 and k2:
                    i += 3
                    continue
                elif v >> 3 == 0b11110 and k1 and k2 and k3:
                    i += 4
                    continue
                return False
        return True
