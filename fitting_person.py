import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math
import Test


def func1(x, a, b, c):
    return a * np.power(b, x) + c


# 对数函数拟合
def func2(x, a, b, c):
    return a * np.log(x+b) + c


# 对于人数的拟合
xr = [3, 14, 32, 40, 50, 60, 70]  # 以1950年为0
yr = [58260, 69458, 100818, 113368, 126583, 133972, 141178]  # 人数
xrdata, yrdata = np.array(xr), np.array(yr)
rpopt1, rpcov1 = curve_fit(func1, xrdata, yrdata,maxfev=5000000)
rpopt2, rpcov2 = curve_fit(func2, xrdata, yrdata,maxfev=5000000)
ar1, br1, cr1 = rpopt1
yr_pre1 = ar1 * np.power(br1, xr) + cr1
print(f"yr_pre1 = {ar1} * np.power({br1}, xr) + {cr1}")
ar2, br2, cr2 = rpopt2
yr_pre2 = ar2 * np.log(xr + br2) + cr2
print(f"yr_pre2 = {ar2} * np.log(xr + {br2}) + {cr2}")


# 三次函数拟合
rcoef1 = np.polyfit(xr, yr, 3)
yr_pre3 = np.polyval(rcoef1, xr)
ar3, br3, cr3, dr3 = rcoef1
print(f"yr_pre3 = {ar3} * xr^3 + {br3} * xr^2 + {cr3} * xr + {dr3}")


# 二次函数拟合
rcoef2 = np.polyfit(xr, yr, 2)
yr_pre4 = np.polyval(rcoef2, xr)
ar4, br4, cr4 = rcoef2
print(f"yr_pre4 = {ar4} * xr^2 + {br4} * xr + {cr4}")


plt.plot(xr, yr_pre1, 'g-', label="Fitting Curve/exp")
plt.plot(xr, yr_pre2, 'y-', label="Fitting Curve/log")
plt.plot(xr, yr_pre3, 'b-', label="Fitting Curve/^3")
plt.plot(xr, yr_pre4, 'p-', label="Fitting Curve/^2")
plt.plot(xr, yr, 'r-', label="National Population")
plt.xlabel("years")
plt.ylabel("10000persons")
plt.legend()
plt.show()

# 计算误差率
for ir in [40, 50, 60, 70]:
    yr0 = yr[xr.index(ir)]
    yr1 = Test.r_exp_test(ir)
    yr2 = Test.r_log_test(ir)
    yr3 = Test.r_cube_test(ir)
    yr4 = Test.r_square_test(ir)
    print(f"{1950 + ir}年的实际人数为{yr0}万人")
    for jr in [yr1, yr2, yr3, yr4]:
        cr = math.fabs(jr - yr0) / yr0
        if jr == yr1:
            print(f"指数函数拟合的预期人数为{jr}万人,误差为{cr}")
        elif jr == yr2:
            print(f"对数函数拟合的预期人数为{jr}万人,误差为{cr}")
        elif jr == yr3:
            print(f"三次函数拟合的预期人数为{jr}万人,误差为{cr}")
        elif jr == yr4:
            print(f"二次函数拟合的预期人数为{jr}万人,误差为{cr}")
