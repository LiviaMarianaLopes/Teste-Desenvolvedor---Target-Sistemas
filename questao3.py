import json


def calcular_estatisticas_faturamento(nome_arquivo):
    """Função para calclar maior valor, menor valor e quantidade de dias acima da média de um vetor"""
    with open(nome_arquivo, 'r') as arquivo:
        faturamento = json.load(arquivo)

    valores_faturamento = [dia['valor'] for dia in faturamento]
    # salva apenas os dias com faturamento
    dias_com_faturamento = [dia['dia'] for dia in faturamento if dia['valor'] > 0]
    media_do_mes = sum(valores_faturamento) / len(dias_com_faturamento)
    menor_valor = min(valores_faturamento)
    maior_valor = max(valores_faturamento)
    dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_do_mes)

    return menor_valor, maior_valor, dias_acima_da_media


# Váriavel com o nome do arquivo JSON
nome_arquivo = 'dados.json'

# salva as estatísticas do faturamento
menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas_faturamento(nome_arquivo)

print(f'Menor valor: R${menor_valor:.2f}\n'
      f'Maior valor: R${maior_valor:.2f}\n'
      f'Quantidade de dias acima da média mensal: {dias_acima_da_media}')
