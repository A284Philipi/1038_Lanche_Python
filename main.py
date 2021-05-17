a, b = input().split(" ")
a = int(a)
b = int(b)
if a == 1:
    valor = float(4)
else:
    if a == 2:
        valor = float(4.5)
    else:
        if a == 3:
            valor = float(5)
        else:
            if a == 4:
                valor = float(2)
            else:
                valor = float(1.5)
valor = float(valor * b)
print("Total: R$ %.2f"%(valor))