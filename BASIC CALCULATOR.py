class Solution:
    def calculate(self, s: str) -> int:
        val_stack = []
        cur_num = 0
        total = 0
        sign = 1
        for c in s:
            if c.isdigit():
                cur_num*=10
                cur_num+=int(c)
            elif c=='+':
                total+=cur_num*sign
                cur_num = 0
                sign = 1
            elif c=='-':
                total+=cur_num*sign
                cur_num = 0
                sign = -1
            elif c=='(':
                val_stack.append(total)
                val_stack.append(sign)
                sign = 1
                total = 0
            elif c==')':
                total += sign * cur_num
                cur_num = 0
                total *= val_stack.pop()
                total += val_stack.pop()
        if cur_num: total += sign * cur_num
        return total
