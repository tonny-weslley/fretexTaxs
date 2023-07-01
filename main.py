import json
import os

from prettytable import PrettyTable

with open('data/profissionais.json') as f:
    profissionais = json.load(f)

with open('data/atividades.json') as f:
    atividades = json.load(f)
    
with open('data/taxas.json') as f:
    taxas = json.load(f)

tabela_de_atividades = PrettyTable()
tabela_de_atividades.field_names = ['Atividade', 'Horas', 'Profissionais', 'Valor'] 

def calculateHour(profissional):
    hora = profissionais[profissional]['hora']
    for taxa in taxas:
        hora = hora + hora * taxas[taxa]['valor']
    return round(hora, 2)    


def main():

    for atividade in atividades:
        prof = atividades[atividade]['profissionais']
        profissionais = ', '.join(prof)
        valor = 0
        for profi in prof:
            hora_profissiona = calculateHour(profi)
            valor = valor + hora_profissiona * atividades[atividade]['horas']
        tabela_de_atividades.add_row([atividade, atividades[atividade]['horas'], profissionais, round(valor, 2)])
    print(tabela_de_atividades)

main()


"""
1 - Listar todas as atividades
2 - Listar todos os profissionais de uma atividade
4 - Calcular a hora de um profissional
5 - Calcular o valor de uma atividade
6 - Adicionar a tabela
"""