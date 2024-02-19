import json

def calcular_estatisticas_faturamento(dados):
    dias_com_faturamento = [registro["valor"] for registro in dados if registro["valor"] > 0]

    if not dias_com_faturamento:
        print("Não há dados de faturamento para calcular estatísticas.")
        return

    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for registro in dados if registro["valor"] > media_mensal)

    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias acima da média: {dias_acima_media}")


with open('dados.json', 'r') as file:
    dados = json.load(file)

calcular_estatisticas_faturamento(dados)


