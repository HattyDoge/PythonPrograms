b = True
c = False
k = None
def AltraFunzione(divisore):
    return 10 // divisore
def Funzione(x):
    AltraFunzione(x)
try:
    print(AltraFunzione(10))
    print(Funzione(0))
except ZeroDivisionError:
    print("Divisione per zero !")
else:
    print("Siamo nell'else «wooo»")
finally:
    print("Finalmente !")
