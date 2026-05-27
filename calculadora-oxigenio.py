'''INSTRUÇÕES DA ATIVIDADE:

CRIE UM ALGORITMO QUE....

LEIA:
  -TEMPO DE CAMINHADA
  -QUANTIDADE DE OXIGÊNIO INICIAL
  -CONSUMO

  E QUE NO FINAL CALCULE A QUANTIDADE DE OXEGÊNIO RESTANTE NO TANQUE.'''
  
temp_caminhada=float(input("Quanto foi o tempo de caminhada?(em min): "))
quant_oxigenio_inicial=float(input("Qual é a quantidade de oxigênio inicial?(em %): "))

consumo = float(input("Quanto Oxigênio foi gasto por minuto?: "))
x=temp_caminhada * consumo
quant_oxigenio_final=quant_oxigenio_inicial-x

print("Quanto oxigênio resta no tanque: ", quant_oxigenio_final,"%")






