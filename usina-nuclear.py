'''
Algoritmo e lógica de programação
Heldor Filgueira - Atividade 3
'''

#Usina de Springfield

import random
import time


#Módulo de identificação do operador

nome = input("Nome do operador:")
print(("Bem-vindo: ", nome))


#modulo de repetição

while True:

    temperatura = random.randint(0, 2200)

    time.sleep(3)

    print()


    #módulo de verificação de temperatura

    if temperatura >= 2200:
        print(("temperatura= ", temperatura, "°C, status: Deus o abençoe!!"))

    elif temperatura > 1000:
        print(("temperatura= ", temperatura, "°C, status: Temperatura Crítica!!"))

    elif temperatura >= 500:
        print(("temperatura= ", temperatura, "°C, status: aquecimento"))

    else:
        print(("temperatura= ", temperatura, "°C, status: Reator Ok"))
