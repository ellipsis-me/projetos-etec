from colorama import Fore, Style

def definir_cor(nivel):
    matriz_cores = [
        [Fore.RED, "Muito baixo (crítico)"],
        [Fore.YELLOW, "Baixo"],
        [Fore.GREEN, "Médio"],
        [Fore.CYAN, "Alto"],
        [Fore.BLUE, "Muito alto (alerta)"]
    ]
    for i in range(len(matriz_cores)):
        cor = matriz_cores[i][0]
        situacao = matriz_cores[i][1]
        if nivel == i + 1:
            return cor, situacao

niveis_reservatorio = [1, 2, 3, 4, 5]
for nivel in niveis_reservatorio:
    cor, situacao = definir_cor(nivel)
    print(cor + f"Nível do reservatório: {nivel} - Situação: {situacao}")

print(Style.RESET_ALL + "Monitoramento concluído. Estilo do terminal restaurado.")
