from model.Grafico import GraficosExcel
from model.LeitorDados import LeitorDados
from controller.FiltroDataframe import FiltroDataframe
from controller.CalculoDados import CalculoDados


class Visualizador:
    def __init__(self):
        pass

    def gerar_graficos_pesos(self):
        arquivo, planilha = "./arquivo/Data.xlsx", "Demand"
        titulo, eixo_x, eixo_y = "Distribuição peso das encomendas", "Peso da Encomenda (KG)", "Frequência absoluta dos registros"
        leitorDados = LeitorDados(arquivo)
        dataframe = leitorDados.retornar_dados(planilhas=planilha, comeco_linha=0, comeco_coluna=0)
        filtroXls = FiltroDataframe(dataframe)
        grafico = GraficosExcel(filtroXls.ler_coluna("WAGA"))
        res = grafico.histograma(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_velocidade(self):
        arquivo, planilha = "./arquivo/Results.xlsx", ["NO_wind", "Wind_January", "Wind_April", "Wind_July", "Wind_November"]
        titulo, eixo_x, eixo_y = "Velocidade Média dos Drones por Cenário de Vento.", "Cenário (Sem vento, Janeiro, Abril, Julho e Novembro).", "Velocidade média"
        leitorDados = LeitorDados(arquivo)
        dict_dataframe = leitorDados.retornar_dados(planilha, comeco_linha=0, comeco_coluna=0)
        filtroDados = FiltroDataframe(dict_dataframe)
        res = filtroDados.ler_coluna("Vground")
        print(res)
        linha, coluna = CalculoDados.calcular_media(planilha=planilha, conjunto_dados=res)
        grafico = GraficosExcel(linha, coluna)
        res = grafico.grafico_barras(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_consumo(self):
        arquivo, planilha = "./arquivo/Results.xlsx", "Comparison"
        titulo, eixo_x, eixo_y = "Comparação do Consumo Energético por Modalidade de Entrega.", "Cenário do Vento", "Valor do consumo energetico"
        linhas, colunas = ["UAVs", "Courier"], ["NO_wind", "Wind_January", "Wind_April", "Wind_July", "Wind_November"]
        leitorDados = LeitorDados(arquivo)
        dataframe = leitorDados.retornar_dados(planilhas=planilha, comeco_linha=1, comeco_coluna=0, colunas_sel="B:G")
        filtroDados = FiltroDataframe(dataframe)
        consumo = filtroDados.ler_celulas(linha=linhas, coluna=colunas)
        linha_orientada = consumo.T.to_dict(orient='list') #o T é de transpor as chaves de uma linha para colunas, list significa orientar o direcionario para chave --> listas
        cenarios = consumo.columns.tolist()
        grafico = GraficosExcel(linha_orientada, cenarios)
        res = grafico.grafico_barras_agrupadas(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()

    def gerar_grafico_distribuicao_espacial(self):
        arquivo, planilha = "./arquivo/Data.xlsx", ["Nodes", "Parcel lockers", "Demand"]
        titulo, eixo_x, eixo_y = "Distribuição dos Armários e dos Destinos Associados.", "Cenário do Vento", "Valor do consumo energetico"
        linhas, colunas = ["UAVs", "Courier"], ["NO_wind", "Wind_January", "Wind_April", "Wind_July", "Wind_November"]
        leitorDados = LeitorDados(arquivo)
        dataframe = leitorDados.retornar_dados(planilhas=planilha, comeco_linha=1, comeco_coluna=0, colunas_sel="B:G")
        filtroDados = FiltroDataframe(dataframe)
        consumo = filtroDados.ler_celulas(linha=linhas, coluna=colunas)
        linha_orientada = consumo.T.to_dict(
            orient='list')  # o T é de transpor as chaves de uma linha para colunas, list significa orientar o direcionario para chave --> listas
        cenarios = consumo.columns.tolist()
        print(linha_orientada)
        grafico = GraficosExcel(linha_orientada, cenarios)
        res = grafico.grafico_barras_agrupadas(titulo=titulo, titulo_x=eixo_x, titulo_y=eixo_y)
        res.grid(True)
        res.show()