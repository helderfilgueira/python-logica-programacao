contacaixa=0
peso_max=0
peso_max_robo=int(input("Qual é o peso máximo suportado pelo robô? "))

while True:

    peso_caixa=int(input("Qual é o peso da caixa? "))
    peso_max=int(peso_max+peso_caixa)
    contacaixa=contacaixa+1
    quant_viagem=int((peso_max/peso_max_robo)+1)

    soma_caixa=input("Quer somar mais caixas?(0 P/Não): ")
    if soma_caixa == "0":
        print()
        print("O peso total das caixas é: ", peso_max)
        print("A quantidade de caixas é: ", contacaixa)
        print("A quantidade de viagens para transportar é: ", quant_viagem)


        break
