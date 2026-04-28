import numpy as np
import matplotlib.pyplot as plt
import dataset1

# 真の関数
x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

plt.plot(x, y, label="true_function")

# 観測点
df = dataset1.create_dataset()

mean = 0
variance = 2
sigma = np.sqrt(variance)
size = len(df)

noise = np.random.normal(mean, sigma, size)

noise = noise / 2
df["観測値"] = df["真値"] + noise
plt.scatter(df["観測点"], df["観測値"], label="observed", color="red")
plt.legend()
plt.savefig("ex1.3.png")
plt.show()

df.to_csv("dataset.tsv", sep="\t", index=False)

