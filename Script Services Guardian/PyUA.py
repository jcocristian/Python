# Bibliotecas Importadas

import datetime
from tkinter import *
from os import system

# Constantes - Tubla 't' com vários textos que são utilizados pelos programas e tubla 'c' com definições de cores.

t = ('PyUA', 'Backend', 'no', 'yes', 'Usuários: ', 'Ativar', 'Desativar', 'O(s) {} usuário(s) foram processados.', 'By Jonas Cristian Oliveira', 'Informe as contas de usuário, separado-os por vírgula.', 'Você precisa informar pelo menos 1 conta.', 'true', 'false', 'AD', 'MS365', 'Domínio de E-mail: @', 'Instalar AzureADPreview', '[ Caso NÃO tenha instalado o AzureAD ]', 'PyMS365_.txt', 'PS_365.ps1', 'sucesso', 'não foi encontrado', 'Você precisa informar um domínio de e-mail.', 'AzureAD', 'PyUserAdmin')
cl = ('#e8f7fe', '#191971', '#66aec7', '#fff', '#fe0000')


# Programas Auxiliares - Criei esses programas para me auxiliar na execução de processos repetitivos ou reduzir código.

def Backend():  # Definição Padrão do Backend.
    system(f'mode 50,14 & color 1f & title {t[0]} - {t[1]}')


def TelaBackend(text):  # Este programa escreve na tela Backend.
    system(f'echo {text}')


def TelaFrontEnd(text):  # Este programa escreve na tela do Frotend.
    mt1['text'] = f'{text}'


def DT_HJ():  # Retorna o objeto 'date.today()'.
    return datetime.date.today()


def TM_HJ():  # Retorna o objeto 'time'.
    return datetime.time


def DT_YMD():  # Retorna a string de data no formato 'YYYY-MM-DD'.
    return f'{DT_HJ().year}-{DT_HJ().month}-{DT_HJ().day}'


def TM_HMS():  # Retorna a string de hora no formato 'HH-MM-SS'.
    return f'{TM_HJ().hour}-{TM_HJ().minute}-{TM_HJ().second}'


def DT_YMD_HMS():  # Retorna a string de Data e Hora no formato 'YYYY-MM-DD-HH-MM-SS'.
    return f'{DT_YMD()}-{TM_HMS()}'


def StrLow(text):  # Recebe uma string, e retorna ela sem espaços no começo e no fim, e minúsculo.
    return str(text).strip().lower()


def Split_U():  # Ler a string do campo 'Usuários', separa a string por víngula, e retorna uma lista com os valores.
    return (u.get()).split(',')


def Writer(Name, text):  # Recebe o nome do arquivo e o texto a ser escrito nele, e cria o arquivo (caso não exista), se o arquivo já existir, ele adiciona o texto.
    open(f'{Name}', 'a').write(f'{text}')


def Check_U():  # Faz um teste com Split(), pra validar se foi informado algum usuário no campo 'Usuários': SE SIM returna 'True', SE NÃO retorna 'False'.
    if Split_U()[0] == '' and len(Split_U()) == 1:
        return False
    else:
        return True


# Programas Secundários - Criei esses programas para serem atuadores para os Programas Principais.

def PS_AD(user, op):  # Recebe o usuário e o parâmetro para o Powershell, executa o comando no Backend, e retorna '0' se executado sem erro.
    return system(f'powershell.exe dsquery user domainroot -samid "{user}" | dsmod user -disabled {op}')


def ActionAD(op):  # Recebe o parâmetro para o Powershell, chama o 'PS_AD()' passando o parâmetro, Faz um laço 'FOR', onde nas iterações faz um teste lógico com o retorno do 'PS_AD', e grava o Log.
    Backend()
    for i in range(0, len(Split_U())):
        if PS_AD(Split_U()[i].strip(), op) == 0:
            rel = (f'{t[20].capitalize()} - {Split_U()[i].strip()[i]}')
            TelaBackend(rel)
        else:
            rel = (f'Falha - {Split_U()[i].strip()[i]}')
            TelaBackend(rel)
        Writer(f'{t[24]}LOG-{DT_YMD()}.txt', f'{DT_YMD_HMS()} - {rel}\n')


def PS_365(op):  # Recebe o parâmetro para o Powershell, então verifica se o arquivo 'PyMS365_.txt' existe: SE existir, ele grava o script 'PS_365.ps1' temporário com o parâmetro recebido, chama o 'PS_365.ps1' no powershell, e após concluir, deleta o 'PS_365.ps1'; SE NÃO existir, ele printa nas telas que o arquivo 'PyMS365_.txt' não foi encontrado.
    try:
        open(f'{t[18]}', 'r')
        Writer(f'{t[19]}', f'Connect-{t[23]}\nGet-Content "{t[18]}" | ForEach {"{"}Set-{t[23]}User -ObjectID $_ -AccountEnabled ${op}{"}"}\n')
        system(f'attrib + h {t[19]} & powershell.exe .\\{t[19]} & del /a /q /f {t[19]}')
    except FileNotFoundError:
        TelaFrontEnd(f'{t[18]} {t[21]}.')
        TelaBackend(f'{t[18]} {t[21]}.')


