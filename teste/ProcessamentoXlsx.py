import pandas as pd

class ProcessamentoXlsx:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise Exception("Não é um Dataframe!")
        self.dataframe = dataframe
        print(self.dataframe)

    def ler_toda_planilha(self):
        return self.dataframe

    def ler_coluna(self, coluna):
        if isinstance(coluna, str): #Le a coluna por meio de uma String
            return self.dataframe[coluna]
        elif isinstance(coluna, int):
            return self.dataframe.iloc[:, coluna]
        elif isinstance(coluna, list):
            if all(isinstance(item, str) for item in coluna):
                return self.dataframe[coluna]
            elif all(isinstance(item, int) for item in coluna):
                return self.dataframe.iloc[:, coluna]
        raise Exception("Coluna em formato não especificado")

    def ler_linha(self, linha, coluna=None):
        if coluna is None:
            if isinstance(linha, str):  # Precisa de linha e da coluna a mirar
                # return self.dataframe.loc[ self.ler_coluna(coluna) == linha]
                return self.dataframe.loc[linha]
            elif isinstance(linha, int):  #
                return self.dataframe.iloc[linha]
            elif isinstance(linha, list):
                if all(isinstance(item, str) for item in linha):
                    # return self.dataframe.loc[ self.ler_coluna(coluna) == linha]
                    return self.dataframe.loc[linha]
                elif all(isinstance(item, int) for item in linha):
                    return self.dataframe.iloc[linha, :]
            raise Exception("Linha em formato não especificado")
        else:
            if isinstance(linha, str):
                return self.dataframe.loc[self.ler_coluna(coluna) == linha]
            elif all(isinstance(item, str) for item in linha):
                return self.dataframe.loc[ self.ler_coluna(coluna) == linha]
            raise Exception("Linha em formato não String")

    def ler_celula(self, linha, coluna, id_linha=None):
        linha_sel = self.ler_linha(linha, id_linha)
        coluna_sel = self.ler_coluna(coluna)
        nome_coluna = coluna_sel.name if hasattr(coluna_sel, 'name') else coluna_sel.columns
        return linha_sel[nome_coluna]
