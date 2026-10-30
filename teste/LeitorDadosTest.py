import pandas as pd

class LeitorDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def ler_planilha(self, planilha, comeco_linha=None, comeco_coluna=None, forcar_str=False):
        eLinha = str if forcar_str else None
        return pd.read_excel(self.arquivo, sheet_name=planilha, skiprows=comeco_linha, skipfooter=comeco_coluna)
        #return pd.read_excel(self.arquivo, sheet_name=planilha, header=comeco_linha, index_col=comeco_coluna, dtype=eLinha)


