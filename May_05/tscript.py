#!/usr/bin/env python3
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

print("__________T-test__________")

p_mean = float(input("\nPopulation mean: "))
s_mean = float(input("Sample mean: "))
s_stdv = float(input("Sample stand_dev: "))
n = float(input("Sample length: "))

# degrees of freedom, level of significance, confidence level
dof = n - 1;  los = 0.05; cnl = 1 - los

# calculation of T-statistics
tstatistics = (s_mean - p_mean)/(s_stdv/np.sqrt(n))
tstatistics = -tstatistics if tstatistics > 0 else tstatistics
print("\nT-statistics: {:.5f}".format(tstatistics))

# calculation of Critical values
tcritical_l = t.ppf(q = los/2, df = dof)
tcritical_u = -tcritical_l
print("\nCritical values are {}, {}".format(tcritical_l, tcritical_u))

# decision making - using T-statistics and Critical values
if tstatistics < tcritical_l or tstatistics > tcritical_u:
    print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# calculation of p-value
pvalue = 2*t.cdf(tstatistics, df = dof)
print("\np-value: {:.5f}".format(pvalue))

# decision making - using p-value
if pvalue < los: print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# standard error
std_err = s_stdv/np.sqrt(n)
print("\nStandard Error: {:.5f}".format(std_err))

# confidence interval
cnf_int = s_mean + std_err * np.array([tcritical_l, tcritical_u])
print("Confidence Interval: {}".format(cnf_int))

# plot script
x1=np.linspace(-10,tcritical_l,1000); y1=t.pdf(x1,df=dof)
x2=np.linspace(tcritical_u,10,1000);  y2=t.pdf(x2,df=dof)
x3=np.linspace(-4,4,1000); y3=t.pdf(x3,df=dof)
ax=plt.figure().add_subplot(111); ax.plot(x3,y3,color='brown')
ax.fill_between(x1,y1,0,alpha=0.5,color='brown',label='Rejection Region')
ax.fill_between(x2,y2,0,alpha=0.5,color='brown'); ax.set(xlabel='X',ylabel='P(X)')
ax.axvline(x=tstatistics,ls='--',c='b',label='T statistics = {:.5f}'.format(tstatistics))
ax.set(xlim=[-4,4],title="T Distribution (degrees of freedom = {:.0f})".format(dof))
plt.legend(); plt.show()
