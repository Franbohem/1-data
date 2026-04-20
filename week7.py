import math
import numpy as np


def y_2(x):
    return x/3-2/9+(11/9)* math.exp(3*x)

def y_1(g, x0, y0, x_end, h):
    xs = [x0]
    ys = [y0]
    i = 0

    while xs[i] <= x_end:
        K1 = g(xs[i], ys[i])
        K2 = g(xs[i] + h/2, ys[i] + h*K1/2)
        K3 = g(xs[i] + h/2, ys[i] + h*K2/2)
        K4 = g(xs[i] + h, ys[i] + h*K3)
        ys.append(ys[i] + h*(K1 + 2*K2 + 2*K3 + K4)/6)
        xs.append(xs[i] + h)
        i += 1

    return np.array(xs), np.array(ys)
    

def f(x, y):
    return 3*y-x+1

x0 = 0.0
y0 = 1.0
x_end = 1.0
h = 0.2

xs, ys_num = y_1(f, x0, y0, x_end, h)
ys_exact = np.array([y_2(x) for x in xs])
errors = np.abs(ys_num - ys_exact)

print("    x\tRK4数值解\t解析解\t\t绝对误差")
print("-" * 70)
for x, yn, ye, err in zip(xs, ys_num, ys_exact, errors):
    print(f"{x:6.2f}\t{yn:12.6f}\t{ye:12.6f}\t{err:12.4e}")