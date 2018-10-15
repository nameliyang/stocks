import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x,y, label='liner')
plt.legend()
plt.show()
print(mt.is_interactive())
