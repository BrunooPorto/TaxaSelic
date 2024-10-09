# Análise de Correlação entre Selic, Ibovespa e Setores da Bolsa

Este projeto analisa a correlação entre a taxa Selic, o Ibovespa e os retornos de setores da bolsa brasileira (Cíclicos, Não Cíclicos, Financeiro e Commodities). A análise utiliza dados do Yahoo Finance e um arquivo histórico da taxa Selic.

## Funcionalidades

- **Correlação**: Calcula e plota a correlação entre a Selic e os setores.
- **Teste de Causalidade de Granger**: Avalia a relação de causalidade entre a taxa Selic e os setores.

## Dependências

Para rodar o projeto, instale as seguintes bibliotecas:

```bash
pip install pandas yfinance matplotlib seaborn statsmodels numpy

Como usar
1.Adicione seu arquivo da Taxa Selic no formato Excel.
2.Configure as variáveis start_date, end_date e o caminho do arquivo file_path no código.
3.Execute o script principal para visualizar os gráficos de correlação e os resultados do teste de causalidade.

# Selic Analysis Project

This project analyzes the relationship between the Selic rate and various asset classes in the Brazilian market.

**Features:**

* Downloads Selic rate data from an Excel file (replace with the actual features)
* Downloads data for Ibovespa and other relevant indices (replace with actual indices)
* Calculates correlations between Selic and other assets
* Performs Granger causality tests to explore potential causal relationships

**Requirements:**

* Python 3 (or later)
* pandas
* yfinance
* matplotlib
* seaborn
* statsmodels

**Usage:**

1. Replace `'TCC - Taxa Selic histórica.2.xlsx'` in `main` with the path to your Selic data file.
2. Adjust start and end dates (`start_date` and `end_date`) as needed.
3. Run the script: `python selic_analysis.py`
