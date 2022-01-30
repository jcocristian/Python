import datetime
from os import system
from tkinter import *
PyNA_t = ('PyNetAdmin', 'PyCMD', 'PySRV', 'PyPassWD', 'Menu', 'Testando conexão..', 'Escolha um Programa do PyNA', 'Usuário', 'Senha', 'Hostname / IP', 'Autenticar', '{} Ativo', '{} está inacessível.\nVerifique sua conexão e tente novamente.', 'Conectar', '{} Inativo', 'Você saiu do {}.', 'Preencha usuário e senha.', 'Serviço', 'Start', 'Restart', 'Stop', 'Status')
PyNA_c = ('#003b8e', '#ffffff', '#268dbd', '#6fc4dd', '#54b17d', '#03fdfc', '#fd9f02')
PyUA_t = ('PyUA', 'Backend', 'no', 'yes', 'Usuários: ', 'Ativar', 'Desativar', 'O(s) {} usuário(s) foram processados.', 'By Jonas Cristian Oliveira', 'Informe as contas de usuário, separado-os por vírgula.', 'Você precisa informar pelo menos 1 conta.', 'true', 'false', 'AD', 'MS365', 'Domínio de E-mail: @', 'Instalar AzureADPreview', '[ Caso NÃO tenha instalado o AzureAD ]', 'PyMS365_.txt', 'PS_365.ps1', 'sucesso', 'não foi encontrado', 'Você precisa informar um domínio de e-mail.', 'AzureAD', 'PyUserAdmin')
PyUA_c = ('#e8f7fe', '#191971', '#66aec7', '#fff', '#fe0000')
PySA_t = ('PySA', 'PySessionAdmin', 'query session /server:', 'rwinsta /server:', 'Usuários', 'Verificar', 'Sessões', 'X DROP X', 'Sessão de ID "{}" encerrada com sucesso.', 'Falha ao encerrar a sessão de ID "{}".', 'ID', 'Nenhuma sessão encontrada no {}.', 'Você precisa informar o "{}".', 'Você precisa informar pelo menos 1 "ID".', 'Processados com sucesso: {}', 'Processados com falha: {}', 'Informe os IDs', 'TOTAL')
ErrorT = ('Error', 'PySA_IDDrop()')


def PyNA_Backend():
    system(f'color 1f & mode 80,20 & title {PyNA_t[0]} Backend')


def PyDTtm(Op):
    def Today():
        return datetime.date.today()

    def Time():
        return datetime.datetime.now()

    if Op == 'YMD':
        return f'{Today().year}-{Today().month:0>2}-{Today().day:0>2}'
    elif Op == 'Y':
        return f'{Today().year}'
    elif Op == 'M':
        return f'{Today().month:0>2}'
    elif Op == 'D':
        return f'{Today().day:0>2}'
    elif Op == 'hms':
        return f'{Time().hour:0>2}:{Time().minute:0>2}:{Time().second:0>2}'
    elif Op == 'hmsms':
        return f'{Time().hour:0>2}:{Time().minute:0>2}:{Time().second:0>2}:{Time().microsecond:0>6}'
    elif Op == 'h':
        return f'{Time().hour:0>2}'
    elif Op == 'm':
        return f'{Time().minute:0>2}'
    elif Op == 's':
        return f'{Time().second:0>2}'
    elif Op == 'ms':
        return f'{Time().microsecond:0>6}'
    elif Op == 'YMDhms':
        return f'{Today().year}-{Today().month:0>2}-{Today().day:0>2}:{Time().hour:0>2}:{Time().minute:0>2}:{Time().second:0>2}'
    elif Op == 'YMDhmsms':
        return f'{Today().year}-{Today().month:0>2}-{Today().day:0>2}:{Time().hour:0>2}:{Time().minute:0>2}:{Time().second:0>2}:{Time().microsecond:0>6}'
    elif Op == 'Today':
        return Today()
    elif Op == 'TmNow':
        return Time()
    else:
        return SyntaxError


def tsping(host):
    def ping(h):
        return system(f'ping -n 1 {h}')

    if ping(host) == 0:
        return True
    else:
        if ping(host) == 0:
            return True
        else:
            if ping(host) == 0:
                return True
            else:
                if ping(host) == 0:
                    return True
                else:
                    return False


def CheckAut(user, passwd):
    if user == '' or passwd == '':
        return False
    else:
        return True


