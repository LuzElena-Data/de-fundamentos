import pandas as pd

a = pd.Series([1, 2, 3, 4])
b = pd.Series([10, 20, 30, 40])
c = pd.Series([40, 30, 20, 10])
d = pd.Series([5, 1, 7, 2])

print(a.corr(b))
print(a.corr(c))
print(a.corr(d))