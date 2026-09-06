# -*- coding: utf-8 -*-
import sys

# Força o terminal a interpretar texto e emojis em UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")

# Calculadora de Consumo Elétrico Inteligente

def calcular_consumo():
    print("=" * 45)
    print("CALCULADORA DE CONSUMO ELETRICO INTELIGENTE")
    print("=" * 45)

    # 1. Entrada de dados
    aparelho = input("\nNome do aparelho (ex: Geladeira): ").strip()
    
    # Validações com estruturas condicionais (if/else)
    try:
        potencia = float(input("Potencia do aparelho em Watts (W): "))
        horas_dia = float(input("Tempo medio de uso diario em horas: "))
    except ValueError:
        print("\n[Erro]: Por favor, insira apenas valores numericos validos.")
        return

    # Verificação de valores lógicos
    if potencia <= 0 or horas_dia <= 0:
        print("\n[Erro]: Potencia e tempo de uso devem ser maiores que zero.")
        return
    elif horas_dia > 24:
        print("\n[Erro]: O dia possui apenas 24 horas! Verifique o tempo informado.")
        return

    # 2. Processamento (Fórmula de consumo)
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Cálculo extra do custo estimado (Tarifa média: R$ 0,75 por kWh)
    valor_tarifa = 0.75
    custo_estimado = consumo_mensal * valor_tarifa

    # 3. Saída formatada
    print("\n" + "-" * 35)
    print("RESULTADO DA ESTIMATIVA:")
    print("-" * 35)
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mes")
    print(f"Custo aproximado: R$ {custo_estimado:.2f} (base: R$ {valor_tarifa:.2f}/kWh)")
    print("-" * 35)

if __name__ == "__main__":
    calcular_consumo()