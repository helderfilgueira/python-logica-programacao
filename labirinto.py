'''ATIVIDADE - LABIRINTO
OBS: USUÁRIO UTILIZA UM MAPA EXTERNO PARA JOGAR
["S", "_", "#", "#", "_", "$"]
["_", "#", "_", "_", "#", "_"]
["#", "_", "#", "#", "$", "_"]
["_", "_", "_", "$", "_", "_"]
["$", "#", "#", "#", "_", "E"]
'''

mapa=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        print(f'[{mapa[l][c]:^6}]', end='')
    print()

for l in range(0,5):
    for c in range(0,5):
        mapa[l][c]=str(input(f'digite um valor ["_","#","$"] para[{l},{c}]: '))  
        mapa[4][4]='E'
        
        if mapa[l][c]=='_':
            print('Avançou uma casa!!!')
        elif mapa[l][c]=='#':
            print('Qubrou pedra e avançou!!!')
        elif mapa[l][c]=='$':
            print('coletou moeda!!')
        elif mapa[l][c]==mapa[4][4]:
            print('encontrou a saída!!!') 
        else:
            print("ELEMENTO INVÁLIDO!!")
            mapa[l][c]=str(input(f'digite o elemento correto ["_","#","$"] para[{l},{c}]: '))  

for l in range(0,5):
    for c in range(0,5):
        print(f'[{mapa[l][c]:^6}]', end='')
    print()
