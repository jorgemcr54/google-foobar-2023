from fractions import Fraction
def calcular_matriz_trans(matriz):
    for i in range(len(matriz)):
        denominador = sum(matriz[i])
        for j in range(len(matriz[0])):
            if denominador != 0:
                matriz[i][j] = Fraction(matriz[i][j],denominador)
    return matriz

def extraer_matriz_no_absorbentes(matriz):
    lista_no_absorbentes = []
    for i in range(len(matriz)):
        if sum(matriz[i]) != 0:
            lista_no_absorbentes.append(i)
    matriz_no_absorbentes = [[0 for _ in range(len(lista_no_absorbentes))] for _ in range(len(lista_no_absorbentes))]
    for i in lista_no_absorbentes:
        for j in lista_no_absorbentes:
            matriz_no_absorbentes[lista_no_absorbentes.index(i)][lista_no_absorbentes.index(j)] = matriz[i][j]
    return matriz_no_absorbentes

def extraer_matriz_absorbentes(matriz):
    lista_no_absorbentes = []
    lista_absorbentes = list(range(len(matriz)))
    for i in range(len(matriz)):
        if sum(matriz[i]) != 0:
            lista_no_absorbentes.append(i)
            lista_absorbentes.remove(i)
    matriz_absorbentes = [[0 for _ in range(len(lista_absorbentes))] for _ in range(len(lista_no_absorbentes))]

    for i in lista_no_absorbentes:
        for j in lista_absorbentes:
            matriz_absorbentes[lista_no_absorbentes.index(i)][lista_absorbentes.index(j)] = matriz[i][j]
    return matriz_absorbentes

def restar_matriz_identidad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                matriz[i][j] = Fraction(1,1) - matriz[i][j]
            else:
                matriz[i][j] = 0 - matriz[i][j]
    return matriz

def matriz_adjunta(matriz):
    n = len(matriz)
    adjunta = []
    for i in range(n):
        fila_adjunta = []
        for j in range(n):
            submatriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i]+matriz[i+1:])]
            determinante = determinante_matriz(submatriz)
            signo = (-1) ** (i + j)
            fila_adjunta.append(signo * determinante)
        adjunta.append(fila_adjunta)
    return adjunta


def multiplicar_matrices(matriz1, matriz2):
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return (a * b) // calcular_mcd(a, b)

def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def calcular_matriz_inversa(matriz):
    n = len(matriz)
    matriz_extendida = [fila + fila_identidad for fila, fila_identidad in zip(matriz, matriz_identidad(n))]
    for i in range(n):
        pivote = matriz_extendida[i][i]
        if pivote == 0:
            raise ValueError("La matriz no tiene inversa, el pivote es cero.")
        for j in range(i, 2*n):
            matriz_extendida[i][j] /= pivote
        
        for k in range(n):
            if k == i:
                continue
            factor = matriz_extendida[k][i]
            for j in range(i, 2*n):
                matriz_extendida[k][j] -= factor * matriz_extendida[i][j]
    matriz_inversa = [fila[n:] for fila in matriz_extendida]
    return matriz_inversa


def solution(m):
    matriz = calcular_matriz_trans(m)
    matriz_absorbentes = extraer_matriz_absorbentes(matriz)
    matriz_no_absorbentes = extraer_matriz_no_absorbentes(matriz)
    matriz_menos_identidad = restar_matriz_identidad(matriz_no_absorbentes)
    matriz_inversa = calcular_matriz_inversa(matriz_menos_identidad)
    matriz_final = multiplicar_matrices(matriz_inversa,matriz_absorbentes)
    denominadores = []
    respuesta = [] 
    denominador = matriz_final[0][0].denominator
    
    for i in range(len(matriz_final[0])):
        denominadores.append(matriz_final[0][i].denominator)
        respuesta.append(matriz_final[0][i].numerator)
        denominador = calcular_mcm(denominador,matriz_final[0][i].denominator)
    
    

    for i in range(len(respuesta)):
        respuesta[i] = int((denominador/denominadores[i])*respuesta[i])

    respuesta.append(denominador)
    
    return(respuesta)