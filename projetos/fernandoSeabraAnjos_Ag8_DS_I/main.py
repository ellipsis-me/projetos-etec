# Desenvolver um programa em Python utilizando a estrutura de repetição FOR para coletar e exibir o retorno de uma pesquisa de atendimento ao cliente.
# O programa deve solicitar a digitação do nome, idade e opinião do entrevistado sobre o atendimento prestado, sendo:
# 1: EXCELENTE
# 2: BOM
# 3: RUIM
# A pesquisa deve ser feita com 50 entrevistados.
# Ao final, o programa deverá exibir na tela:
# a) Quantidade de respostas “EXCELENTE”
# b) Quantidade de respostas “RUIM”
# Utilize estruturas de decisão para verificar a opinião do entrevistado.
# Realize testes com 10 entrevistados para validar o funcionamento do programa.
# Compartilhe o projeto completo no seu repositório Github, informe o link do repositório no ambiente virtual.

contagem_excelente = 0
contagem_bom = 0
contagem_ruim = 0

for i in range(5):
    nome_entrevistado = input("Digite o nome do entrevistado: ")
    try:
        idade_entrevistado = int(input("Digite a idade do entrevistado: "))
        opiniao_entrevistado = int(input('''
Digite a opinião do entrevistado sendo
1: EXCELENTE
2: BOM
3: RUIM
Nota do atendimento prestado: '''))

    except ValueError:
        print(f"Idade ou opinião inválidas. Por favor, tente novamente.")
        continue

    if opiniao_entrevistado == 1:
        contagem_excelente += 1
    elif opiniao_entrevistado == 2:
        contagem_bom += 1
    elif opiniao_entrevistado == 3:
        contagem_ruim += 1

print(f"Quantidade de respostas 'EXCELENTE': {contagem_excelente}")
print(f"Quantidade de respostas 'BOM': {contagem_bom}")
print(f"Quantidade de respostas 'RUIM': {contagem_ruim}")
