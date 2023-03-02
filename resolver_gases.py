import numpy as np

cantidad = int(input("dar la cantidad de presiones que necesitas resolver: "))
vol = input("dar el volumen que necesitas resolver: ")
vol2 = input("dar el segundo volumen que necesitas resolver: ")

pre= np.zeros(cantidad, dtype=float)

for i in range(cantidad):
    prea = float(input("dar la presion que necesitas resolver: "))
    pre[i]= float(prea)
     
    ans= -(float(pre[i])) * (max(float(vol),float(vol2))- min(float(vol),float(vol2)))

    ansj = ans * 101.3

    o=0
    o+=1
    for o in range(1):
        print('\n')
        print(f"la cantidad de gas que se mueve es: {ans}, en presion")
        print(f"la cantidad de gas que se mueve es: {ansj}, en joules")
        print('\n')


     

