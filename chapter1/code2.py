"""
进行小数运算
"""

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def div(self) -> float:

        return self.num / self.den

    # 重写str方法
    def __str__(self):

        return str(self.num) + "/" + str(self.den)

    # 最大公因数
    def gcd(self, num, den):
        while num % den != 0:
            tmp = num % den
            num = den 
            den = tmp

        return den

    # 重写add方法
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)

        return Fraction(int(newnum/common), int(newden/common))
    
    # 重写equal方法
    def __eq__(self, other):
        sum1 = self.num * other.den
        sum2 = self.den * other.num

        return sum1 == sum2




f1 = Fraction(3, 5)
print(f1)
f2 = Fraction(1, 3)
print(f1.div())
f3 = f1 + f2
print(f3)
print(f1 == f2)

# print(dir(f1))
