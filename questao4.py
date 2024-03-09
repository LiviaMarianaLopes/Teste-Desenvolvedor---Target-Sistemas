def calcular_percentuais_faturamento(faturamento_estado):
    """Função que retorna um dicionario com os estados e seus respectivos percentuais do faturamento"""
    total_mensal = sum(faturamento_estado.values())

    # Calcula o percentual de representação de cada estado
    percentuais_por_estado = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in
                              faturamento_estado.items()}

    return percentuais_por_estado


# Valores do faturamento mensal de cada estado
faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula os percentuais de representação de faturamento
percentuais_estado = calcular_percentuais_faturamento(faturamento_estado)

print("Percentual de representação de faturamento por estado:")

# Exibe os estados com seus respectivos porcentuais
for estado, percentual in percentuais_estado.items():
    print(f"{estado}: {percentual:.2f}%")
