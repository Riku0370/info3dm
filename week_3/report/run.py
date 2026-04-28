import numpy as np
import random
import dataset1
# フォント設定
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
plt.rcParams['font.family'] = font_prop.get_name()


x = np.array([0])
y = dataset1.true_function(x)
print(y)

x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

plt.plot(x, y, label="true_function")
plt.legend()
plt.savefig("ex1.1.png")
plt.show()