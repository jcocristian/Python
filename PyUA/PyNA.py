from os import system
from tkinter import *

t = ('PyNetAdmin', 'PyCMD', 'PySRV', 'PyPassWD', 'Menu', 'Testando conexão..', 'Escolha um Programa do PyNA', 'Usuário', 'Senha', 'Hostname / IP', 'Autenticar', '{} Ativo', '{} está inacessível.\nVerifique sua conexão e tente novamente.', 'Conectar', '{} Inativo', 'Você saiu do {}.', 'Preencha usuário e senha.', 'Serviço', 'Start', 'Restart', 'Stop', 'Status')
clr = ('#003b8e', '#ffffff', '#268dbd', '#6fc4dd', '#54b17d', '#03fdfc')
system(f'color 1f & mode 80,20 & title {t[0]} Backend')


def tsping(host):
    def ping(h):
        x = system(f'ping -n {h}')
        return x

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


def CheckHost(host):
    if host == '':
        return False
    else:
        return True


def StrLow(text):
    x = str(text).strip().lower()
    return x


def StrUp(text):
    x = str(text).strip().upper()
    return x


def PyCMD():
    def pycmdtitle(tx1, tx2, tx3):
        m.title(f'{tx1} - {tx2} - {tx3}')

    def pycmdtext(txt):
        if '{}' in txt:
            mt5['text'] = txt.format(StrUp(s.get()))
        else:
            mt5['text'] = txt

    def pycmd_a():
        pycmdtext(t[5])
        if not tsping(StrUp(s.get())):
            pycmdtitle(t[0], t[1], t[14].format(StrUp(s.get())))
            pycmdtext(t[12])
        else:
            pycmdtitle(t[0], t[1], t[11].format(StrUp(s.get())))
            if not CheckAut():
                pycmdtext(t[16])
                pycmdtitle(t[0], t[1], t[14].format(StrUp(s.get())))
            else:
                x = f'{t[1]}.exe \\\\{StrLow(s.get())} -u {(StrLow(u.get()))} -p {(p.get()).strip()} cmd.exe'
                system(x)
                pycmdtitle(t[0], t[1], t[14].format(StrUp(s.get())))
                pycmdtext(t[15])

    def pycmd_t():
        pycmdtext(t[5])
        if not tsping(s.get()):
            pycmdtitle(t[0], t[1], t[14].format(StrUp(s.get())))
            pycmdtext(t[12])
        else:
            pycmdtitle(t[0], t[1], t[11].format(StrUp(s.get())))
            x = f'{t[1]}.exe \\\\{StrLow(s.get())} -s cmd.exe'
            system(x)
            pycmdtitle(t[0], t[1], t[14].format((s.get()).upper()))
            pycmdtext(t[15])

    m = Tk()
    m.title(f'{t[0]} - {t[1]}')
    m.geometry('450x200')
    m.configure(background=f'{clr[2]}')
    s = Entry(m, foreground=f'{clr[0]}', bd=2)
    u = Entry(m, foreground=f'{clr[0]}', bd=2)
    p = Entry(m, foreground=f'{clr[0]}', show='*', bd=2)
    mt1 = Label(m, text=f'{t[7]}', background=f'{clr[2]}', anchor=W)
    mt2 = Label(m, text=f'{t[8]}', background=f'{clr[2]}', anchor=W)
    mt3 = Label(m, text=f'{t[9]}', background=f'{clr[2]}', anchor=W)
    mt4 = Label(m, text=f'{t[0]}', background=f'{clr[2]}', anchor=N)
    mt5 = Label(m, text='', background=f'{clr[1]}', foreground=f'{clr[0]}', bd=3, anchor=W)
    mt1.place(x=10, y=5, width=100, height=20)
    u.place(x=10, y=30, width=120, height=20)
    mt2.place(x=10, y=55, width=120, height=20)
    p.place(x=10, y=80, width=120, height=20)
    mt3.place(x=10, y=105, width=120, height=20)
    s.place(x=10, y=130, width=120, height=20)
    mt4.place(x=150, y=5, width=230, height=30)
    mt5.place(x=150, y=30, width=230, height=120)
    mb1 = Button(m, text=f'{t[10]}', command=pycmd_a, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb2 = Button(m, text=f'{t[13]}', command=pycmd_t, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb1.place(x=10, y=160, width=120, height=30)
    mb2.place(x=150, y=160, width=120, height=30)
    m.mainloop()


def PySRV():
    def pysrvtext(txt):
        if '{}' in txt:
            mt5['text'] = txt.format((s.get()).upper())
        else:
            mt5['text'] = txt

    def pysrv(host, user, passwd, op, srv):
        if not CheckAut(user, passwd):
            pysrvtext(t[16])
        elif not CheckHost(host):
            pysrvtext(f'Informe o {t[9]}')
        elif not tsping(host):
            pysrvtext(f'{t[12]}')
        elif srv == '':
            pysrvtext('Informe o serviço destino')
        else:
            x = f'{t[2]}.exe \\\\{host} -u {user} -p {passwd} {op} {srv}'
            system(x)

    def pysrv_start():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), t[18].lower(), sv.get().strip())

    def pysrv_restart():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), t[19].lower(), sv.get().strip())

    def pysrv_stop():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), t[20].lower(), sv.get().strip())

    def pysrv_status():
        pysrv(StrLow(s.get()), StrLow(u.get()), p.get().strip(), t[21].lower(), sv.get().strip())


    m = Tk()
    m.title(f'{t[0]} - {t[2]}')
    m.geometry('530x210')
    m.configure(background=f'{clr[2]}')
    s = Entry(m, foreground=f'{clr[0]}', bd=2)
    u = Entry(m, foreground=f'{clr[0]}', bd=2)
    p = Entry(m, foreground=f'{clr[0]}', show='*', bd=2)
    sv = Entry(m, foreground=f'{clr[0]}', bd=2)
    mt1 = Label(m, text=f'{t[7]}', background=f'{clr[2]}', anchor=N)
    mt2 = Label(m, text=f'{t[8]}', background=f'{clr[2]}', anchor=N)
    mt3 = Label(m, text=f'{t[9]}', background=f'{clr[2]}', anchor=N)
    mt4 = Label(m, text=f'{t[0]}', background=f'{clr[2]}', anchor=W)
    mt5 = Label(m, text='', background=f'{clr[1]}', foreground=f'{clr[0]}', bd=3, anchor=W)
    mt6 = Label(m, text=f'{t[17]}', background=f'{clr[2]}', anchor=N)
    mt1.place(x=10, y=5, width=100, height=20)
    u.place(x=10, y=30, width=120, height=20)
    mt2.place(x=140, y=5, width=120, height=20)
    p.place(x=140, y=30, width=120, height=20)
    mt3.place(x=270, y=5, width=120, height=20)
    s.place(x=270, y=30, width=120, height=20)
    mt4.place(x=90, y=180, width=230, height=30)
    mt6.place(x=400, y=5, width=120, height=20)
    sv.place(x=400, y=30, width=120, height=20)
    mt5.place(x=10, y=60, width=230, height=120)
    mb1 = Button(m, text=f'{t[18]}', command=pysrv_start, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb2 = Button(m, text=f'{t[19]}', command=pysrv_restart, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb3 = Button(m, text=f'{t[20]}', command=pysrv_stop, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb4 = Button(m, text=f'{t[21]}', command=pysrv_status, foreground=f'{clr[0]}', bd=3, anchor=N)
    mb1.place(x=250, y=60, width=60, height=30)
    mb2.place(x=250, y=95, width=60, height=30)
    mb3.place(x=250, y=130, width=60, height=30)
    mb4.place(x=250, y=165, width=60, height=30)
    m.mainloop()


def PyNA_P():
    m = Tk()
    m.title(f'{t[0]} - {t[4]}')
    m.geometry('450x300')
    m.configure(background=f'{clr[2]}')
    mt1 = Label(m, text=f'{t[6]}', background=f'{clr[2]}', anchor=N)
    mb1 = Button(m, text=f'{t[1]}', command=PyCMD, bd=3, foreground=f'{clr[0]}', anchor=N)
    mb2 = Button(m, text=f'{t[2]}', command=PySRV, bd=3, foreground=f'{clr[0]}', anchor=N)
    mt1.place(x=130, y=10, width=190, height=30)
    mb1.place(x=10, y=40, width=100, height=30)
    mb2.place(x=120, y=40, width=100, height=30)
    m.mainloop()


PyNA_P()
