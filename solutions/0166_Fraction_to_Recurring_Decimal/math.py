class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # determine sign
        sign_pos = True
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            sign_pos = False
        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator
        # get int_part and frac_part
        int_part = numerator // denominator
        frac_part = numerator % denominator
        frac_div_list = [] # tracking division's result(quotient)
        frac_part_list = [] # tracking dividend
        # if no frac_part, return answer formed by int_part
        if frac_part == 0:
            return "%s%d" % ('' if sign_pos else '-', int_part)
        # get all digits by left-shift and divide
        while frac_part not in frac_part_list: # stop when a dividend has already occured
            frac_part_list.append(frac_part)
            frac_part *= 10
            frac_div_list.append(str(frac_part // denominator))
            frac_part = frac_part % denominator
        # find the index where repeating from
        repeat_from = frac_part_list.index(frac_part)
        # form the answer
        if frac_div_list[-1] == '0':
            return "%s%d.%s" % ('' if sign_pos else '-', \
                    int_part, \
                    ''.join(frac_div_list[:-1]))
        else:
            return "%s%d.%s(%s)" % ('' if sign_pos else '-', \
                    int_part, \
                    ''.join(frac_div_list[:repeat_from]), \
                    ''.join(frac_div_list[repeat_from:]))
