'''CARDÁPIO - SISTEMA DE PEDIDOS 
Helder Filgueira 

OBS: NESSA ATIVIDADE NÃO PODIA SER USADO LISTAS (ARRAY)'''
  
print("Entradas:") 
print("  1 Batata-Frita ---------- R$ 10,00") 
print("  2 Bolinhas de Queijo ---- R$ 12,00") 
print("  3 Cubos de Frango ------- R$ 13,00") 
print("  4 Torresmo -------------- R$ 15,00") 
print("  5 Saladinha ------------- R$ 11,00") 
print("  0 Nenhuma das opções acima") 
print() 

print("Pratos Principais:") 
print("  6  Picanha --------------- R$ 140,00") 
print("  7  Filé ------------------ R$ 110,00") 
print("  8  Sushi ----------------- R$ 120,00") 
print("  9  Alcatra --------------- R$ 100,00") 
print("  10 Bacalhau -------------- R$ 200,00") 
print("  0  Nenhuma das opções acima") 
print() 

print("Bebidas:") 
print("  11 Ice ------------------- R$ 10,00") 
print("  12 Coca-Cola ------------- R$ 10,00") 
print("  13 Gin ------------------- R$ 20,00") 
print("  14 Sprite ---------------- R$ 10,00") 
print("  15 Vinho ----------------- R$ 100,00") 
print("  0  Nenhuma das opções acima") 
print() 

# ENTRADAS---------------------------------------------------------- 

entrada = input("Digite o número da sua entrada (ou 0 para nenhuma): ") 

if entrada == "1": 
    p_ent = "Batata-Frita" 
elif entrada == "2": 
    p_ent = "Bolinhas de Queijo" 
elif entrada == "3": 
    p_ent = "Cubos de Frango Empanado" 
elif entrada == "4": 
    p_ent = "Torresmo" 
elif entrada == "5": 
    p_ent = "Saladinha" 
else: 
    p_ent = "Nenhuma" 

quant_entrada = int(input("Digite a quantidade: ")) 

if entrada == "1": 
    preco_entrada = quant_entrada * 10 
elif entrada == "2": 
    preco_entrada = quant_entrada * 12 
elif entrada == "3": 
    preco_entrada = quant_entrada * 13 
elif entrada == "4": 
    preco_entrada = quant_entrada * 15 
elif entrada == "5": 
    preco_entrada = quant_entrada * 11 
else: 
    preco_entrada = 0 

# PRATO PRINCIPAL-------------------------------------------------------------- 

principal = input("Digite o número do seu prato principal (ou 0 para nenhum): ") 

if principal == "6": 
    p_prin = "Picanha" 
elif principal == "7": 
    p_prin = "Filé" 
elif principal == "8": 
    p_prin = "Sushi" 
elif principal == "9": 
    p_prin = "Alcatra" 
elif principal == "10": 
    p_prin = "Bacalhau" 
else: 
    p_prin = "Nenhum" 

quant_principal = int(input("Digite a quantidade: ")) 
  
if principal == "6": 
    preco_principal = quant_principal * 140 
elif principal == "7": 
    preco_principal = quant_principal * 110 
elif principal == "8": 
    preco_principal = quant_principal * 120 
elif principal == "9": 
    preco_principal = quant_principal * 100 
elif principal == "10": 
    preco_principal = quant_principal * 200 
else: 
    preco_principal = 0 

# BEBIDAS----------------------------------------------------------------------- 

bebida = input("Digite o número da sua bebida (ou 0 para nenhuma): ") 

if bebida == "11": 
    p_beb = "Ice" 
elif bebida == "12": 
    p_beb = "Coca-Cola" 
elif bebida == "13": 
    p_beb = "Gin" 
elif bebida == "14": 
    p_beb = "Sprite" 
elif bebida == "15": 
    p_beb = "Vinho" 
else: 
    p_beb = "Nenhuma" 

quant_bebida = int(input("Digite a quantidade: ")) 

if bebida == "11": 
    preco_bebida = quant_bebida * 10 
elif bebida == "12": 
    preco_bebida = quant_bebida * 10 
elif bebida == "13": 
    preco_bebida = quant_bebida * 20 
elif bebida == "14": 
    preco_bebida = quant_bebida * 10 
elif bebida == "15": 
    preco_bebida = quant_bebida * 100 
else: 
    preco_bebida = 0 

# RESUMO DO PEDIDO----------------------------------------------- 
  
total = preco_entrada + preco_principal + preco_bebida 

print() 
print("==========================================") 
print("            RESUMO DO PEDIDO") 
print("==========================================") 

print(quant_entrada, "un -", p_ent, "- R$", preco_entrada, ",00") 
print(quant_principal, "un -", p_prin, "- R$", preco_principal, ",00") 
print(quant_bebida, "un -", p_beb, "- R$", preco_bebida, ",00") 
print("------------------------------------------") 

print("TOTAL DO PEDIDO: R$", total, ",00") 

print("==========================================") 
