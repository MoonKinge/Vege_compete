import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math
import Test


x = [2, 10, 20, 30, 40]  # 以1980年为0
y = [2.09, 1.48, 1.07, 0.57, 0.53]

# 对于增长率的拟合
# 指数函数拟合
def func1(x, a, b, c):
    return a * np.power(b, x) + c


# 对数函数拟合
def func2(x, a, b, c):
    return a * np.log(x+b) + c


xdata = np.array(x)
ydata = np.array(y)
popt1, pcov1 = curve_fit(func1, xdata, ydata,maxfev=5000000)
popt2, pcov2 = curve_fit(func2, xdata, ydata,maxfev=5000000)
a1, b1, c1 = popt1
y_pre1 = a1 * np.power(b1, x) + c1
print(f"y_pre1 = {a1} * np.power({b1}, x) + {c1}")
a2, b2, c2 = popt2
y_pre2 = a2 * np.log(x + b2) + c2
print(f"y_pre2 = {a2} * np.log(x + {b2}) + {c2}")


# 三次函数拟合
coef1 = np.polyfit(x, y, 3)
y_pre3 = np.polyval(coef1, x)
a3, b3, c3, d3 = coef1
print(f"y_pre3 = {a3} * x^3 + {b3} * x^2 + {c3} * x + {d3}")


# 二次函数拟合
coef2 = np.polyfit(x, y, 2)
y_pre4 = np.polyval(coef2, x)
a4, b4, c4 = coef2
print(f"y_pre4 = {a4} * x^2 + {b4} * x + {c4}")


plt.plot(x, y_pre1, 'g-', label="Fitting Curve/exp")
plt.plot(x, y_pre2, 'y-', label="Fitting Curve/log")
plt.plot(x, y_pre3, 'b-', label="Fitting Curve/^3")
plt.plot(x, y_pre4, 'p-', label="Fitting Curve/^2")
plt.plot(x, y, 'r-', label="Annual Growth Rate")
plt.xlabel("years")
plt.ylabel("%")
plt.legend()
plt.show()

# 计算误差率
for i in [10, 20, 30, 40]:
    y0 = y[x.index(i)]
    y1 = Test.exp_test(i)
    y2 = Test.log_test(i)
    y3 = Test.cube_test(i)
    y4 = Test.square_test(i)
    print(f"{1980+i}年的实际增长率为{y0}")
    for j in [y1, y2, y3, y4]:
        c = math.fabs(j - y0) / y0
        if j == y1:
            print(f"指数函数拟合的预期增长率为{j},误差为{c}")

        elif j == y2:
            print(f"对数函数拟合的预期增长率为{j},误差为{c}")
        elif j == y3:
            print(f"三次函数拟合的预期增长率为{j},误差为{c}")
        elif j == y4:
            print(f"二次函数拟合的预期增长率为{j},误差为{c}")


