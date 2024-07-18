#operaciones matematicas
a = 10
b = 3
print(a>b)
print(a<b)
print(a >= b)
print(a <= b)
print(a == b)

print("suma", a + b)
print("resta", a - b)
print("multiplicacion", a * b)
print("division", a / b)

#en python, el operador (%) obtiene el residuo de una division
print("modulo", a % b)
#el siguiente signo es doble division y el resultado seria la parte entera 
print("division entera", a // b)
print("potencia", a ** b)
a += 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a -= 2
print(a)
      
operacion_1 = 2 + 3 * 4
print(operacion_1)
operacion_2 = 2 + (3 * 4)
print(operacion_2)
operacion_3 = (2 + 3) * 4
print(operacion_3)
operacion_4 = (2 + 3) * (4 ** 2) / 8 - 1
print(operacion_4)
