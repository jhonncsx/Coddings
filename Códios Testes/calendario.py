

import calendar

print("===== CALENDÁRIO =====")

ano = 2026

try:
    mes = int(input('Digite o número do mês que deseja visualizar (1 a 12): '))

    if 1 <= mes <= 12:
        print('\n')
        calendario_mes = calendar.month(ano, mes)
        print(calendario_mes)
    else:
        print('Mês inválido! Por favor, escolha um número entre 1 e 12.')

except ValueError:
    print('Entrada inválida! Por favor, digite apenas números inteiros.')