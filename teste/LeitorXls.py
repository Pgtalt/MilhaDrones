import pandas as pd

class LeitorXls:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.planilha = None
        self.eLinha = None
        self.comeco_coluna = None
        self.comeco_linha = None

    def ler_planilha(self, planilha, comeco_linha=0, comeco_coluna=0, forcar_str=False):
        self.planilha = planilha
        self.eLinha = str if forcar_str else None
        self.comeco_coluna = comeco_coluna
        self.comeco_linha = comeco_linha
        #return pd.read_excel(self.arquivo, sheet_name=planilha, header=comeco_linha, index_col=comeco_coluna, dtype=eLinha)

    def retornar_dataframe(self):
        if not self.planilha:
            raise Exception("Não foi passada uma planilha")
        if isinstance(self.planilha, str):
            return pd.read_excel(self.arquivo, sheet_name=self.planilha, skiprows=self.comeco_linha,
                                 skipfooter=self.comeco_coluna)
        raise Exception("A planilha deve ser uma String")

    def retornar_dict_dataframe(self):
        if not self.planilha:
            raise Exception("Não foi passada uma planilha")
        planilha_lst = self.planilha
        if isinstance(planilha_lst, str):
            planilha_lst = [planilha_lst]
        return pd.read_excel(self.arquivo, sheet_name=planilha_lst, skiprows=self.comeco_linha,
                             skipfooter=self.comeco_coluna)