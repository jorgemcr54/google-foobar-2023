def solution(banana_list):
    print(validate_pair(13,19))

def validate_pair(a, b):
    list_pairs = []
    list_pairs.append([a,b])
    print(str(a) + ' ' + str(b))
    cont = 0
    while(True):
        cont=cont+1
        print(cont) 
        print(str(a) + ' ' + str(b))
        if a>b:
            a=a-b
            b=b*2
        elif a<b:
            b=b-a
            a=a*2
        elif a==b:
            return False
        if [a,b] in list_pairs:
            return True
        else:
            list_pairs.append([a,b])
            list_pairs.append([b,a])
     

    

print(validate_pair(10737,432648))

