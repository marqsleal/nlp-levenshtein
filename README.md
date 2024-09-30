# NLP LEVENSHTEIN - Distância de Levenshtein aplicada ao processamento de linguagem natural
_Projeto para fins acadêmicos criando uma implementação manual da Distância de Levenshtein na linguagem Python._

## Dependências 

Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt
```

## Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/marqsleal/nlp-levenshtein.git
```

2. Execute o arquivo `test.py`:

```bash
python3 test.py
```
## Distância de Levenshtein 

A distância de Levenshtein é uma medida de similaridade de texto que compara duas palavras e retorna um valor numérico representando a distância entre elas. A distância reflete o total de alterações feitas por caractere que são necessárias para transformar uma palavra na outra. Quanto mais similiar ambas palavras são, menor a distância entre elas, e vice e versa.

## Código:
```python
def levenshtein(token1: str, token2: str, printMatrix=False) -> float:
    token1 = unidecode(token1.lower())
    token2 = unidecode(token2.lower())

    token1len = len(token1) + 1
    token2len = len(token2) + 1

    distances = np.zeros(
        (token1len, 
        token2len)
    )

    for t1 in range(token1len):
        distances[t1][0] = t1

    for t2 in range(token2len):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, token1len):
        for t2 in range(1, token2len):

            if (token1[t1-1] == token2[t2-1]):                
                distances[t1][t2] = distances[t1-1][t2-1]
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

    levenshtein = distances[len(token1)][len(token2)]

    return levenshtein
```

- Utilização do `numpy` para a criação de Arrays;
- Utilização do `unidecode` para a normalização dos tokens;