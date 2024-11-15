import pandas as pd
import openpyxl

from Entity import Entity


def ler_planilha():
    df = pd.read_excel('igreja.xlsx')

    lista_de_objetos = [
        Entity(
            row['1'],
            row['2'],
            row['3'],
            row['4'],
            row['5'],
            row['6'],
            row['7'],
            row['8'],
            row['9']
        )
        for index, row in df.iterrows()
    ]

    print('LEITURA FINALIZADA')
    return lista_de_objetos
