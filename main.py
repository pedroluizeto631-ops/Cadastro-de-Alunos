from time import sleep

# ---------------- DADOS ---------------- #

turmas = {
    '1141': [],
    '1142': [],
    '1143': []
}

# ---------------- FUNÇÕES ---------------- #

def adicionar_aluno(turmas):
    turma = input('Digite a turma do aluno (1141, 1142, 1143) -> ')
    
    if turma not in turmas:
        print('Turma inválida!')
        return

    nome = input('Digite o nome completo do aluno: ')
    print('')
    try:
        nota1 = float(input('Digite a primeira nota do aluno no semestre -> '))
        print('')
        nota2 = float(input('Digite a segunda nota do aluno no semestre -> '))
    except ValueError:
        print('Digite apenas números válidos para as notas!')
        return

    media = (nota1 + nota2) / 2

    aluno = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media
    }

    turmas[turma].append(aluno)
    print('Aluno cadastrado com sucesso!')


def listar_alunos(turmas):
    turma = input('Digite a turma (1141, 1142, 1143) -> ')

    if turma not in turmas:
        print('Turma inválida!')
        return

    if not turmas[turma]:
        print('Nenhum aluno cadastrado nessa turma!')
        return

    print(f"\n--- Turma {turma} ---")
    for aluno in turmas[turma]:
        print(f"{aluno['nome']} | Média: {aluno['media']:.2f}")


def buscar_aluno(turmas):
    turma = input('Digite a turma do aluno (1141, 1142, 1143) -> ')
    nome = input('Digite o nome do aluno: ')
    
    if turma not in turmas:
        print('Turma inválida.')
        return
    
    if not turmas[turma]:
        print('Nenhum aluno nessa turma!')
        return
    
    for aluno in turmas[turma]:
        if aluno["nome"].lower() == nome.lower():
            print(f"\nNome: {aluno['nome']}")
            print(f"Nota 1: {aluno['nota1']}")
            print(f"Nota 2: {aluno['nota2']}")
            print(f"Média: {aluno['media']:.2f}")
            return
    
    print("Aluno não encontrado.")


def remover_aluno(turmas):
    turma = input('Digite a turma do aluno (1141, 1142, 1143) -> ')

    if turma not in turmas:
        print('Turma inválida!')
        return

    nome = input('Digite o nome do aluno que deseja remover: ')

    for aluno in turmas[turma]:
        if aluno["nome"].lower() == nome.lower():
            turmas[turma].remove(aluno)
            print('Aluno removido com sucesso!')
            return
        
    print('Aluno não encontrado nessa turma.')


def media_geral(turmas):
    total_alunos = 0
    soma = 0

    for turma in turmas.values():
        for aluno in turma:
            soma += aluno['media']
            total_alunos += 1

    if total_alunos == 0:
        print('Nenhum aluno cadastrado!')
        return

    media = soma / total_alunos
    print(f'Média geral da escola: {media:.2f}')


def mudar_turma(turmas):
    turma_origem = input('Digite a turma atual do aluno -> ')
    
    if turma_origem not in turmas:
        print('Turma inválida!')
        return

    nome = input('Digite o nome do aluno: ')

    for aluno in turmas[turma_origem]:
        if aluno['nome'].lower() == nome.lower():

            turma_destino = input('Digite a nova turma (1141, 1142, 1143) -> ')

            if turma_destino not in turmas:
                print('Turma de destino inválida!')
                return

            if turma_origem == turma_destino:
                print('O aluno já está nessa turma!')
                return

            turmas[turma_origem].remove(aluno)
            turmas[turma_destino].append(aluno)

            print('Aluno transferido com sucesso!')
            return

    print('Aluno não encontrado na turma informada.')


# ---------------- SISTEMA ---------------- #

while True:
    print('\n== CADASTRO DE ALUNOS ==')
    print('='*25)
    print('Olá, seja bem-vindo ao sistema da ETERJ...')
    print('='*25)
    sleep(1)

    print('''
Escolha o que deseja fazer:
[1] ADICIONAR ALUNO
[2] LISTAR ALUNOS POR TURMA
[3] BUSCAR ALUNO
[4] REMOVER ALUNO
[5] MÉDIA GERAL DA ESCOLA
[6] MUDAR TURMA DO ALUNO
[7] SAIR
''')

    escolha = input('-> ')

    if escolha == '1':
        adicionar_aluno(turmas)

    elif escolha == '2':
        listar_alunos(turmas)

    elif escolha == '3':
        buscar_aluno(turmas)

    elif escolha == '4':
        remover_aluno(turmas)

    elif escolha == '5':
        media_geral(turmas)

    elif escolha == '6':
        mudar_turma(turmas)

    elif escolha == '7':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida!')
