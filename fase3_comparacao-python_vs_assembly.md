## Resultados: Comparação Python vs Assembly

### Tabela Comparativa

| N     | Python (ciclos) | Assembly (ciclos) | Redução | Razão |
|------|----------------|-------------------|---------|-------|
| 10   | 29.500         | 39                | 99,87%  | 756x  |
| 100  | 14.000         | 309               | 97,79%  | 45x   |
| 1.000| 55.750         | 3.009             | 94,61%  | 18,5x |

---

## Ciclos de CPU
**Conclusão:** Assembly reduz ciclos de CPU em **94% a 99%**.

---

## Tempo de Execução

### Python (medido)
- N = 10 → 0,0118 ms  
- N = 100 → 0,0056 ms  
- N = 1.000 → 0,0223 ms  

### Assembly (estimado @ 2.5 GHz)
- N = 10 → 15,6 ns  
- N = 100 → 124 ns  
- N = 1.000 → 1,2 µs  

**Conclusão:** Assembly é de **750x a 18x mais rápido**.

---

## Consumo de Energia

### Python (medido @ 15W TDP)
- N = 10 → 0,177 mJ  
- N = 100 → 0,084 mJ  
- N = 1.000 → 0,335 mJ  

### Assembly (estimado @ 15W TDP)
- N = 10 → 0,000234 mJ (234 nJ)  
- N = 100 → 0,00186 mJ (1,86 µJ)  
- N = 1.000 → 0,0181 mJ (18,1 µJ)  

**Conclusão:** Assembly consome **94% a 99% menos energia**.

---

## Extrapolação: Cenário Real em um Eletroporto

### Caso de Uso
**N = 1.000.000 (processamento em tempo real)**

| Métrica                | Python        | Assembly       | Redução |
|----------------------|--------------|---------------|---------|
| Ciclos               | ~25.000.000  | ~3.000.009    | 88%     |
| Tempo                | ~10 ms       | ~1,2 ms       | 8,3x    |
| Energia por operação | ~150 µJ      | ~18 µJ        | 88%     |

---

## Consumo Anual de um Eletroporto (24/7)

### Premissas
- 100.000 operações de controle por segundo  
- TDP do processador: 15W  

---

### Em Python
- Ciclos/segundo: 2,5 trilhões  
- Potência: ~12W contínuos  
- Consumo/dia: 288 Wh  
- Consumo/ano: 105 kWh  

---

### Em Assembly
- Ciclos/segundo: 300 bilhões  
- Potência: ~1,2W contínuos  
- Consumo/dia: 28,8 Wh  
- Consumo/ano: 10,5 kWh  

---

### Economia Anual
- **94,5 kWh economizados**  
- **~€94,50 em energia**  
- **~47 kg de CO₂ não emitidos**