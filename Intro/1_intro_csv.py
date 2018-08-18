from matplotlib import pyplot as plt
from matplotlib import style
import  numpy as np

style.use('ggplot')

x,y = np.loadtxt('plik.csv',
                unpack = True,
                delimiter = ',' )
plt.plot(x,y)

plt.title('Wykres')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
