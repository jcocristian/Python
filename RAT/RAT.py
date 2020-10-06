from os import system
while True:
    system('mode 50,22 & cls & color 1f & title Remote Access Tool v1.5')
    print('{:-^50}'.format(': Remote Access Tool v1.5 :'))
    print('By: Cristian Oliveira\n')
    op = input('\nAÇÃO REMOTA\n1: CMD\n2: Abrir C:\n3: Senha\n4: Serviços\n5: Sair\n>> ').strip().lower()
    if op == '1' or op == 'cmd': #Acessar CMD remoto.
        system('mode 100,22 & cls & color 0f & title Remote Access Tool v1.5 - CMD Remoto')
        op1 = input('Método de Autenticação:\n1: Transparente.\n2: Personalizado.\n').strip().lower()
        if op1 == 'transparente' or op1 == '1': #Método Transparente.
            while op1 == 'transparente' or op1 == '1':
                pc = input('Informe o nome da máquina: ')
                system(f'psexec.exe \\\\{pc} -s cmd.exe')
                q1 = input('Deseja acessar outra máquina? (S/N): ').strip().lower()
                if q1[0] == 'n':
                    op1 = ''
        elif op1 == 'personalizado' or op1 == '2':
            u = input('Usuário: ').strip().lower()
            d = input('Domínio: ').strip().lower()
            while op1 == 'personalizado' or op1 == '2':
                pc = input('Informe o nome da máquina: ')
                system(f'psexec.exe \\\\{pc} -u {d}\\{u} cmd.exe')
                q2 = input('Deseja acessar outra máquina? {S/N): ').strip().lower()
                if q2[0] == 'n':
                    op1 = ''
    elif op == '2' or op == 'abrir c:' or op == 'c' or op == 'abrir c':
        while op == '2' or op == 'abrir c:' or op == 'c' or op == 'abrir c':
            system('mode 50,22 & cls & title Remote Access Tool v1.5 - Disco C Remoto')
            pc = input('Informe o nome da máquina: ')
            system(f'start \\\\{pc}\\c$')
            q3 = input('Deseja abrir o C de outra máquina? (S/N): ').strip().lower()
            if q3[0] == 'n':
                op = ''
    elif op == '3' or op == 'alterar senha' or op == 'senha':
        system('mode 50,22 & cls & color cf & title Remote Access Tool v1.5 - Gerenciador de Senha Remoto')
        u = input('Seu Usuário: ').strip().lower()
        d = input('Domínio: ').strip().lower()
        while op == '3' or op == 'alterar senha' or op == 'senha':
            pc = input('Informe o nome da máquina ou domínio: ').strip().lower()
            ud = input('Usuário Destino: ').strip().lower()
            pd = input('Nova Senha: ').strip()
            system(f'pspasswd.exe \\\\{pc} -u {d}\{u} {ud} {pd}')
            q4 = input('Deseja alterar outra senha? {S/N): ').lower().strip()
            if q4[0] == 'n':
                op = ''
    elif op == 'serviços' or op == 'servicos' or op == '4':
        system('mode 50,22 & title Remote Access Tool v1.5 - Gerenciador de Serviços Remoto')
        u = input('Usuário: ').strip().lower()
        d = input('Domínio: ').strip().lower()
        while op == 'serviços' or op == 'servicos' or op == '4':
            pc = input('Informe o nome do computador: ').lower().strip()
            srv = input('Ação: stop/start/restart service_name\n>> ')
            system(f'psservice.exe \\\\{pc} -u {d}\\{u} {srv}')
            q5 = input('Deseja continuar? (S/N): ').strip().lower()
            if q5[0] == 'n':
                op = ''
    elif op == '5' or op == 'sair' or op == 'exit':
        break
    else:
        print('\n')
