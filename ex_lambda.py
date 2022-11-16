"""
Universidad del valle de Guatemala
Teoría de la computación 
13/11/2022
@author Marco Jurado 20308

Expresiones utilizando funciones lambda para determinar
la diferencia de las mismas usando beta y alpha.
sintaxis --> lambda argumentos : expresion
"""

#primero se define alpha y beta
alpha_lambda = lambda x: x + 1
beta_lambda = lambda x: 2 * x

#funciones de numeros utilizando lambda
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))

#funciones de operaciones utilizando lambda
sucessor = lambda n: lambda f: lambda x: f(n(f) (x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f) (x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f)) (x)
potencia = lambda a: lambda b: lambda f: lambda x: a(b) (f) (x)

#ejemplos de uso de funciones
"""
beta
@description
@params 
"""
print('beta > ', beta_lambda(1))
print(' ')

"""
alpha
@description
@params 
"""
print('alpha > ', alpha_lambda(1))
print(' ')

"""
cero
@description
@params 
"""
print('cero con alpha > ', cero(alpha_lambda)(2))
print('cero con beta > ', cero(beta_lambda)(2))
print(' ')

"""
uno
@description
@params 
"""
print('uno con alpha > ', uno(alpha_lambda)(3))
print('uno con beta > ', uno(beta_lambda)(3))
print(' ')

"""
dos
@description
@params 
"""
print('dos con alpha > ', dos(alpha_lambda)(2))
print('dos con beta > ', dos(beta_lambda)(2))
print(' ')

"""
tres
@description
@params 
"""
print('tres con alpha > ', tres(alpha_lambda)(2))
print('tres con beta > ', tres(beta_lambda)(2))
print(' ')

"""
sucessor
@description
@params 
"""
print('sucessor con alpha > ', sucessor(cero)(alpha_lambda)(1))
print('sucessor con beta > ', sucessor(cero)(beta_lambda)(1))
print(' ')

"""
suma
@description
@params 
"""
print('suma con alpha > ', suma(dos)(dos)(alpha_lambda)(1))
print('suma con beta > ', suma(dos)(dos)(beta_lambda)(1))
print(' ')

"""
multiplicacion
@description
@params 
"""
print('multiplicacion con alpha > ', multiplicacion(uno)(dos)(alpha_lambda)(2))
print('multiplicacion con beta > ', multiplicacion(uno)(dos)(beta_lambda)(2))
print(' ')


"""
potencia
@description
@params 
"""
print('potencia con alpha > ', potencia(dos)(tres)(alpha_lambda)(2))
print('potencia con beta > ', potencia(dos)(tres)(beta_lambda)(2))
print(' ')