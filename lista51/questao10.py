'''
Desenvolver um programa apresentes as potências de 3 variando de 0 a 15. Deve ser considerado que qualquer número
elevado a 0 é 1, e elevado a 1 ele próprio. A apresentação deve observar a seguinte exibição da tabela:
3^0 = 1
3^1 = 3
3^2 = 9
'''
import math

# Processamento e Output
var = 0
while var <= 15:
    print(f"3^{var}={math.pow(3,var)}")
    var = var + 1
print("FIM")
