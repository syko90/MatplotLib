import matplotlib.pyplot as plt

dni = [1,2,3,4,5]

sen = [7,8,6,11,7]
jedzenie = [2,3,4,3,2]
praca = [7,8,7,2,2]
zabawa = [8,5,7,8,13]

plt.stackplot(dni, sen, jedzenie,praca, zabawa, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Fajny graf')
plt.show()
