import matplotlib.pyplot as plt

dni = [1,2,3,4,5]

sen = [7,8,6,11,7]
jedzenie = [2,3,4,3,2]
praca = [7,8,7,2,2]
zabawa = [8,5,7,8,13]

plt.plot([],[],color='m', label='sen', linewidth=5)
plt.plot([],[],color='c', label='jedzenie', linewidth=5)
plt.plot([],[],color='r', label='praca', linewidth=5)
plt.plot([],[],color='k', label='zabawa', linewidth=5)

plt.stackplot(dni, sen, jedzenie,praca, zabawa, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Fajny graf')
plt.legend()
plt.show()
