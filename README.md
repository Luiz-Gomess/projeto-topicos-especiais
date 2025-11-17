# 🏨 Classificação de Reservas de Hotel por Faixa de Preço  
Disciplina: Tópicos Especiais (2025.2)

Este repositório contém o pipeline de preparação, limpeza, transformação e engenharia de atributos aplicado ao dataset **Hotel Booking Demand**, com o objetivo de construir um modelo capaz de classificar reservas de hotel em **faixas de preço**: Econômica, Padrão, Premium ou Luxo.

O trabalho corresponde à **1ª entrega da equipe Securitas**, do curso de Sistemas para Internet (IFPB), relacionada à etapa de *Tratamento dos dados do Dataset*.

---

## 📄 Dicionário de Dados 

O dicionário oficial de dados utilizado neste projeto está disponível no arquivo:

👉 **[📘 dicionario_de_dados.md](./dicionario_de_dados.md)**

Ele descreve todas as variáveis do dataset original, seus significados, tipos e usos dentro da modelagem.


---

## 📌 Objetivo do Projeto

Desenvolver um sistema de **Aprendizado de Máquina supervisionado** para prever em qual faixa de preço uma reserva de hotel se enquadra, com base em variáveis presentes no dataset.


As faixas utilizadas foram definidas com base nos quartis da variável `adr`:

| Faixa | Regra |
|-------|-------|
| **Econômica** | adr < 74.0 |
| **Padrão** | 74.0 ≤ adr < 99.0 |
| **Premium** | 99.0 ≤ adr < 135.0 |
| **Luxo** | adr ≥ 135.0 |

---

## 👥 Equipe — *Codinome*: Securitas

- Luiz Fernando (líder)  
- João Vittor  
- Kauã Victor  
- Lucas Kaique 
- Silas Leão

---

## 📂 Dataset Utilizado

**Nome:** Hotel Booking Demand  
**Origem:** Kaggle  
**Link:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand  

**Resumo do Dataset:**

| Métrica | Valor |
|--------|--------|
| Total de instâncias | 85.586 |
| Atributos preditores | 31 |
| Atributo alvo | `faixa_preco` |
| Classes | 4 (Econômica, Padrão, Premium, Luxo) |

A distribuição original das classes é balanceada (~25% cada).

---

## 🧹 1. Limpeza de Dados

O código realiza um conjunto de etapas para remover inconsistências, garantir qualidade e preparar os dados para modelagem.

### 🔍 Remoção de Duplicatas
- Identificamos **31.994** linhas duplicadas.
- Removidas com `drop_duplicates()`.

### 🚫 Remoção de Reservas sem Hóspedes
Linhas com `adults == 0`, `children == 0` e `babies == 0` foram descartadas:  
→ Indicam reservas inconsistentes.

### ❓ Tratamento de Valores Ausentes (Nulos)

| Coluna | Ação |
|--------|------|
| `company` | preenchido com **0** (ID inválido → "não informado") |
| `agent` | preenchido com **0** |
| `country` | preenchido com a **moda** (valor mais frequente: `PRT`) |

### 🧭 Tratamento da Variável `adr`
- Valores negativos não fazem sentido → removidos  
- Valores igual a 0 foram removidos  
  - justificativa: impossibilitam classificar faixa de preço  
  - podem representar gratuidades, não configurando dados úteis para o modelo  

---

## 🧪 2. Transformação e Engenharia de Atributos

### 🎯 Criação da Variável Alvo `faixa_preco`
A coluna `adr` foi segmentada em 4 grupos usando quartis:

```python
df_limpo['faixa_preco'] = pd.cut(
    df_limpo['adr'],
    bins=[-inf, q1, q2, q3, inf],
    labels=['Econômica', 'Padrão', 'Premium', 'Luxo'],
    right=False
)
