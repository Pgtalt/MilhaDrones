import pandas as pd

class LeitorDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = None

    def __carregar_arquivo(self, planilha=None):
        if self.arquivo:
            if planilha:
                self.dados = pd.read_excel(self.arquivo, sheet_name=planilha)
            else:
                self.dados = pd.read_excel(self.arquivo, sheet_name=None)
        else:
            raise Exception("Erro 1")

    def gerar_dados(self, planilha=None):
        self.__carregar_arquivo(planilha)
        if self.dados:
            return self.dados
        raise Exception("Dataframe Vazio")

    def gerar_dados_linha(self, planilha, linha):
        self.__carregar_arquivo(planilha)
        if self.dados:
            if isinstance(self.dados, dict):
                df_unificado = pd.concat(self.dados.values(), ignore_index=True)
                return df_unificado.iloc[int(linha)]
            else:
                return self.dados.iloc[int(linha)]
        raise Exception("Linha inexistente ou Dataframe Vazio")
