prod1,quant1,valor1 = input().split()

prod1 = int(prod1)
quant1 = float(quant1)
valor1 = float(valor1)

prod2,quant2,valor2 = input().split()

prod2 = int(prod2)
quant2 = float(quant2)
valor2 = float(valor2)

result = (valor1*quant1)+(valor2*quant2)
print(f"VALOR A PAGAR: R$ {result:.2f}")