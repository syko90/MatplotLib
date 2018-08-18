import matplotlib.pyplot as plt

kawalki = [7,2,2,13]
czynnosci = ['sen', 'jedzenie','praca','zabawa']
kolumny = ['c','m','r','b']

plt.pie(kawalki,
        labels = czynnosci,
        colors = kolumny,
        startangle = 90,
        shadow = True,
        explode = (0,0.1,0,0),
        autopct ='1.1f%%'
        )
plt.title('Graf')
plt.show()
