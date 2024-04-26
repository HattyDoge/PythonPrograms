from math import sqrt
from matplotlib import pyplot
def CalcolaY(a,b,c,x):
    return a*x**2+b*x+c
#Codice Equazione di secondo grado
a = 0
while a == 0:
    a = float(input("Inserisci il primo valore a deve essere diverso da 0: "))
b = float(input("Inserisci il secondo valore b: "))
c = float(input("Inserisci il terzo valore c: "))
print("_"*20)
print(a,"x² + ",b, "x + ",c," = 0")
print("_"*20)
delta = pow(b,2) - 4 * a * c
if(delta < 0):
    soluzione = "Equazione impossibile"
elif(delta == 0):
    risultato1 = -b/(a*2)
    soluzione = "x¹² = "+ str(risultato1)
else:
    risultato1 = -b+sqrt(delta)/(a*2)
    risultato2 = -b-sqrt(delta)/(a*2)
    soluzione = "x¹ = " + str(risultato1) + "x² = " + str(risultato2)
print(soluzione)
x_coo = []
y_coo = []
delta_r = 2 * (risultato2 - risultato1)
for i in range(0,1001):
    x = risultato1 -delta_r/4 + i/1000 * delta_r
    x_coo.append(x)
    y_coo.append(CalcolaY(a,b,c,x))

pyplot.plot(x_coo, y_coo)
pyplot.show()
