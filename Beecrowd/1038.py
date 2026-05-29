pedido,quant = map(int,input().split())

let1 = 4.00
let2 = 4.50
let3 = 5.00
let4 = 2.00
let5 = 1.50

if pedido == 1:
    pedido = let1
if pedido == 2:
    pedido = let2
if pedido == 3:
    pedido = let3
if pedido == 4:
    pedido = let4
if pedido == 5:
    pedido = let5

result = pedido*quant
print(f"Total: R$ {result}")

