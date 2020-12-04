class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            v = data[i]
            if v < 0 or v > 255:
                return False
            # read 0 or 1's in the first byte
            if v & 128 == 0: # 0xxxxxxx (1-byte length)
                i += 1
            else:
                # count 1's freq
                mask, cnt = 128, 0
                while (v & mask) and (cnt < 4):
                    cnt += 1
                    mask >>= 1
                # Invalid if first byte is like 10xxxxx
                if cnt == 1:
                    return False
                # Invalid if next bit is not 0
                if v & mask:
                    return False
                # Invalid when no space for (n - 1) following bytes
                if i + cnt> len(data):
                    return False
                # check (n - 1) following bytes
                for j in range(i + 1, i + cnt):
                    if data[j] >> 6 != 2:
                        return False
                i += cnt
        return True
