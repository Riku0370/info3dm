# 適当なデータを用意
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

datasets = np.array([[4,7], [8,10], [13,11], [17,14]])
x = datasets[:,0]
y = datasets[:,1]


def function(x):
  return (x-10)**2

plt.scatter(x, y, color="black", label="データセット")
plt.xlabel('x')
plt.ylabel('y')
x2 = np.linspace(4, 17, 100) #定義域[4,17]で5等分したサンプルを用意
y2 = function(x2)           #サンプルにおけるyの値を準備
plt.plot(x2, y2, color="blue", linewidth=3, label="プロット例")
plt.legend(loc="best")
plt.show()