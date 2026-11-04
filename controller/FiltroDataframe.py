import pandas as pd

class FiltroDataframe:
    def __init__(self, dataframe):
        if not isinstance(dataframe, (pd.DataFrame, dict)):
            raise Exception("Não é um formato de dados válido para filtragem")
        self.dataframe = dataframe

    def todos_dados(self):
        return self.dataframe

    def _ler_dict_dataframe(self, coluna, planilha):
        if planilha:
            if isinstance(coluna, str):
                return self.dataframe[planilha][coluna]
        else:
            return pd.DataFrame({
                nome_planilha: df[coluna]
                for nome_planilha, df in self.dataframe.items()
                if coluna in df.columns
            })

    def _ler_dataframe(self, coluna):
        if isinstance(coluna, str):
            return self.dataframe.loc[:, coluna]
        elif isinstance(coluna, int):
            return self.dataframe.iloc[coluna]

    def ler_coluna(self, coluna, planilha=None):
        if not coluna:
            raise Exception("Coluna está vazia")
        if isinstance(self.dataframe, dict):
            return self._ler_dict_dataframe(coluna, planilha)
        elif isinstance(self.dataframe, pd.DataFrame):
            return self._ler_dataframe(coluna)
        else:
            raise Exception("Formato de dados não especificado")

    def ler_linha(self, linha):
        if not linha:
            raise Exception("Linha está vazia")
        if isinstance(self.dataframe, dict):
            ...
        elif isinstance(self.dataframe, pd.DataFrame):
            return self.dataframe.loc[linha]

    def ler_celulas(self, linha, coluna):
        if not coluna or not linha:
            raise Exception("Célula não especificada")
        if isinstance(self.dataframe, dict):
            ...
            #return self._ler_dict_dataframe(coluna, planilha)
        elif isinstance(self.dataframe, pd.DataFrame):
            return self.dataframe.loc[linha, coluna]
        else:
            raise Exception("Formato de dados não especificado")