def Writer(Name, text):
    open(f'{Name}', 'a').write(f'{text}')


def Reader(Name):
    try:
        return open(f'{Name}', 'r', encoding='utf-8').read()
    except FileNotFoundError:
        return FileNotFoundError


def SysSTR(Commander):
    temp = f'{"".join((PyDTtm("YMDhmsms").split(":")))}'
    c = system(f'{Commander}>>SysSTR{temp}.temp & attrib +h SysSTR{temp}.temp')
    if c == 0:
        x = Reader(f'SysSTR{temp}.temp')
        system(f'del /a /q /f SysSTR{temp}.temp')
        return x
    else:
        system(f'del /a /q /f SysSTR{temp}.temp')
        return c


def StrSplV(txt):
    x = str(txt).split(',')
    LL = []
    for i in range(0, len(x)):
        LL.append(x[i].strip())
    return LL


def CheckInput(Entrada):
    if Entrada == '':
        return False
    else:
        return True


def StrLow(text):
    return str(text).strip().lower()


def StrUp(text):
    return str(text).strip().upper()


def PyCMD():
    def pycmdtitle(tx1, tx2):
        m.title(f'{tx1} - {tx2}')

    def pycmdtext(txt):
        if '{}' in txt:
            mt1['text'] = txt.format(StrUp(s.get()))
        else:
            mt1['text'] = txt

    def pycmd_a():
        pycmdtext(PyNA_t[5])
        if not CheckInput(s.get()):
            pycmdtext(f'Informe o {PyNA_t[9]}')
        elif not tsping(StrUp(s.get())):
            pycmdtitle(PyNA_t[1], PyNA_t[14].format(StrUp(s.get())))
            pycmdtext(PyNA_t[12])
        else:
            pycmdtitle(PyNA_t[1], PyNA_t[11].format(StrUp(s.get())))
            if not CheckAut(u.get(), p.get()):
                pycmdtext(PyNA_t[16])
                pycmdtitle(PyNA_t[1], PyNA_t[14].format(StrUp(s.get())))
            else:
                system(f'{PyNA_t[1]}.exe \\\\{StrLow(s.get())} -u {(StrLow(u.get()))} -p {(p.get()).strip()} cmd.exe')
                PyNA_Backend()
                pycmdtitle(PyNA_t[1], PyNA_t[14].format(StrUp(s.get())))
                pycmdtext(PyNA_t[15])

    def pycmd_t():
        pycmdtext(PyNA_t[5])
        if not CheckInput(s.get()):
            pycmdtext(f'Informe o {PyNA_t[9]}')
        else:
            if not tsping(s.get()):
                pycmdtitle(PyNA_t[1], PyNA_t[14].format(StrUp(s.get())))
                pycmdtext(PyNA_t[12])
            else:
                pycmdtitle(PyNA_t[1], PyNA_t[11].format(StrUp(s.get())))
                system(f'{PyNA_t[1]}.exe \\\\{StrLow(s.get())} -s cmd.exe')
                PyNA_Backend()
                pycmdtitle(PyNA_t[1], PyNA_t[14].format((s.get()).upper()))
                pycmdtext(PyNA_t[15])

    m = Tk()
    m.title(PyNA_t[1])
    m.geometry('390x200')
    m.configure(background=PyNA_c[2])
    u = Entry(m, foreground=PyNA_c[0], bd=2)
    p = Entry(m, foreground=PyNA_c[0], show='*', bd=2)
    s = Entry(m, foreground=PyNA_c[0], bd=2)
    mt1 = Label(m, text='', background=PyNA_c[1], foreground=PyNA_c[0], bd=3, anchor=W)
    Label(m, text=PyNA_t[7], background=PyNA_c[2], anchor=W).place(x=10, y=5, width=100, height=20)
    u.place(x=10, y=30, width=120, height=20)
    Label(m, text=PyNA_t[8], background=PyNA_c[2], anchor=W).place(x=10, y=55, width=120, height=20)
    p.place(x=10, y=80, width=120, height=20)
    Label(m, text=PyNA_t[9], background=PyNA_c[2], anchor=W).place(x=10, y=105, width=120, height=20)
    s.place(x=10, y=130, width=120, height=20)
    mt1.place(x=150, y=30, width=230, height=120)
    Button(m, text=PyNA_t[10], command=pycmd_a, foreground=PyNA_c[0], bd=3, anchor=N).place(x=10, y=160, width=120, height=30)
    Button(m, text=PyNA_t[13], command=pycmd_t, foreground=PyNA_c[0], bd=3, anchor=N).place(x=150, y=160, width=120, height=30)
    Label(m, text=PyUA_t[8], background=PyNA_c[1], anchor=N).place(x=190, y=130, width=150, height=20)
    m.resizable(width=False, height=False)
    m.mainloop()


