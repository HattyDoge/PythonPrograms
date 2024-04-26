# tipi di dato

a = 1

b = "nel mezzo del cammin di nostra vita..." # tipo string

c = [1, 7, "a", (2, 4, 6)] # una lista di 4 elementi

d = 3.1415681 # float

e = (7, 5, "ciao", 3.14) # tupla = lista non modificabile

#print(e)

#print("stacco")

#for i in e:
#    print(i)

# print("stacco")

# for i in range(4):
#     print(e[i])

print("-"*40)
print(b)
print(b[4:11])
print(b[4:])
print(b[4:9999999])
print(b[-11:-4])
print(b[:-4])
print("-"*40)

l = [1]
t = (1,)

dict = {"key":7, "key2":3.14}
s = input("Caro utente, scrivi qualcosa: ")
print("Hai scritto " + s)
numero = int("12345", 16)
print(numero)
numero = tuple("abdc") # c'è anche list()
print(numero)
t = float("3.145")
print(t)
t = bool(12)
print(t)
t = bool(0)
print(t)
t = chr(65) # ord è per trovare in base al carattere il codice unicode
print(t)
# Costrutti Python
numero = int(input("Caro utente, Inserisci un numero intero: "))
if(numero % 3 == 0):
    print("Il numero "+ str(numero) +" inserito è divisibile per 3")
else:
    print("Il numero "+ str(numero) +" inserito è divisibile per 3")
print("_"*20)
while numero > 0:
    print(numero)
    numero = numero//2
print("_"*20)
for i in range(numero):
    print(i)