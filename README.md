# Projeto: SafeStock

## 🧠 Sobre o Projeto

Este projeto tem como foco o desenvolvimento de um sistema inteligente para apoiar a **gestão de abrigos emergenciais** durante **eventos extremos da natureza**, como enchentes, deslizamentos e ondas de calor intenso.

## 🔍 Objetivo

O objetivo principal é utilizar dados históricos e variáveis ambientais para **prever a quantidade de pessoas** que podem ocupar um abrigo e, com base nisso, **planejar os recursos necessários**.

## 🧰 Tecnologias Utilizadas

- **Python + Pandas/Scikit-Learn**: Processamento e análise dos dados, treinamento do modelo preditivo.
- **Streamlit**: Criação de um dashboard interativo para visualização em tempo real.
- **Jupyter Notebook**: Para testes e ajustes no modelo.
  
## 📊 Dataset

Criei um dataset simulado com variáveis como:
- Volume de chuva (mm)
- Temperatura (°C)
- Índice de vulnerabilidade da região
- Número de eventos extremos anteriores
- Distância até a cidade mais próxima
- Capacidade do abrigo
- Pessoas previstas
- Quantidade de água, refeições e kits médicos necessários

> Após a primeira versão, adaptei o CSV para representar **cenários mais extremos**, com chuvas acima de 600mm, temperaturas entre -10°C e 45°C e alta vulnerabilidade, para avaliar a robustez do modelo em situações críticas.

## 🤖 Machine Learning

Utilizei um modelo de **regressão** para prever o número de pessoas que ocuparão o abrigo com base nas variáveis climáticas e estruturais. A partir disso, são estimados automaticamente os recursos necessários.

### Funcionalidades do modelo:
- Previsão da ocupação do abrigo
- Cálculo automático de litros de água, refeições e kits médicos
- Avaliação da severidade do cenário

## 🖥️ Dashboard

O dashboard foi feito com Streamlit e oferece:
- Visualização de cenários em tempo real
- Gráficos de tendência e distribuição
- Alertas visuais para situações críticas
- Interface simples para tomada de decisão

## 🧪 Testes

Realizei testes com diferentes cenários, desde normais até extremos, para validar:
- A precisão do modelo de previsão
- O comportamento do sistema em situações críticas
- A adequação das recomendações de recursos

Para realização de novos testes:
```bash
pip install pandas scikit-learn streamlit matplotlib
```
```bash
streamlit run app_abrigo.py
```

## 🚀 Ideia para uma possível atualização

- Integrar sistema de alerta via SMS/WhatsApp para coordenação de abrigos, com uso de sensores via ESP32 para medir o nível da água e temperatura no local.
