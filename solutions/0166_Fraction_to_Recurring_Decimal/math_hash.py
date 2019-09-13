class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign_pos = True
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            sign_pos = False
        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator
        int_part = numerator // denominator
        frac_part = numerator % denominator
        if frac_part == 0:
            return "%s%d" % ('' if sign_pos else '-', int_part)
        frac_div_list = []
        fracs, i = {}, 0
        while frac_part not in fracs:
            fracs[frac_part] = i
            frac_part *= 10
            frac_div_list.append(str(frac_part // denominator))
            frac_part = frac_part % denominator
            i += 1
        repeat_from = fracs[frac_part]
        if frac_div_list[-1] == '0':
            return "%s%d.%s" % ('' if sign_pos else '-', \
                    int_part, \
                    ''.join(frac_div_list[:-1]))
        else:
            return "%s%d.%s(%s)" % ('' if sign_pos else '-', \
                    int_part, \
                    ''.join(frac_div_list[:repeat_from]), \
                    ''.join(frac_div_list[repeat_from:]))
