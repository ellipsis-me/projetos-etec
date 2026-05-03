# função para calcular a média das notas
def calcular_media(notas):
    media = sum(notas) / len(notas) # soma todas as notas e divide pelo número de notas para obter a média
    return media # retorna a média calculada

# lista de notas do aluno
notas = [8.5, 7.0, 9.5, 6.0, 8.0]
# chama a função para calcular a média das notas e armazena o resultado na variável media
media = calcular_media(notas)

# exibe a média das notas para o usuário
print(f"A média das notas é: {media}")


# função para verificar se o aluno foi aprovado ou reprovado com base na média das notas
def verificar_aprovacao(media, corte):
    # Retorna True se a média for maior ou igual à nota de corte, indicando aprovação. 
    # Caso contrário, retorna False, indicando reprovação.
    return media >= corte 

# define a nota de corte para aprovação
corte = 7.0
aprovacao = verificar_aprovacao(media, corte)

# exibe a situação do aluno com base na aprovação ou reprovação.
print(f"Situação do aluno: {'Aprovado' if aprovacao else 'Reprovado'}")