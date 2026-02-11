import pandas as pd
data = [101,102,103,104]
series = pd.Series(data)
print(series)
Output ==>
0    101
1    102
2    103
3    104
dtype: int64

import pandas as pd
data = [True,False,True,False]
series = pd.Series(data)
print(series)
Output ==>
0     True
1    False
2     True
3    False
dtype: bool

import pandas as pd
data = ["A","B","C","D"]
series = pd.Series(data)
print(series)
Output ==>
0    A
1    B
2    C
3    D
dtype: object

import pandas as pd

data = [101,102,103,104]
series = pd.Series(data, index = ["a","b","c","d"])
print(series.loc["a"])
print(series.loc["b"])
print(series.loc["c"])
Output ==>
101
102
103

import pandas as pd
data = [101,102,103,104,105,106]
series = pd.Series(data, index = ["a","b","c","d","e","f"])
print(series[series < 200])
Output ==>

a    101
b    102
c    103
d    104
e    105
f    106
dtype: int64

