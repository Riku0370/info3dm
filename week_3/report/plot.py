import numpy as np
import matplotlib.pyplot as plt
import dataset1

# 真の関数
x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

plt.plot(x, y, label="true_function")

# 観測点
df = dataset1.create_dataset()
plt.scatter(df["観測点"], df["真値"], label="sample", s=30)

plt.legend()
plt.savefig("ex1.2.png")
plt.show()