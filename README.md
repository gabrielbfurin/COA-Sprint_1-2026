# Projeto Sustentável em Arquitetura de Computadores (COA)

> **EV Challenge 2026 — Sprint 1 (COA)**  
> **Tema:** Sustentabilidade e eficiência computacional em eletropostos por meio de **arquitetura RISC** e **otimização em Assembly (RISC-V)**.

---

## 1) Objetivo do Projeto

Este projeto demonstra, de forma **técnica e mensurável**, como conceitos de **Arquitetura de Computadores** (RISC vs CISC, pipeline, cache, ciclos de CPU) e **programação em baixo nível (Assembly)** impactam diretamente:

- **ciclos de CPU**
- **tempo de execução**
- **consumo energético computacional**

Em cenários de mobilidade elétrica (eletropostos), essas reduções ajudam a:

- diminuir desperdício de energia (computacional)
- viabilizar melhor o uso de **fontes renováveis** (ex.: solar) em sistemas de menor potência
- aumentar eficiência de controle de carga, sensores e autenticação

---

## 2) Problema

Sistemas de eletropostos frequentemente utilizam:

- **software de alto nível** (ex.: Python)
- **hardware genérico**

Mesmo para tarefas simples e repetitivas (leitura de sensores, controle de carga, decisões condicionais), isso pode gerar:

- consumo desnecessário de energia (mais tempo + mais ciclos)
- baixa eficiência no processamento em tempo real
- desperdício de recursos computacionais

---

## 3) Justificativa

A crescente demanda por eletropostos exige soluções eficientes para minimizar o consumo energético. Softwares de alto nível e hardware genérico geram desperdício computacional, impactando a sustentabilidade. Este projeto se justifica pela necessidade de otimizar operações críticas em baixo nível, demonstrando como a arquitetura de computadores pode reduzir diretamente o consumo de energia e viabilizar melhor o uso de fontes renováveis.

---

## 4) Proposta de Solução

Propor um **módulo de controle crítico** otimizado em **Assembly RISC-V**, visando:

- reduzir o número de instruções e ciclos executados
- aproveitar uma arquitetura com pipeline eficiente (RISC)
- ser adequado a **microcontroladores** e **sistemas embarcados de baixo consumo**

A ideia é manter partes não críticas em alto nível (produtividade), e implementar partes críticas (hot paths) em baixo nível, quando o objetivo for **eficiência e previsibilidade**.

---

## 5) Fundamentação Técnica

### 5.1 Relação entre ciclos de CPU e consumo energético

A relação entre ciclos e energia é direta: **mais ciclos ⇒ mais chaveamento de transistores ⇒ maior consumo**.

Modelo simplificado do consumo dinâmico:

P = C . V^2 . f

- **P**: potência (energia por segundo)
- **C**: capacitância efetiva
- **V**: tensão
- **f**: frequência (ciclos por segundo)

Mesmo com frequência baixa, se um programa executa muitas instruções, ele roda por mais tempo e consome mais energia.

### 5.2 Python (alto nível) vs Assembly (baixo nível)

Python (interpretado) executa cada operação através de camadas (bytecode + VM + interpretador), o que aumenta o custo em ciclos por operação.

Exemplo lógico simples:

```python
if battery < 50:
    action = "reduce"
```

Em Assembly (RISC-V), a mesma lógica pode ser reduzida a poucas instruções.

### 5.3 Pipeline e CPI

- Sem pipeline: uma instrução passa por vários estágios sequenciais, aumentando o **CPI** (ciclos por instrução).
- Com pipeline (comum em RISC): várias instruções são processadas em paralelo por estágio, aproximando o throughput de **1 instrução por ciclo** (em condições ideais).

Resultado prático: **pipeline reduz CPI**, reduz ciclos totais e tende a reduzir tempo/energia.

### 5.4 Cache e ciclos

Cache reduz ciclos perdidos em acesso à RAM:

- RAM: dezenas/centenas de ciclos
- L1: ~1–4 ciclos
- L2: ~10 ciclos
- L3: ~30–50 ciclos

Tempo médio de acesso (AMAT):

AMAT = Hit Time + Miss Rate . Miss Penalty

