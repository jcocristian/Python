from time import sleep
from os import system #Sistemas Microsoft Windows
from datetime import date
system('{}'.format('color 1f & mode 50,8 & title PyDateFixer v1.2')) #Definidor do console
while True: #Tratamento de erros do usuário.
    n = input('Informe data no seguinte formato D-M-AAAA:\nEx¹ 7-7-2020\nEx² 7-12-2020\nEx³ 21-11-2020\n:> '.strip())
    if len(n.split('-')) != 3: #Teste de validade.
        print('A data informada é inválida.')
    else: #Se a data informada for validade, ele entra nesse bloco para definição do "new" a ser usada no system()
        n = '-'.join([str(int(n.split('-')[0])), str(int(n.split('-')[1])), str(int(n.split('-')[2]))])
        tvd = int(input('Intervalo de tempo para o PyDateFixer verificar a data do sistema (em segundos): '))
        if tvd == 0: #Coleta do tempo a ser usado para verificar o data do sistema
            tvd = 3600
            print('Aplicamos o tempo padrão que é 3600 segundos.')
            sleep(3)
        break
v = r = int()
m = (f'Verificamos a data do seu Sistema uma\nvez a cada {tvd} segundos.', 'JonLei IT Solutions')
while True:
    d = date.today()
    d = '-'.join([str(int((str(d)).split('-')[2])), str(int((str(d)).split('-')[1])), str(int((str(d)).split('-')[0]))])
    if d != n: #Condição se Data Coletada for Diferente da data a ser fixada.
        system(f'cls {"&"} date {n}') #Aplicação da Data Definida.
        r += 1
        v += 1
        print('{}{:^50}{:^50}'.format(m[0], f'Data Fixada: {n}\nRedefinições: {r}\nVerificações: {v}\n\n', m[1]))
        sleep(tvd)
    else:
        system('cls')
        v += 1
        print('{}{:^50}{:^50}'.format(m[0], f'Data Fixada: {n}\nRedefinições: {r}\nVerificações: {v}\n\n', m[1]))
        sleep(tvd)
