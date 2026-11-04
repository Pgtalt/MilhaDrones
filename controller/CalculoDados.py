import pandas as pd

class CalculoDados:
    @staticmethod
    def calcular_media(planilha, conjunto_dados):
        linha = pd.Series(planilha)
        coluna = []
        for planilha in conjunto_dados.columns:
            coluna.append(conjunto_dados[planilha].mean())
        return linha, coluna