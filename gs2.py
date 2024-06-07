import random
import json

# Função para capturar dados simulados
def capturar_dados(num_entradas):
    dados = []
    for _ in range(num_entradas):
        entrada = {
            "plastico_kg": random.uniform(0, 50),
            "poluicao_quimica_ppm": random.uniform(0, 100),
            "temperatura_c": random.uniform(10, 30)
        }
        dados.append(entrada)
    return dados

# Função para processar dados
def processar_dados(dados):
    if not dados:
        return {}
    
    total_plastico = sum(d["plastico_kg"] for d in dados)
    total_poluicao = sum(d["poluicao_quimica_ppm"] for d in dados)
    total_temperatura = sum(d["temperatura_c"] for d in dados)
    
    media_plastico = total_plastico / len(dados)
    media_poluicao = total_poluicao / len(dados)
    media_temperatura = total_temperatura / len(dados)
    
    max_plastico = max(d["plastico_kg"] for d in dados)
    min_plastico = min(d["plastico_kg"] for d in dados)
    
    max_poluicao = max(d["poluicao_quimica_ppm"] for d in dados)
    min_poluicao = min(d["poluicao_quimica_ppm"] for d in dados)
    
    max_temperatura = max(d["temperatura_c"] for d in dados)
    min_temperatura = min(d["temperatura_c"] for d in dados)
    
    estatisticas = {
        "media_plastico": media_plastico,
        "media_poluicao": media_poluicao,
        "media_temperatura": media_temperatura,
        "max_plastico": max_plastico,
        "min_plastico": min_plastico,
        "max_poluicao": max_poluicao,
        "min_poluicao": min_poluicao,
        "max_temperatura": max_temperatura,
        "min_temperatura": min_temperatura
    }
    
    return estatisticas

# Função para apresentar dados
def apresentar_dados(estatisticas):
    if not estatisticas:
        print("Nenhuma estatística disponível para apresentar.")
        return
    
    print("Estatísticas dos Dados de Poluição Marinha:")
    print(f"Média de Plástico (kg): {estatisticas['media_plastico']:.2f}")
    print(f"Média de Poluição Química (ppm): {estatisticas['media_poluicao']:.2f}")
    print(f"Média de Temperatura da Água (°C): {estatisticas['media_temperatura']:.2f}")
    print(f"Máximo de Plástico (kg): {estatisticas['max_plastico']:.2f}")
    print(f"Mínimo de Plástico (kg): {estatisticas['min_plastico']:.2f}")
    print(f"Máximo de Poluição Química (ppm): {estatisticas['max_poluicao']:.2f}")
    print(f"Mínimo de Poluição Química (ppm): {estatisticas['min_poluicao']:.2f}")
    print(f"Máximo de Temperatura da Água (°C): {estatisticas['max_temperatura']:.2f}")
    print(f"Mínimo de Temperatura da Água (°C): {estatisticas['min_temperatura']:.2f}")

# Função para salvar dados em um arquivo
def salvar_dados(estatisticas, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(estatisticas, file)
        print(f"Estatísticas salvas no arquivo {filename}.")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {e}")

# Função principal
def main():
    try:
        dados = capturar_dados(100)
        estatisticas = processar_dados(dados)
        apresentar_dados(estatisticas)
        salvar_dados(estatisticas, "estatisticas.json")
    except Exception as e:
        print(f"Ocorreu um erro no sistema: {e}")

if __name__ == "__main__":
    main()