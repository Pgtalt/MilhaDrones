import pandas as pd

from controller.Grafico import GraficosExcel
#from controller.LeitorDados import LeitorDados
from teste.LeitorDadosTest import LeitorDados
from teste.ProcessamentoXlsx import ProcessamentoXlsx


class Visualizador:
    def __init__(self):
        pass

    def gerar_graficos_pesos(self):
        arquivo, planilha = "./arquivo/Data.xlsx", "Demand"
        titulo, eixo_x, eixo_y = "Distribuição peso das encomendas", "Peso da Encomenda (KG)", "Frequência absoluta dos registros"
        leitor = LeitorDados(arquivo)
        dataframe = leitor.ler_planilha(planilha, comeco_linha=0, comeco_coluna=0)
        peso = ProcessamentoXlsx(dataframe)
        grafico = GraficosExcel(peso.ler_coluna("WAGA"))
        res = grafico.histograma(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_velocidade(self):
        arquivo, planilha = "./arquivo/Results.xlsx", ["NO_wind", "Wind_January", "Wind_April", "Wind_July", "Wind_November"]
        titulo, eixo_x, eixo_y = "Velocidade Média dos Drones por Cenário de Vento.", "Cenário (Sem vento, Janeiro, Abril, Julho e Novembro).", "Velocidade média"
        leitor = LeitorDados(arquivo)
        dataframe = leitor.ler_planilha(planilha)
        res = ProcessamentoXlsx(dataframe)
        linha = pd.Series(planilha)
        coluna = []
        for valor in dados_dicionario.values():
             coluna.append(valor["Vground"].mean())
        grafico = GraficosExcel(linha, coluna)
        res = grafico.grafico_barras(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_consumo(self):
        arquivo, planilha = "./arquivo/Results.xlsx", "Comparison"
        titulo, eixo_x, eixo_y = "Comparação do Consumo Energético por Modalidade de Entrega.", "Cenário do Vento", "Valor do consumo energetico"
        linha, coluna = ["UAVs", "Courier"], "NO_wind"
        dataframe = LeitorDados(arquivo)
        dataframe.ler_planilha(planilha=planilha)
        consumo = ProcessamentoXlsx(dataframe)
        dados_dicionario = consumo.obter_dados(planilha=planilha, linha=linha, coluna=coluna, header=1, index_col=0)
        print(dados_dicionario)

        grafico = GraficosExcel(linha, coluna)
        res = grafico.grafico_barras_agrupadas(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()


    def gerar_grafico_distribuicao_espacial(self):
        ...