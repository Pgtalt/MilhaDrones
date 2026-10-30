import matplotlib.pyplot as plt
import pandas as pd

class GraficosExcel:
    def __init__(self, serie, coluna=None):
        self.__serie = serie
        self.__coluna = coluna

    def histograma(self, titulo="Histograma", titulo_x="Eixo X", titulo_y="Eixo Y"):
        if not isinstance(self.__serie, pd.Series):
            raise Exception("Erro")
        x = self.__serie
        # the histogram of the data
        n, bins, patches = plt.hist(x, 10, density=False, facecolor='red')

        plt.xlabel(titulo_x)
        plt.ylabel(titulo_y)
        plt.title(titulo)
        plt.axis((min(x), max(x), 0, max(n)+min(n)))
        return plt

    def velocidade_media(self, titulo="Velocidade Média", titulo_x="Eixo X", titulo_y="Eixo Y"):
        if not isinstance(self.__serie, pd.Series):
            raise Exception("Erro")

        x = self.__serie
        y = self.__coluna
        plt.plot(x, y)

        plt.xlabel(titulo_x)
        plt.ylabel(titulo_y)
        plt.title(titulo)
        #plt.axis((min(x), max(x), 0, max(n)+min(n)))
        return plt

    def grafico_barras(self, titulo="Velocidade Média", titulo_x="Eixo X", titulo_y="Eixo Y"):
        if not isinstance(self.__serie, (pd.Series, list) ) or not isinstance(self.__coluna, (pd.Series, list) ):
            raise Exception("Erro")
        x = self.__serie
        y = self.__coluna
        fig, ax = plt.subplots()
        plt.xlabel(titulo_x, size=12, color="gray")
        plt.ylabel(titulo_y, size=12, color="gray")
        plt.title(titulo)
        ax.bar(x, y, width=0.5, edgecolor="blue", linewidth=1, color="green")
        return plt

    def grafico_barras_agrupadas(self, titulo="Velocidade Média", titulo_x="Eixo X", titulo_y="Eixo Y"):

        species = ("Adelie", "Chinstrap", "Gentoo")
        penguin_means = {
            'Bill Depth': (18.35, 18.43, 14.98),
            'Bill Length': (38.79, 48.83, 47.50),
            'Flipper Length': (189.95, 195.82, 217.19),
        }

        fig, ax = plt.subplots(layout='constrained')

        res = ax.grouped_bar(penguin_means, tick_labels=species, group_spacing=1)
        for container in res.bar_containers:
            ax.bar_label(container, padding=3)

        # Add some text for labels, title, etc.
        ax.set_ylabel('Length (mm)')
        ax.set_title('Penguin attributes by species')
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, max(max(penguin_means.values())))

        return plt