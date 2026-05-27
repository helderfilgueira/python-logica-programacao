idade=int(input("Qual é a sua idade? "))

if idade <= 12:
    print("CRIANÇA!!!")
elif idade <= 17:
    print("Adolescente")
elif idade <= 21:
    print("Jovem")
elif idade <= 50:
    print("Adulto")
else:
    print("Idoso")
