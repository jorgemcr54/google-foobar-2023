def solution(banana_list):
    banana_list.sort(reverse=True)
    potencias_dos = [2 ** n for n in range(1, 32)]
    potencias_dos_mas_uno = [x - 1 for x in potencias_dos[:-2]]
    lista_parejas = []
    for i in range(len(banana_list)):
        for j in range(i + 1, len(banana_list)):
            if validate_pair(banana_list[i],banana_list[j],potencias_dos,potencias_dos_mas_uno):
                lista_parejas.append([i,j])
    print(lista_parejas)
    print(len(lista_parejas))


def validate_pair(a, b, lista_potencias,lista_potencias_mas_uno):
    if  a+b in lista_potencias or a/b in lista_potencias_mas_uno:
        return False
    else:
        return True

    

#print(validate_pair(10737,432648))
solution([4,365,21,243,65,7,8])

