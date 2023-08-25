def contar_combinaciones_suma(total, elementos, memo={}):
   if (total, tuple(elementos)) in memo:
       return memo[(total, tuple(elementos))]
   if total == 0:
       return 1
   if total < 0 or len(elementos) == 0:
       return 0
   con_primero = contar_combinaciones_suma(total - elementos[0], elementos[1:], memo)
   sin_primero = contar_combinaciones_suma(total, elementos[1:], memo)
   memo[(total, tuple(elementos))] = con_primero + sin_primero
   return memo[(total, tuple(elementos))]

def solution(n):
    numeros = range(1,n,1)
    num_combinaciones = contar_combinaciones_suma(n, numeros)
    return num_combinaciones