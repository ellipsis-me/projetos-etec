try:
    nome_aparelho = input("Digite o nome do aparelho para calcular o gasto de energia mensal: ")
    potencia_aparelho = float(input("Digite a potência do aparelho em watts (W): "))

    tempo_uso_medio_diario = float(input("Digite o tempo médio de uso diário do aparelho em horas: "))

    custo_regional_kwh = float(input('''Use este mapa para ver o preço médio do kWh por região https://clarke.com.br/mapa-de-tarifas-de-energia-no-brasil
Digite o custo regional do kWh em reais (ex.: R$ 0.75 por kWh): '''
        ))

    consumo_mensal_kwh = (potencia_aparelho * tempo_uso_medio_diario * 30) / 1000

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos.")
    exit()
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
    exit()


print(
f'''
Aparelho: {nome_aparelho}
Consumo estimado: {consumo_mensal_kwh:.0f} kWh/mês
Custo mensal estimado: R$ {consumo_mensal_kwh * custo_regional_kwh:.2f}
'''
)
