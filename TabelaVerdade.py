import ttg

# Uma lista com todas as letras do alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    # Lista que armazena as variáveis
    variaveisLista = []

    # O usuário entra com a fórmula
    formula = input('Digite a fórmula em minúscula:')
    if not formula.islower():
        print('ERRO: A fórmula digitada não pode estar em maiúscula!')
        continue

    # Adiciona apenas as letras da fórmula à lista de variáveis
    for char in formula:
        if char.isalpha() and char in alfabeto:
            variaveisLista.append(char)

    # Faz a contagem das operações que estão na fórmula
    operacoes = {
        'and': formula.count('and'),
        'or': formula.count('or'),
        'not': formula.count('not') + formula.count('~()') + formula.count('~'),
        'implic': formula.count('=>'),
        'nand': formula.count('nand')
    }

    # Deixa em ordem alfabética
    variaveisLista = sorted(set(variaveisLista))

    # Imprime as letras digitadas
    print('Variáveis:', variaveisLista)

    # Faz as contagens das operações e a quantidade de vezes
    print('Operações na fórmula:')
    for operacao, quantidade in operacoes.items():
        if operacao == 'nand':
            print(f"{operacao}: {quantidade} vezes.")
        else:
            print(f"{operacao}: {quantidade} vezes.")

    # Cria a tabela verdade
    tabelaVerdade = ttg.Truths(variaveisLista, [formula])

    # Imprime a tabela verdade
    print("\nTabela Verdade")
    print(tabelaVerdade)

    # Pergunta ao usuário se ele deseja sair do programa
    continuar = input('Digite S/N para continuar:')
    if continuar.upper() != 'S':
        print('Finalizando o processo...')
        break