---

## 6) Implementação (Fase 2)

Para demonstrar a diferença entre alto e baixo nível, foi implementado o mesmo algoritmo em duas versões:

- **Python:** soma acumulada de 1 até N com medição de tempo e estimativas
- **RISC-V Assembly:** soma acumulada equivalente com loop em instruções diretas

### 6.1 Python (alto nível)

Arquivo: `fase2_python.py`

- mede tempo de execução com `time.perf_counter()`
- estima ciclos: `ciclos = tempo(s) × frequência(Hz)`
- estima energia: `E = P × t` usando TDP aproximado

### 6.2 Assembly RISC-V (baixo nível)

Arquivo: `fase2_assembly.txt`

Implementa a soma acumulada usando registradores e desvios (`bgt`, `jal`, `jr`). Abaixo, um trecho do código:
```assembly
# Trecho do código em fase2_assembly.txt
soma_acumulada:
    addi a1, zero, 0       # a1 = total = 0
    addi a2, zero, 1       # a2 = i = 1

loop_start:
    bgt a2, a0, loop_end   # if (i > N) sai
    add a1, a1, a2         # total += i
    addi a2, a2, 1         # i++
    jal zero, loop_start   # volta ao inicio do loop

loop_end:
    jr ra                  # retorna
```
---

## 7) Resultados (Fase 3) — Python vs Assembly

Arquivo: `fase3_comparacao-python_vs_assembly.md`

### 7.1 Tabela comparativa

| N     | Python (ciclos) | Assembly (ciclos) | Redução | Razão |
|------|----------------|-------------------|---------|-------|
| 10   | 29.500         | 39                | 99,87%  | 756x  |
| 100  | 14.000         | 309               | 97,79%  | 45x   |
| 1.000| 55.750         | 3.009             | 94,61%  | 18,5x |

**Conclusão:** Assembly reduz ciclos em **94% a 99%**.

### 7.2 Extrapolação (cenário de eletroporto)

Para operações críticas repetidas em tempo real (ex.: controle/decisão), a redução de ciclos pode gerar economia relevante de energia computacional ao longo do tempo.

No cenário estimado (24/7):

- Python: ~105 kWh/ano
- Assembly: ~10,5 kWh/ano
- **Economia:** ~94,5 kWh/ano e ~47 kg de CO₂ evitados

---

## 8) Sustentabilidade (por que isso importa?)

Reduzir custo computacional significa:

- menos energia gasta para realizar as mesmas decisões de controle
- possibilidade de usar hardware mais simples/eficiente (embarcardo)
- melhor compatibilidade com energia renovável (ex.: operação sustentada com solar/bateria)

Em larga escala (muitos eletropostos e operações frequentes), pequenas otimizações multiplicam impacto.

---

## 9) Vídeo Pitch

Roteiro: `fase4_roteiro_video.txt`

**Link do vídeo (YouTube não listado):**

> **COLE O LINK AQUI (quando estiver gravado)**

> Observação: o vídeo deve ter protagonismo dos integrantes (sem narração por IA).

---

## 10) Estrutura do Repositório (Projeto 1)

- `fase1_pipeline_CPU_cache.txt` — pesquisa: ciclos × energia, pipeline e cache
- `fase1_risc_vc_cisc.txt` — pesquisa: RISC vs CISC
- `fase2_python.py` — implementação em Python (alto nível)
- `fase2_assembly.txt` — implementação em Assembly RISC-V (baixo nível)
- `fase3_comparacao-python_vs_assembly.md` — comparação e resultados
- `fase4_roteiro_video.txt` — roteiro do vídeo pitch

---

## 11) Integrantes

| Nome | RM |
|------|----|
| Gabriel Barbosa Furin | 572941 |
| Gabriel de Almeida Santos | 569395 |
| Herbert Soares de Jesus | 571507 |
| Lucas Kiodi Moraca | 571004 |
| Renan Fracalossi Mano da Silva | 569610 |

---

## 12) Como executar

### Python

```bash
python fase2_python.py
```

### Assembly (RISC-V)

Simulador utilizado:

- https://riscv-simulator-five.vercel.app/