# Programas Primários - São todos os programas chamados diretamente pelo Interface de Usuário.

def EAccount_AD():  # SE 'Check_U()' for 'Falso' ele exibe nas telas a mensagem que precisa ser informado pelo menos 1 conta; SE for 'True', ele faz um laço 'FOR' chamado o 'ActionAD()', passando UM-a-UM os usuários do 'Split_U()' e também o Parâmetro 'no'.
    if not Check_U():
        TelaFrontEnd(t[10])
    else:
        ActionAD(t[2])
        TelaFrontEnd(t[7].format(len(Split_U())))


def DAccount_AD():  # SE 'Check_U()' for 'Falso' ele exibe nas telas a mensagem que precisa ser informado pelo menos 1 conta; SE for 'True', ele faz um laço 'FOR' chamado o 'ActionAD()', passando UM-a-UM os usuários do 'Split_U()' e também o Parâmetro 'no'.
    if not Check_U():
        TelaFrontEnd(t[10])
    else:
        ActionAD(t[3])
        TelaFrontEnd(t[7].format(len(Split_U())))


def Enable365():
    if not Check_U():
        TelaFrontEnd(t[10])
    else:
        PS_365(t[11])
        TelaFrontEnd(t[7].format(len(Split_U())))


def Disable365():
    if not Check_U():
        TelaFrontEnd(t[10])
    else:
        PS_365(t[12])
        TelaFrontEnd(t[7].format(len(Split_U())))


def MS365_Archive():
    if not Check_U():
        TelaFrontEnd(t[10])
    elif StrLow(d.get()) == '':
        TelaFrontEnd(t[22])
    else:
        for i in range(0, len(Split_U())):
            Writer(f'{t[18]}', f'{Split_U()[i].strip()}@{StrLow(d.get())}')
        TelaFrontEnd(f'{t[18]} criado com {t[20]}.')


def MS365_DArchive():
    try:
        open(f'{t[18]}', 'r')
        system(f'del /a /q /f {t[18]}')
        TelaFrontEnd(f'{t[18]} deletado com {t[20]}.')
    except FileNotFoundError:
        TelaFrontEnd(f'{t[18]} {t[21]}.')


def InstallAzureADPreview():
    system(f'mode 100,16 & powershell.exe Install-module {t[23]}Preview')
    Backend()


# Execução Backend - Definição padrão da tela do Backend.

Backend()

# Programa Frontend - Parametrização do Frontend.

m = Tk()
m.title(t[0])
m.configure(background=cl[0])
m.geometry('400x380')
u = Entry(m, bd=3, foreground=cl[1])
d = Entry(m, bd=3, foreground=cl[1])
Label(m,  text=t[24], background=cl[0], foreground=cl[1], anchor=N).place(x=0, y=0, width=400, height=20)
Label(m,  text=t[4], background=cl[0], foreground=cl[1], anchor=W).place(x=0, y=30, width=400, height=20)
u.place(x=5, y=60, width=390, height=25)
Button(m, text=f'{t[5]} {t[13]}', command=EAccount_AD, background=cl[2], bd=3, anchor=N).place(x=5, y=90, width=100, height=30)
Button(m, text=f'{t[6]} {t[13]}', command=DAccount_AD, background=cl[2], bd=3, anchor=N).place(x=125, y=90, width=100, height=30)
Label(m,  text=t[15], background=cl[0], foreground=cl[1], anchor=W).place(x=0, y=145, width=120, height=20)
d.place(x=120, y=140, width=275, height=25)
Button(m, text=f'{t[5]} {t[14]}', command=Enable365, background=cl[2], bd=3, anchor=N).place(x=5, y=180, width=100, height=30)
Button(m, text=f'{t[6]} {t[14]}', command=Disable365, background=cl[2], bd=3, anchor=N).place(x=125, y=180, width=100, height=30)
Button(m, text=f'Novo {t[18]}', command=MS365_Archive, background=cl[4], bd=3, anchor=N).place(x=235, y=180, width=160, height=30)
Button(m, text=f'Apagar {t[18]}', command=MS365_DArchive, background=cl[4], bd=3, anchor=N).place(x=235, y=215, width=160, height=30)
Button(m, text=t[16], command=InstallAzureADPreview, background=cl[4], bd=3, anchor=N).place(x=35, y=245, width=160, height=30)
Label(m,  text=t[17], background=cl[0], foreground=cl[4], anchor=W).place(x=5, y=220, width=220, height=20)
mt1 = Label(m, text=t[9], background=cl[1], foreground=cl[3], bd=5, anchor=N)
mt1.place(x=5, y=290, width=390, height=50)
Label(m, text=t[8], background=cl[1], foreground=cl[3], bd=5, anchor=N).place(x=5, y=340, width=390, height=30)
m.mainloop()
