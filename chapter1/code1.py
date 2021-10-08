"""
牛顿迭代法计算平方根
"""

def squareroot(n):
    root = n/2 #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

x = squareroot(81)
print(x)