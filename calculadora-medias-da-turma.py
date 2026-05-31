'''Algoritmo e lógica de programação
Professor: T. MOURA
Aluno: Heber Figueira
Data: 15/03/2026


 Calculadora que pergunta a nota do aluno e calcula a sua média individual;
'''

# Média na contagem - (PARTE 1) -> salva as informações independente do loop.
contaluno = 0
contmedias = 0


while true:  # Conceito de repetição

    nome = input("Digite o nome do aluno")

    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))

    média = (n1 + n2 + n3 + n4) / 4


# média de médias

if média > 10:  # Dgt - erro de digitação

    print("ERRO: as notas digitadas estão incorretas!! Insira novamente!!")
    contmedias = contmedias - media
    contalunos = contalunos - 1

elif media == 10:

    print("Aluno Destaque: O Aluno(a) ", nome, " foi aprovado(a), com média: ", média)

elif media >= 7:

    print("Aluno(a) ", nome, " foi aprovado(a), com média: ", média)

elif media <= 7:

    print("Aluno(a) ", nome, " foi reprovado(a), com média: ", média)
