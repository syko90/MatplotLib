import matplotlib.pyplot as plt
plt.bar([1,2,5,6,9],[5,2,7,8,2],label='Przykład')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label = 'Przykład drugi',color='g')
plt.legend()
plt.xlabel('numer słupka')
plt.ylabel('wykość słupka')

plt.title('Super wykres\na tu kolejna linia! Moaaa')

plt.show()
