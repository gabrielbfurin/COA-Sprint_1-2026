"""
=============================================================
 Sprint 1 — Fase 2 | Implementação em Python (Alto Nível)
 Disciplina : Arquitetura de Computadores
 Descrição  : Cálculo de soma acumulada de 1 até N,
              com medição de tempo, ciclos estimados
              e consumo energético aproximado.
=============================================================
"""

import time
import os
import platform

# ─────────────────────────────────────────────
#  CONFIGURAÇÕES
# ─────────────────────────────────────────────
N = 1000         # Limite da soma (1 até N)
CPU_FREQ_GHZ = 2.5     # Frequência estimada do processador (GHz)
TDP_WATTS    = 15.0    # TDP típico de um processador mobile (Watts)

# ─────────────────────────────────────────────
#  FUNÇÕES AUXILIARES
# ─────────────────────────────────────────────

def ciclos_estimados(tempo_segundos: float, freq_ghz: float) -> int:
    """
    Estima o número de ciclos de CPU consumidos.
    Fórmula: ciclos = tempo(s) × frequência(Hz)
    """
    return int(tempo_segundos * freq_ghz * 1e9)


def energia_estimada_mj(tempo_segundos: float, tdp_watts: float) -> float:
    """
    Estima a energia consumida em milijoules.
    Fórmula: E = P × t  (Potência × Tempo)
    """
    return tdp_watts * tempo_segundos * 1000  # converte J → mJ


def info_sistema() -> dict:
    """Retorna informações básicas do sistema."""
    return {
        "SO"        : platform.system(),
        "Arquitetura": platform.machine(),
        "Processador": platform.processor() or "Não identificado",
        "Python"    : platform.python_version(),
        "PID"       : os.getpid(),
    }


# ─────────────────────────────────────────────
#  ALGORITMO: SOMA ACUMULADA (loop simples)
#  Equivalente direto ao que será feito
#  em Assembly na Fase 2.
# ─────────────────────────────────────────────

def soma_acumulada(n: int) -> int:
    """
    Soma todos os inteiros de 1 até n usando loop explícito.
    Propositalmente NÃO usa a fórmula de Gauss (n*(n+1)/2)
    para forçar iteração real e tornar a comparação com
    Assembly mais direta (instrução por instrução).
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ─────────────────────────────────────────────
#  EXECUÇÃO E MEDIÇÃO
# ─────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  Sprint 1 — Fase 2 | Python (Alto Nível)")
    print("  Algoritmo : Soma acumulada de 1 até N")
    print("=" * 55)

    # Info do sistema
    info = info_sistema()
    print("\n[SISTEMA]")
    for chave, valor in info.items():
        print(f"  {chave:<14}: {valor}")

    print(f"\n[PARÂMETROS]")
    print(f"  N               : {N:,}")
    print(f"  Freq. CPU (est.): {CPU_FREQ_GHZ} GHz")
    print(f"  TDP (est.)      : {TDP_WATTS} W")

    # ── Medição ──
    print("\n[EXECUTANDO...]")
    inicio = time.perf_counter()
    resultado = soma_acumulada(N)
    fim = time.perf_counter()

    tempo_s   = fim - inicio
    tempo_ms  = tempo_s * 1000
    ciclos    = ciclos_estimados(tempo_s, CPU_FREQ_GHZ)
    energia   = energia_estimada_mj(tempo_s, TDP_WATTS)

    # ── Resultados ──
    print("\n[RESULTADOS]")
    print(f"  Resultado       : {resultado:,}")
    print(f"  Tempo           : {tempo_ms:.4f} ms")
    print(f"  Ciclos (est.)   : {ciclos:,}")
    print(f"  Energia (est.)  : {energia:.6f} mJ")

    # ── CPI estimado ──
    # Em Python, cada iteração do loop envolve múltiplas
    # instruções de bytecode → estimamos ~10 instruções por iteração
    instrucoes_estimadas = N * 10
    cpi = ciclos / instrucoes_estimadas if instrucoes_estimadas else 0

    print(f"\n[ANÁLISE]")
    print(f"  Instruções (est.): {instrucoes_estimadas:,}")
    print(f"  CPI estimado     : {cpi:.2f} ciclos/instrução")
    print(f"  Overhead Python  : bytecode + interpretador + GC")
    print(f"\n  → Em Assembly, o mesmo algoritmo usaria ~3")
    print(f"    instruções por iteração (MOV, ADD, CMP/JMP),")
    print(f"    com CPI próximo de 1 por instrução.")

    print("\n" + "=" * 55)
    print("  Dados prontos para comparação na Fase 3")
    print("=" * 55)

    # ── Retorno estruturado para uso na Fase 3 ──
    return {
        "linguagem"           : "Python",
        "n"                   : N,
        "resultado"           : resultado,
        "tempo_ms"            : round(tempo_ms, 4),
        "ciclos_estimados"    : ciclos,
        "energia_mj"          : round(energia, 6),
        "instrucoes_estimadas": instrucoes_estimadas,
        "cpi_estimado"        : round(cpi, 2),
    }


if __name__ == "__main__":
    dados = main()