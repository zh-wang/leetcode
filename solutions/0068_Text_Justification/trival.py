class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        line_num, line_w, wc, wc_start = 0, 0, 0, 0
        # first word
        line_w += len(words[0])
        wc += 1
        for i in range(1, len(words)):
            wl = len(words[i])
            if line_w + 1 + wl <= maxWidth: # add words if avaiable
                line_w = line_w + 1 + wl
                wc += 1
            else: # cannot add words
                l = self.justifyLine(words, line_w, wc, wc_start, maxWidth)
                ret.append(l)
                # start a newline, handle first word of the line
                line_num += 1
                line_w = wl
                wc = 1
                wc_start = i
        # handle last line
        if wc > 0:
            lastLine = words[wc_start]
            for i in range(1, wc):
                lastLine += (' ' + words[wc_start + i])
            lastLine += (' ' * (maxWidth - line_w))
            ret.append(lastLine)
        return ret

    def justifyLine(self, words, line_w, wc, wc_start, maxWidth):
        ret = ''
        if wc == 1:
            ret += words[wc_start]
            ret += (' ' * (maxWidth - line_w))
        else:
            totalSpace = maxWidth - line_w + (wc - 1)
            rem, mod = totalSpace // (wc - 1), totalSpace % (wc - 1)
            ret += words[wc_start]
            for i in range(1, wc):
                ret += (' ' * rem)
                if mod > 0:
                    ret += ' '
                    mod -= 1
                ret += words[wc_start + i]
        return ret
