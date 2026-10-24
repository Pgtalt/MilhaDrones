from teste.TesteGraficoBarras import TesteGraficoBarras
from view.visualizador import Visualizador

def main():
    tipo = "Gráfico"
    visualizador = Visualizador()

    while True:
        try:
            decisao = int(input(f"1. {tipo} - Distribuição de Pesos das Encomendas\n"
                                f"2. {tipo} - Gerar Velocidade Média\n"
                                f"3. {tipo} - Comparação do consumo energético por modalidade de entrega\n"
                                f"4. {tipo} – Distribuição espacial dos armários e dos destinos associados\n"
                                f"0. Sair\n"
                                f"> "))
            if decisao == 1:
                visualizador.gerar_graficos_pesos()
            elif decisao == 2:
                visualizador.gerar_grafico_velocidade()
            elif decisao == 3:
                TesteGraficoBarras.exibir()
                #visualizador.gerar_grafico_consumo()
            elif decisao == 4:
                visualizador.gerar_grafico_distribuicao_espacial()
            elif decisao == 0:
                exit(0)
            else:
                raise Exception("Opção invalida do menu")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()