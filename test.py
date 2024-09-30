from levenshtein import levenshtein

# Calcular a distância entre 'amor' e 'valor', imprimindo a matriz
distancia = levenshtein('amor', 'valor', True)
print(f'Distância de Levenshtein: {distancia}')
