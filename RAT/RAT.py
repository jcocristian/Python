from os import system
u = d = pc = c = str()
rat = ('psexec.exe', 'psservice.exe', 'pspasswd.exe', 'scanip.exe', 'shutdown -s -t', 'shutdown -r -t', 'shutdown -a -m')
txt = ('Remote Acess Tool v2.0', 'Editor de Senha', 'Serviços', 'POWER', 'CMD', 'Scan IP', 'By: Cristian Oliveira', 'Disco C')
while True:
    system(f'mode 70,22 & cls & color 1f & title {txt[0]}')
    print('{:-^70}\n{}\n'.format(f': {txt[0]} :', txt[6]))
    print('''AÇÃO REMOTA\n1: CMD\n2: Abrir C:\n3: Senha\n4: Serviços\n5: Power\n6: Sair''')
    op = input('>> ').strip().lower()
    if op == '1' or op == 'cmd': #Acessar CMD remoto.
        system(f'mode 100,22 & cls & color 0f & title {txt[0]} - {txt[4]}')
        op1 = input(f'CMD\nMétodo de Autenticação:\n1: Transparente.\n2: Personalizado.\n').strip().lower()
        if op1 == 'transparente' or op1 == '1': #Método Transparente.
            while op1 == 'transparente' or op1 == '1':
                pc = input('CMD\nInforme o nome da máquina: ')
                system(f'{rat[0]} \\\\{pc} -s cmd.exe')
                if (input('Deseja acessar outra máquina? (S/N): ').strip().lower())[0] == 'n':
                    op1 = ''
        elif op1 == 'personalizado' or op1 == '2':
            u = input('Usuário: ').strip().lower()
            d = input('Domínio: ').strip().lower()
            while op1 == 'personalizado' or op1 == '2':
                pc = input('CMD Remoto\nInforme o nome da máquina: ')
                system(f'{rat[0]} \\\\{pc} -u {d}\\{u} cmd.exe')
                if (input('Deseja acessar outra máquina? {S/N): ').strip().lower())[0] == 'n':
                    op1 = ''
    elif op == '2' or op == 'abrir c:' or op == 'c' or op == 'abrir c':
        while op == '2' or op == 'abrir c:' or op == 'c' or op == 'abrir c':
            system(f'mode 70,22 & cls & title {txt[0]} - {txt[8]}')
            pc = input(f'{txt[8]}\nInforme o nome da máquina: ')
            system(f'start \\\\{pc}\\c$')
            if (input('Deseja abrir o C de outra máquina? (S/N): ').strip().lower())[0] == 'n':
                op = ''
    elif op == '3' or op == 'alterar senha' or op == 'senha':
        system(f'mode 70,22 & cls & color cf & {txt[0]} - {txt[1]}')
        u = input(f'{txt[1]}\nSeu Usuário: ').strip().lower()
        d = input('Domínio: ').strip().lower()
        while op == '3' or op == 'alterar senha' or op == 'senha':
            pc = input('Informe o nome da máquina ou domínio atingido: ').strip().lower()
            ud = input('Usuário atingido: ').strip().lower()
            pd = input('Nova Senha: ').strip()
            system(f'{rat[2]} \\\\{pc} -u {d}\{u} {ud} {pd}')
            if (input('Deseja alterar outra senha? {S/N): ').lower().strip()):
                op = ''
    elif op == 'serviços' or op == 'servicos' or op == '4':
        system(f'mode 70,22 & title {txt[0]} - {txt[2]}')
        u = input(f'{txt[2]}\nUsuário: ').strip().lower()
        d = input('Domínio: ').strip().lower()
        while op == 'serviços' or op == 'servicos' or op == '4':
            pc = input('Informe o nome do computador: ').lower().strip()
            srv = input('Ação: stop/start/restart service_name\n>> ').strip().lower()
            system(f'{rat[1]} \\\\{pc} -u {d}\\{u} {srv}')
            if (input('Deseja continuar? (S/N): ').strip().lower())[0] == 'n':
                op = ''
    elif op == '5' or op == 'shutdown' or op == 'desligar':
        system(f'mode 70,22 & title {txt[0]} - {txt[4]}')
        while op == '5' or op == 'shutdown' or op == 'desligar':
            op2 = input(f'{txt[4]}\n1: Desligar\n2: Reiniciar\n3: Cancelar\n>> ').strip().lower()
            if op2 == 'desligar' or op2 == '1' or op2 == 'shutdown':
                pc = input('Informe o nome da máquina: ').strip().lower()
                t = int(input('Informe o tempo para ser desligada (em segundos): ').strip().lower())
                c = input('Informe uma mensagem a ser exibida na máquina destino:\n>> ').strip()
                if c == '':
                    system(f'{rat[4]} {t} -m \\\\{pc}')
                else:
                    system(f'{rat[4]} {t} -c \"{c}\" -m \\\\{pc}')
            elif op2 == 'reiniciar' or op2 == 'reboot' or op2 == '2':
                pc = input('Informe o nome da máquina: ').strip().lower()
                t = int(input('Informe o tempo para ser reiniciada (em segundos): ').strip().lower())
                c = input('Informe uma mensagem a ser exibida na máquina destino:\n>> ').strip().lower()
                if c == '':
                    system(f'{rat[5]} {t} -m \\\\{pc}')
                else:
                    system(f'{rat[5]} {t} -c \"{c}\" -m \\\\{pc}')
            elif op2 == '3' or op2 == 'cancelar':
                pc = input('Informe o nome da máquina: ').strip().lower()
                system(f'{rat[6]} \\\\{pc}')
            if (input('Deseja executar em outra máquina? (S/N): ').strip().lower())[0] == 'n':
                op = ''
    elif op == '6' or op == 'sair' or op == 'exit':
        break
    else:
        print('\n')
