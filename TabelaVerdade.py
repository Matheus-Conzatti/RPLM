import ttg

# Uma lista com todas as letras do alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    # Lista vazia para fazer o armazenamento das letras da fórmula
    variaveisLista = []

    # O usuário entra com a fórmula
    formula = input('Digite a fórmula em minúscula:')
    if not formula.islower():
        print('ERRO: A fórmula digitada não pode estar em maiúscula!')
        break

    #Adiciona apenas as letras da fórmula à lista de variáveis
    for char in formula:
        if char.isalpha():
            variaveisLista.append(char)


    #Faz a contagem das operações que está na fórmula
    operacoes = {
        'and': formula.count('and'),
        'or': formula.count('or'),
        'not': formula.count('not') + formula.count('~()') + formula.count('~'),
        'implic': formula.count('=>')
    }

    #Faz as contagens das operações e a quantidade de vezes
    print('Operações na fórmula:')
    for operacoes, quantidade in operacoes.items():
        print(f"{operacoes}: {quantidade} vezes.")

    #Armazena na lista vazia para armazenar as letras digitadas
    letrasDigitadas = []

    #Adiciona apenas as letras da fórmula à lista de letra
    for char in formula:
        if char.isalpha():
            letrasDigitadas.append(char)

    #Verifica se as letras que forma digitadas estão no alfabeto
    letrasValidas = [letra for letra in letrasDigitadas if letra in alfabeto]

    #Verifica se as letras não estão dentro dos parenteses
    letraForaParentese = []
    for letra in letrasValidas:
        if (letra not in '()') and (letra not in '~()') and (letra not in 'not()'):
            letraForaParentese.append(letra)

    variaveis = sorted(set(letraForaParentese))

    #Imprime as letras digitadas
    print('Variaveis:', variaveis)

    tabelaVerdade = ttg.Truths(variaveis, [formula])

    #Imprime a tabela verdade
    print("Tabela Verdade")
    print(tabelaVerdade)

    #Pergunta ao usuário se ele deseja sair do programa
    continuar = input('Digite S/N para continuar:')
    if continuar.upper() != 'S':
        break