def PySRV():
    def pysrvtext(txt):
        if '{}' in txt:
            mt1['text'] = txt.format((s.get()).upper())
        else:
            mt1['text'] = txt

    def pysrv(host, user, passwd, op, srv):
        if not CheckAut(user, passwd):
            pysrvtext(PyNA_t[16])
        else:
            if not CheckInput(host):
                pysrvtext(f'Informe o {PyNA_t[9]}')
            else:
                if not tsping(host):
                    pysrvtext(PyNA_t[12])
                else:
                    if srv == '':
                        pysrvtext('Informe o serviço destino.')
                    else:
                        system(f'{PyNA_t[2]}.exe \\\\{host} -u {user} -p {passwd} {op} {srv}')

    def pysrv_start():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), PyNA_t[18].lower(), sv.get().strip())

    def pysrv_restart():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), PyNA_t[19].lower(), sv.get().strip())

    def pysrv_stop():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), PyNA_t[20].lower(), sv.get().strip())

    def pysrv_status():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), PyNA_t[21].lower(), sv.get().strip())

    m = Tk()
    m.title(PyNA_t[2])
    m.geometry('460x190')
    m.configure(background=PyNA_c[6])
    u = Entry(m, foreground=PyNA_c[0], bd=2)
    p = Entry(m, foreground=PyNA_c[0], show='*', bd=2)
    s = Entry(m, foreground=PyNA_c[0], bd=2)
    sv = Entry(m, foreground=PyNA_c[0], bd=2)
    mt1 = Label(m, text='', background=PyNA_c[1], foreground=PyNA_c[0], bd=3, anchor=W)
    Label(m, text=PyNA_t[7], background=PyNA_c[6], anchor=N).place(x=10, y=5, width=120, height=20)
    u.place(x=10, y=25, width=120, height=20)
    Label(m, text=PyNA_t[8], background=PyNA_c[6], anchor=N).place(x=10, y=50, width=120, height=20)
    p.place(x=10, y=70, width=120, height=20)
    Label(m, text=PyNA_t[9], background=PyNA_c[6], anchor=N).place(x=10, y=95, width=120, height=20)
    s.place(x=10, y=115, width=120, height=20)
    Label(m, text=PyUA_t[8], background=PyNA_c[1], anchor=W).place(x=200, y=120, width=150, height=20)
    Label(m, text=PyNA_t[17], background=PyNA_c[6], anchor=N).place(x=10, y=140, width=120, height=20)
    sv.place(x=10, y=155, width=120, height=20)
    mt1.place(x=150, y=25, width=230, height=120)
    Button(m, text=PyNA_t[18], command=pysrv_start, foreground=PyNA_c[0], bd=3, anchor=N).place(x=390, y=25, width=60, height=30)
    Button(m, text=PyNA_t[19], command=pysrv_restart, foreground=PyNA_c[0], bd=3, anchor=N).place(x=390, y=60, width=60, height=30)
    Button(m, text=PyNA_t[20], command=pysrv_stop, foreground=PyNA_c[0], bd=3, anchor=N).place(x=390, y=95, width=60, height=30)
    Button(m, text=PyNA_t[21], command=pysrv_status, foreground=PyNA_c[0], bd=3, anchor=N).place(x=390, y=130, width=60, height=30)
    m.resizable(width=False, height=False)
    m.mainloop()


