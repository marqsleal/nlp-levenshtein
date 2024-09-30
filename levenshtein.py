import numpy as np
from unidecode import unidecode

def printDistances(distances: np.array, token1len: int, token2len: int):
    for t1 in range(token1len):
        for t2 in range(token2len):
            if (t1 == t2) or ((t1 == token1len-1) and (t2 == token2len-1)):
                print(f'\033[1;30;40m{int(distances[t1][t2])}\033[0m', end=' ')
            else:
                print(f'{int(distances[t1][t2])}', end=' ')
            
        print()

def levenshtein(token1: str, token2: str, printMatrix=False) -> float:
    token1 = unidecode(token1.lower())
    token2 = unidecode(token2.lower())

    token1len = len(token1) + 1
    token2len = len(token2) + 1

    if printMatrix:
        print(f'\nToken 1: {token1} / Token 1 Len: {token1len}\nToken 2: {token2} / Token 2 Len: {token2len}')

    distances = np.zeros(
        (token1len, 
        token2len)
    )

    if printMatrix:
        print(f'\nInitializing Array: \n')

    for t1 in range(token1len):
        distances[t1][0] = t1

        if printMatrix:            
            print(f'Distance Array[{t1}][0]: {distances[t1][0]}')
    
    for t2 in range(token2len):
        distances[0][t2] = t2

        if printMatrix:            
            print(f'Distance Array[0][{t2}]: {distances[0][t2]}')

    if printMatrix:
        print('\nInitialized Distances Array: \n')
        printDistances(distances=distances, token1len=token1len, token2len=token2len)

    a = 0
    b = 0
    c = 0

    if printMatrix:
        print(f'\nAssigning Array: \n') 

    for t1 in range(1, token1len):
        for t2 in range(1, token2len):

            if (token1[t1-1] == token2[t2-1]):                
                distances[t1][t2] = distances[t1-1][t2-1]
                
                if printMatrix:
                    print(f'Distance Array[{t1}][{t2}]: {distances[t1-1][t2-1]}')

            else:
                a = distances[t1][t2-1]
                b = distances[t1-1][t2]
                c = distances[t1-1][t2-1]

                if(a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif(b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

                if printMatrix:
                    print(f'Distance Array[{t1}][{t2}]: {distances[t1][t2]}')

    levenshtein = distances[len(token1)][len(token2)]

    if printMatrix:
        print('\nDistances Array: \n')
        printDistances(distances=distances, token1len=token1len, token2len=token2len)    
        print(f'\nLevenshtein Distance between {token1} and {token2}: {levenshtein}\n')

    return levenshtein