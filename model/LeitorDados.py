import pandas as pd

class LeitorDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def retornar_dados(self, planilhas, comeco_linha=0, comeco_coluna=0, colunas_sel=None, forcar_str=False):
        valor = str if forcar_str else None
        return pd.read_excel(
            self.arquivo, sheet_name=planilhas, header=comeco_linha, index_col=comeco_coluna, dtype=valor, usecols=colunas_sel)