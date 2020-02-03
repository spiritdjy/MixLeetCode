# coding: utf-8
"""
验证给定的字符串是否可以解释为十进制数字。
例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要
"""
import wrapt


@wrapt.decorator
def record_args(wrapped, instance, args, kwargs):
    """
    记录程序调用的日志
    :param wrapped:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    ret = wrapped(*args, **kwargs)
    print(wrapped.__name__, args, kwargs, ret)
    return ret



class Solution:
    @record_args
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        if s[0] in '-+':
            s = s[1:]
        return self.no_sign(s)

    @record_args
    def no_sign(self, s: str) -> bool:
        if not s:
            return False

        if s and s[0] == '.':
            if not s[1:] or s[1] not in '0123456789':
                return False
            return self.part(s)

        if s[0] not in '0123456789':
            return False

        # if s[0] == '0':
        #     if len(s) > 1 and s[1] == '.':
        #         return self.part(s[1:])
        #     return self.e_part(s[1:])

        # '01' -> true
        while s and s[0] in '0123456789':
            s = s[1:]
        return self.part(s)

    @record_args
    def part(self, s: str):
        if s and s[0] == '.':
            s = s[1:] # part must 1?
            while s and s[0] in '0123456789':
                s = s[1:]
            return self.e_part(s)
        return self.e_part(s)

    @record_args
    def e_part(self, s: str):
        if s and s[0] == 'e':
            s = s[1:]
            if s and s[0] in '-+':  # 005047e+6
                s = s[1:]
            if not s or s[0] not in '0123456789':  # 2e0 -> True
                return False
            while s and s[0] in '0123456789':
                s = s[1:]
            return not s
        return not s


def test():
    for line in '''"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"005047e+6" => true
"95a54e53" => false'''.split('\n'):
        if line:
            str_, ret = line.split('=>')
            #str_ = eval(str_)
            str_ = str_.strip().strip('"')
            print(str_, ret)
            assert Solution().isNumber(str_) == (ret.strip() == 'true')


if __name__ == '__main__':
    test()