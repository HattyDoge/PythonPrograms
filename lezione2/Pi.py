import random as balls
import math as cock
def MontecarloPi():
    raggio = 1.0
    raggioSQR = raggio**2
    print("Determinazione di Pi-Greco con metodo di Montecarlo")
    iterazioni = 20000000
    dentro = 0
    for i in range(iterazioni):
        x = balls.random()
        y = balls.random()
        if x * x + y * y < raggioSQR:
            dentro+=1
    PiMontecarlo = 4.0 * dentro / iterazioni
    print("Pi-Greco stimato = ", PiMontecarlo)
    print("Pi-Greco esatto = ", cock.pi)
MontecarloPi()