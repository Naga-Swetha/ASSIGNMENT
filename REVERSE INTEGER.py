class Solution:
    def reverse(self, f: int) -> int:
        r = 0
        x = 0
        h = False
        if 0>f:
            x = abs(f)
            h = True
        else:
            x = f
        while x>0:
            i = x%10
            r = r*10+i
            x//=10
        if -2147483648 <= r <= 2147483647:
            if h:
                return -r
            else:
                return r
        else:
            return 0
