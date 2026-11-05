import pandas as pd

class LeitorDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def retornar_dados(self, planilhas, header=0, colunas=None):
        return pd.read_excel(
            self.arquivo,
            sheet_name=planilhas,
            header=header,
            usecols=colunas
        )