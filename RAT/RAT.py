from os import system
print('{:-^50}'.format(':Remote Access Tool v1.3 :'))
print('By: Cristian Oliveira\n')
op = input('Método de autenticação:\n1 - System\n2 - Personalizado\n>> ')
if op == '2':
    u = input('Usuário:\n>> ')
    p = input("Senha:\n>> ")
    d = input('Domínio:\n>> ')
    while True:
        pc = input('Informe o nome do computador.\n(DTI para Sair):\n>> ').strip().upper()
        op2 = input('1 - Abrir "C:\\" da máquina destino.\n2 - Acessar CMD da máquina destino.\n>> ')
        if op2 == '1':
            system(f'start \\\\{pc}\\c$')
            print(f'\nDisco C de {pc} está aberto em seu Windows Explorer.\n')
        elif op2 == '2':
            psexec = (f'psexec.exe \\\\{pc} -u {d}\\{u} -p {p} cmd.exe')
            if pc == 'DTI':
                break
            else:
                print('OK!')
elif op == '1':
    while True:
        pc = input('Informe o nome do computador.\n(DTI para Sair):\n>> ').strip().upper()
        op2 = input('1 - Abrir "C:\\" da máquina destino.\n2 - Acessar CMD da máquina destino.\n>> ')
        if op2 == '1':
            system(f'start \\\\{pc}\\c$')
            print(f'\nDisco C de {pc} está aberto em seu Windows Explorer.\n')
        elif op2 == '2':
            psexec = (f'psexec.exe \\\\{pc} -s cmd.exe')
            if pc == 'DTI':
                break
            else:
                print('OK!')
else:
    input('ENTER ou feche no X para sair.')