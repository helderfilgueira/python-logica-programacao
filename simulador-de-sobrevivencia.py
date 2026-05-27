contadias=0
agua=float(input("Qual é a quantidade inicial de água? "))
consumo=float(input("Qual é o consumo diário de água?"))
quant_agua_reciclada=float(input("Qual é a quantidade diária de água reciclada?"))

while True:
    contadias=contadias+1
    
    agua=agua-consumo
    agua=agua+quant_agua_reciclada
    
    if agua<= consumo:
        print("Você sobreviveu: ", contadias, "Dias")
        print("No último dia restou: ",agua,"L de Água")
        break
