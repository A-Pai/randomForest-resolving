import pandas as pd
import numpy as np
from sklearn import datasets


# %% 生成、展示数据
X, y = datasets.make_circles(
    n_samples=20000, factor=0.7, noise=0.05, random_state=9)  # factor:外圈与内圈的尺度因子

z=pd.DataFrame(np.column_stack((X,y)),columns=["x1", "x2", "y"])

z.to_csv(".\circles.csv",index=None)
