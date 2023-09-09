cont = {}

def validate_pair(a, b, lista_potencias,lista_potencias_mas_uno):
    if  a+b in lista_potencias or (a/b in lista_potencias_mas_uno and a%b == 0):
        return False
    else:
        return True

def find_combinations(tuples_list, current_combination=[], index=0):
    if index == len(tuples_list):
        if len(current_combination) > cont[0]:  
            cont[0] =len(current_combination)
        return
    
    current_tuple = tuples_list[index]
    can_add = all(num not in current_combination for num in current_tuple)

    if can_add:
        new_combination = current_combination + list(current_tuple)
        find_combinations(tuples_list, new_combination, index + 1)
    find_combinations(tuples_list, current_combination, index + 1)
    
def solution(banana_list):
    cont[0] = 0
    potencias_dos = [2 ** n for n in range(1, 32)]
    potencias_dos_mas_uno = [x - 1 for x in potencias_dos[:]]
    banana_list.sort(reverse=True)
    print(banana_list)
    lista_parejas = []
    for i in range(len(banana_list)):
        for j in range(i + 1, len(banana_list)):
            if validate_pair(banana_list[i],banana_list[j],potencias_dos,potencias_dos_mas_uno):
                lista_parejas.append([i,j])

    print(lista_parejas)
    #find_combinations(lista_parejas)
    return len(banana_list) - cont[0]
    

#print(validate_pair(10737,432648))
print(solution([7,1,7893,4,5,7]))

