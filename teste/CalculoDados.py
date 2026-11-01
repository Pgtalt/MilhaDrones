import pandas as pd


class CalculoDados:
    @staticmethod
    def calcular_media(planilha, conjunto_dados):
        linha = pd.Series(planilha)
        coluna = []
        for valor in conjunto_dados.values():
             coluna.append(valor["Vground"].mean())
        return linha, coluna