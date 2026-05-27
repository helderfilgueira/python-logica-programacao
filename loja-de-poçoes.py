'''ATIVIDADE PROPOSTA:
CRIE UM ALGORITMO QUE LEIA: O NOME DA POÇÃO, VALOR, QUANTIDADE; E POR FIM MOSTRE O VALOR TOTAL E A QUANTIDADE'''

pocao=input("Qual o nome da que poção você deseja?")
preco_pocao=float(input("Qual o valor da poção? "))
quantidade=float(input("Qual é a quantidade? "))

print()
print("==============================")
print("Resumo do pedido")
print("==============================")
print()
print(pocao)
print("valor da compra: ", preco_pocao*quantidade, "R$")
