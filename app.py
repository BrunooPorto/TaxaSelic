import pandas as pd  
import yfinance as yf  
import matplotlib.pyplot as plt  
import seaborn as sns  
from statsmodels.tsa.stattools import grangercausalitytests  
import numpy as np  

# Função para ler a taxa Selic do arquivo Excel  
def read_selic_data(file_path):  
    selic_df = pd.read_excel(file_path)  
    selic_df['data'] = pd.to_datetime(selic_df['data'], format='%d/%m/%Y')  
    selic_df.set_index('data', inplace=True)  
    selic_df['valor'] = selic_df['valor'].astype(float)  
    selic_df = selic_df.resample('B').ffill()  # Forward fill for business days  
    return selic_df  

# Função para obter dados de ações/ETFs  
def get_data(tickers, start_date, end_date):  
    data_df = yf.download(tickers, start=start_date, end=end_date)['Adj Close']  
    
    if isinstance(data_df, pd.Series):  
        data_df = data_df.to_frame()  
    
    returns_df = data_df.pct_change()  
    sector_return = returns_df.mean(axis=1)  # Média dos retornos diários para formar o retorno do setor  
    return sector_return  

# Função para calcular a correlação  
def calculate_correlation(selic_df, ibovespa_return, cyclicals_return, non_cyclicals_return, financial_return, commodities_return):  
    combined_df = pd.concat([selic_df, ibovespa_return, cyclicals_return, non_cyclicals_return, financial_return, commodities_return], axis=1)  
    combined_df.columns = ['Selic', 'Ibovespa', 'Cíclicos', 'Não Cíclicos', 'Financeiro', 'Commodities']  
    combined_df.dropna(inplace=True)  

    correlation = combined_df.corr()  
    print("Correlação entre Selic, Ibovespa e Setores:")  
    print(correlation)  
    
    plt.figure(figsize=(10, 6))  
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)  
    plt.title('Correlação entre Selic, Ibovespa, Cíclicos, Não Cíclicos, Financeiro e Commodities')  
    plt.show()  

# Função para realizar o teste de causalidade de Granger  
def granger_causality(combined_df, max_lag=5):  
    print("Teste de Causalidade de Granger:")  
    for column in combined_df.columns[1:]:  # Exclui a coluna 'Selic' para testar contra ela  
        print(f"\nTeste de Granger entre Selic e {column}:")  
        test_result = grangercausalitytests(combined_df[['Selic', column]].dropna(), max_lag, verbose=True)  

# Função principal  
def main(file_path, start_date, end_date):  
    selic_data = read_selic_data(file_path)  
    selic_data = selic_data.resample('B').ffill()['valor']  
    ibovespa_data = get_data("^BVSP", start_date, end_date)  
    
    cyclicals = ["ARZZ3.SA", "LREN3.SA", "COGN3.SA", "YDUQ3.SA", "GMAT3.SA"]  
    non_cyclicals = ["KRSA3.SA", "PGMN3.SA", "DMVF3.SA", "RDOR3.SA", "MATD3.SA"]  
    financial = ["XP", "BPAC11.SA", "BBAS3.SA", "ITUB", "BBD"]  
    commodities = ["VALE", "PBR", "PRIO3.SA", "SUZB3.SA", "KLBN11.SA"]  
    
    cyclicals_return = get_data(cyclicals, start_date, end_date)  
    non_cyclicals_return = get_data(non_cyclicals, start_date, end_date)  
    financial_return = get_data(financial, start_date, end_date)  
    commodities_return = get_data(commodities, start_date, end_date)  

    if not selic_data.empty and not ibovespa_data.empty and not cyclicals_return.empty and not non_cyclicals_return.empty and not financial_return.empty and not commodities_return.empty:  
        combined_df = pd.concat([selic_data, ibovespa_data, cyclicals_return, non_cyclicals_return, financial_return, commodities_return], axis=1)  
        combined_df.columns = ['Selic', 'Ibovespa', 'Cíclicos', 'Não Cíclicos', 'Financeiro', 'Commodities']  
        combined_df.dropna(inplace=True)  
        
        calculate_correlation(selic_data, ibovespa_data, cyclicals_return, non_cyclicals_return, financial_return, commodities_return)  
        granger_causality(combined_df)  
    else:  
        print("Não foi possível obter os dados necessários.")  

# Exemplo de uso  
file_path = 'TCC - Taxa Selic histórica.2.xlsx'  # Substitua pelo caminho do seu arquivo Excel  
start_date = '2017-01-01'  
end_date = '2023-12-31'  

main(file_path, start_date, end_date)