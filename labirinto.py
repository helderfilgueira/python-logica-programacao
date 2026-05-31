'''ATIVIDADE - LABIRINTO
OBS: USUÁRIO UTILIZA UM MAPA EXTERNO PARA JOGAR
["S", "", "#", "#", "", "$"]
["", "#", "", "", "#", ""]
["#", "", "#", "#", "$", ""]
["", "", "", "$", "", "_"]
["$", "#", "#", "#", "_", "E"]
'''
mapa=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#Exibe mapa no inicio
for l in range(0,5):
    for c in range(0,5):
        print(f'[{mapa[l][c]:^6}]', end='')
    print()

#Recebe informação e atribui o valor das 'casas'
for l in range(0,5):
    for c in range(0,5):
        
        mapa[l][c]=str(input(f'digite um valor ["_","#","$"] para[{l},{c}]: '))  
        mapa[4][4]='E'
        mapa[1][2] ='|'
        
        if mapa[l][c]=='_':
            print('Avançou uma casa!!!')
        elif mapa[l][c]=='#':
            print('Qubrou pedra e avançou!!!')
        elif mapa[l][c]=='$':
            print('coletou moeda!!')
        elif mapa[l][c]=='|':
            print('Encontrou beco sem saida, descendo pra linha de baixo!!')
        elif mapa[l][c]==mapa[4][4]:
            print('encontrou a saída!!!') 
        else:
            print("ELEMENTO INVÁLIDO!!")
            mapa[l][c]=str(input(f'digite o elemento correto ["_","#","$"] para[{l},{c}]: '))  
            
#Exibe mapa ao final
for l in range(0,5):
    for c in range(0,5):
        print(f'[{mapa[l][c]:^6}]', end='')
    print()
