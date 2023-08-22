'''
Desenvolver um programa apresentes as potências de 3 variando de 0 a 15. Deve ser considerado que qualquer número
elevado a 0 é 1, e elevado a 1 ele próprio. A apresentação deve observar a seguinte exibição da tabela:
3^0 = 1
3^1 = 3
3^2 = 9
'''
import math

# Processamento e Output (Com math.pow)
var1 = 0
while var1 < 15:
    var1 = var1 + 1
    print(f"3^{var1}={math.pow(3, var1):.0f}")
print("FIM do math.pow")

# Processamento e Output (Sem math.pow)
acumulador = 3
var2 = 2
while var2 < 15:
    acumulador = acumulador * var2
    print(f"3^{var2}={acumulador}")
    var2 = var2 + 1
print("FIM")
