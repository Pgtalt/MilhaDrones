import pandas as pd

from controller.Grafico import GraficosExcel
from controller.LeitorDados import LeitorDados


class Visualizador:
    def __init__(self):
        pass

    def gerar_graficos_pesos(self):
        arquivo, planilha = "./arquivo/Data.xlsx", ["Demand"]
        titulo, eixo_x, eixo_y = "Distribuição peso das encomendas", "Peso da Encomenda (KG)", "Frequência absoluta dos registros"
        demanda = LeitorDados(arquivo)
        peso = demanda.gerar_dados()["Demand"]["WAGA"]  # Coluna WAGA é peso
        grafico = GraficosExcel(peso)
        res = grafico.histograma(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_velocidade(self):
        arquivo, planilha = "./arquivo/Results.xlsx", ["NO_wind", "Wind_January", "Wind_April", "Wind_July", "Wind_November"]
        titulo, eixo_x, eixo_y = "Velocidade Média dos Drones por Cenário de Vento.", "Cenário (Sem vento, Janeiro, Abril, Julho e Novembro).", "Velocidade média"
        demanda = LeitorDados(arquivo)
        dados_dicionario = demanda.gerar_dados(planilha)
        linha = pd.Series(planilha)
        coluna = []
        for valor in dados_dicionario.values():
             coluna.append(valor["Vground"].mean())
        grafico = GraficosExcel(linha, coluna)
        res = grafico.grafico_barras(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_consumo(self):
        arquivo, planilha = "./arquivo/Results.xlsx", ["Comparison"]



    def gerar_grafico_distribuicao_espacial(self):
        ...