def PyUA():
    def Backend():
        system(f'mode 50,14 & color 1f & title {PyUA_t[0]} - {PyUA_t[1]}')

    def TelaBackend(text):
        system(f'echo {text}')

    def TelaFrontEnd(text):
        mt1['text'] = f'{text}'

    def Split_U():
        return StrSplV(u.get())

    def PyUACheck_U():
        if Split_U()[0] == '' and len(Split_U()) == 1:
            return False
        else:
            return True

    def PS_AD(user, op):
        return system(f'powershell.exe dsquery user domainroot -samid "{user}" | dsmod user -disabled {op}')

    def ActionAD(op):
        Backend()
        for i in range(0, len(Split_U())):
            if PS_AD(Split_U()[i], op) == 0:
                rel = (f'{PyUA_t[20].capitalize()} - {Split_U()[i]}')
                TelaBackend(rel)
            else:
                rel = (f'Falha - {Split_U()[i]}')
                TelaBackend(rel)
            Writer(f'{PyUA_t[24]}LOG-{PyDTtm("YMD")}.txt', f'{PyDTtm("YMDhms")} - {rel}\n')

    def PS_365(op):
        try:
            open(f'{PyUA_t[18]}', 'r')
            Writer(f'{PyUA_t[19]}', f'Connect-{PyUA_t[23]}\nGet-Content "{PyUA_t[18]}" | ForEach {"{"}Set-{PyUA_t[23]}User -ObjectID $_ -AccountEnabled ${op}{"}"}\n')
            system(f'attrib + h {PyUA_t[19]} & powershell.exe .\\{PyUA_t[19]} & del /a /q /f {PyUA_t[19]}')
        except FileNotFoundError:
            TelaFrontEnd(f'{PyUA_t[18]} {PyUA_t[21]}.')
            TelaBackend(f'{PyUA_t[18]} {PyUA_t[21]}.')

    def EAccount_AD():
        if not PyUACheck_U():
            TelaFrontEnd(PyUA_t[10])
        else:
            ActionAD(PyUA_t[2])
            TelaFrontEnd(PyUA_t[7].format(len(Split_U())))

    def DAccount_AD():
        if not PyUACheck_U():
            TelaFrontEnd(PyUA_t[10])
        else:
            ActionAD(PyUA_t[3])
            TelaFrontEnd(PyUA_t[7].format(len(Split_U())))

    def Enable365():
        if not PyUACheck_U():
            TelaFrontEnd(PyUA_t[10])
        else:
            PS_365(PyUA_t[11])
            TelaFrontEnd(PyUA_t[7].format(len(Split_U())))

    def Disable365():
        if not PyUACheck_U():
            TelaFrontEnd(PyUA_t[10])
        else:
            PS_365(PyUA_t[12])
            TelaFrontEnd(PyUA_t[7].format(len(Split_U())))

    def MS365_Archive():
        if not PyUACheck_U():
            TelaFrontEnd(PyUA_t[10])
        elif StrLow(d.get()) == '':
            TelaFrontEnd(PyUA_t[22])
        else:
            for i in range(0, len(Split_U())):
                Writer(PyUA_t[18], f'{Split_U()[i].strip()}@{StrLow(d.get())}')
            TelaFrontEnd(f'{PyUA_t[18]} criado com {PyUA_t[20]}.')

    def MS365_DArchive():
        try:
            open(PyUA_t[18], 'r')
            system(f'del /a /q /f {PyUA_t[18]}')
            TelaFrontEnd(f'{PyUA_t[18]} deletado com {PyUA_t[20]}.')
        except FileNotFoundError:
            TelaFrontEnd(f'{PyUA_t[18]} {PyUA_t[21]}.')

    def InstallAzureADPreview():
        system(f'mode 100,16 & powershell.exe Install-module {PyUA_t[23]}Preview')
        Backend()

    Backend()
    m = Tk()
    m.title(PyUA_t[0])
    m.configure(background=PyUA_c[0])
    m.geometry('400x380')
    u = Entry(m, bd=3, foreground=PyUA_c[1])
    d = Entry(m, bd=3, foreground=PyUA_c[1])
    Label(m,  text=PyUA_t[24], background=PyUA_c[0], foreground=PyUA_c[1], anchor=N).place(x=0, y=0, width=400, height=20)
    Label(m,  text=PyUA_t[4], background=PyUA_c[0], foreground=PyUA_c[1], anchor=W).place(x=0, y=30, width=400, height=20)
    u.place(x=5, y=60, width=390, height=25)
    Button(m, text=f'{PyUA_t[5]} {PyUA_t[13]}', command=EAccount_AD, background=PyUA_c[2], bd=3, anchor=N).place(x=5, y=90, width=100, height=30)
    Button(m, text=f'{PyUA_t[6]} {PyUA_t[13]}', command=DAccount_AD, background=PyUA_c[2], bd=3, anchor=N).place(x=125, y=90, width=100, height=30)
    Label(m,  text=PyUA_t[15], background=PyUA_c[0], foreground=PyUA_c[1], anchor=W).place(x=0, y=145, width=120, height=20)
    d.place(x=120, y=140, width=275, height=25)
    Button(m, text=f'{PyUA_t[5]} {PyUA_t[14]}', command=Enable365, background=PyUA_c[2], bd=3, anchor=N).place(x=5, y=180, width=100, height=30)
    Button(m, text=f'{PyUA_t[6]} {PyUA_t[14]}', command=Disable365, background=PyUA_c[2], bd=3, anchor=N).place(x=125, y=180, width=100, height=30)
    Button(m, text=f'Novo {PyUA_t[18]}', command=MS365_Archive, background=PyUA_c[4], bd=3, anchor=N).place(x=235, y=180, width=160, height=30)
    Button(m, text=f'Apagar {PyUA_t[18]}', command=MS365_DArchive, background=PyUA_c[4], bd=3, anchor=N).place(x=235, y=215, width=160, height=30)
    Button(m, text=PyUA_t[16], command=InstallAzureADPreview, background=PyUA_c[4], bd=3, anchor=N).place(x=35, y=245, width=160, height=30)
    Label(m,  text=PyUA_t[17], background=PyUA_c[0], foreground=PyUA_c[4], anchor=W).place(x=5, y=220, width=220, height=20)
    mt1 = Label(m, text=PyUA_t[9], background=PyUA_c[1], foreground=PyUA_c[3], bd=5, anchor=N)
    mt1.place(x=5, y=290, width=390, height=50)
    Label(m, text=PyUA_t[8], background=PyUA_c[1], foreground=PyUA_c[3], bd=5, anchor=N).place(x=5, y=340, width=390, height=30)
    m.resizable(width=False, height=False)
    m.mainloop()


def PySA():
    def PySAtext(text):
        mt1['text'] = text

    def PySATextClean():
        mt1['text'] = ''
        mt2['text'] = ''
        mt3['text'] = ''
        mt4['text'] = ''


    def PySA_IDDrop():
        PySATextClean()
        x = str(Eid.get()).split(',')
        if not CheckInput(s.get()):
            PySAtext(PySA_t[12].format(PyNA_t[9]))
        else:
            if x[0] == '':
                PySAtext(PySA_t[13])
            else:
                if not tsping(StrLow(s.get())):
                    PySAtext(f'{PyNA_t[12].format(StrUp(s.get()))}')
                else:
                    idP = str()
                    idST = str()
                    idS = int()
                    idF = int()
                    for i in range(0, len(x)):
                        c = system(f'{PySA_t[3]}{StrLow(s.get())} {x[i]}')
                        if c == 0:
                            idS += 1
                            idP += f'{x[i]:<4}\n'
                            idST += 'Ok\n'
                        else:
                            idF += 1
                            idP += f'{x[i]:<4}\n'
                            idST += 'X\n'
                    if idS != 0 and idF != 0:
                        PySAtext(f'{PySA_t[14].format(idS)}\n{PySA_t[15].format(idF)}')
                        mt2['text'] = idST
                        mt3['text'] = idP
                    elif idS != 0 and idF == 0:
                        PySAtext(f'{PySA_t[14].format(idS)}')
                        mt2['text'] = idST
                        mt3['text'] = idP
                    elif idS == 0 and idF != 0:
                        PySAtext(f'{PySA_t[15].format(idF)}')
                        mt2['text'] = idST
                        mt3['text'] = idP
                    else:
                        return f'{ErrorT[0]}{ErrorT[1]}: 4º "IF" chegou no "Else".'

    def PySA_Query():
        PySATextClean()
        if not CheckInput(s.get()):
            PySAtext(PySA_t[12].format(PyNA_t[9]))
        else:
            if not tsping(StrLow(s.get())):
                PySAtext(f'{PyNA_t[12].format(StrUp(s.get()))}')
            else:
                sessions = SysSTR(f'{PySA_t[2]}{StrLow(s.get())}').split('\n')
                l1 = []
                for il1 in range(3, len(sessions) - 2):
                    l1.append(sessions[il1].strip())
                l2 = []
                for il2 in range(0, len(l1)):
                    if len(l1[il2]) < 50:
                        l2.append(l1[il2][0:22].strip())
                        l2.append(l1[il2][22:28].strip())
                    if len(l1[il2]) > 50:
                        l2.append(l1[il2][17:41].strip())
                        l2.append(l1[il2][39:47].strip())
                users = str()
                ids = str()
                t = int()
                for il4 in range(0, len(l2)):
                    if il4 % 2 == 0:
                        users += f'{l2[il4]}\n'
                    else:
                        t += 1
                        ids += f'{l2[il4]:<4}\n'
                if users != '' and ids != '':
                    mt2['text'] = users.upper()
                    mt3['text'] = ids
                    mt4['text'] = t
                else:
                    PySAtext(PySA_t[11].format(StrUp(s.get())))


    mPySA = Tk()
    mPySA.title(PySA_t[0])
    mPySA.geometry('380x570')
    mPySA.configure(background=PyUA_c[1])
    Label(mPySA, text=PyNA_t[9], background=PyUA_c[1], foreground=PyUA_c[3], anchor=W).place(x=10, y=5, width=120, height=20)
    Button(mPySA, text=f'{PySA_t[5]} {PySA_t[6]}', command=PySA_Query,  foreground=PyNA_c[0], anchor=N).place(x=200, y=20, width=120, height=30)
    mt1 = Label(mPySA, text='', background=PyNA_c[6], anchor=N)
    mt2 = Label(mPySA, text='', background=PyNA_c[1], anchor=N)
    mt3 = Label(mPySA, text='', background=PyNA_c[1], anchor=N)
    mt4 = Label(mPySA, text='', background=PyNA_c[1], anchor=N)
    s = Entry(mPySA, foreground=PyNA_c[0], bd=2)
    Eid = Entry(mPySA, foreground=PyNA_c[0], bd=2)
    s.place(x=10, y=30, width=180, height=20)
    Eid.place(x=250, y=130, width=120, height=20)
    Label(mPySA, text=f'{PySA_t[4]}', background=PyUA_c[1], foreground=PyUA_c[3], bd=3, anchor=W).place(x=60, y=60, width=100, height=20)
    Label(mPySA, text=f'{PySA_t[10]}', background=PyUA_c[1], foreground=PyUA_c[3], bd=3, anchor=W).place(x=195, y=60, width=50, height=20)
    Label(mPySA, text=PySA_t[16], background=PyUA_c[1], foreground=PyUA_c[3], bd=3, anchor=W).place(x=270, y=110, width=100, height=20)
    Label(mPySA, text=PySA_t[17], background=PyUA_c[1], foreground=PyUA_c[3], bd=3, anchor=N).place(x=250, y=60, width=50, height=20)
    mt1.place(x=10, y=500, width=360, height=60)
    mt2.place(x=10, y=80, width=150, height=400)
    mt3.place(x=180, y=80, width=50, height=400)
    mt4.place(x=250, y=80, width=50, height=20)
    Button(mPySA, text=PySA_t[7], command=PySA_IDDrop, background=PyUA_c[4], anchor=N).place(x=260, y=160, width=100, height=30)
    Label(mPySA, text=PyUA_t[8], background=PyNA_c[6], bd=5, anchor=N).place(x=120, y=535, width=150, height=20)
    mPySA.resizable(width=False, height=False)
    mPySA.mainloop()


def PyNA():
    m = Tk()
    m.title(f'{PyNA_t[0]} - {PyNA_t[4]}')
    m.geometry('450x300')
    m.configure(background=PyNA_c[2])
    Label(m, text=PyNA_t[6], background=PyNA_c[2], anchor=N).place(x=130, y=10, width=190, height=30)
    Button(m, text=PyNA_t[1], command=PyCMD, bd=3, foreground=PyNA_c[0], anchor=N).place(x=10, y=40, width=100, height=30)
    Button(m, text=PyNA_t[2], command=PySRV, bd=3, foreground=PyNA_c[0], anchor=N).place(x=120, y=40, width=100, height=30)
    Button(m, text='PyUA', command=PyUA, bd=3, foreground=PyNA_c[0], anchor=N).place(x=10, y=80, width=100, height=30)
    Button(m, text='PySA', command=PySA, bd=3, foreground=PyNA_c[0], anchor=N).place(x=120, y=80, width=100, height=30)
    m.resizable(width=False, height=False)
    m.mainloop()

PyNA()
