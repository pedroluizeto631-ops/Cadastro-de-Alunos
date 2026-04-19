from time import sleep

lista_alunos = []

# ---------------- FUNÇÕES ---------------- #

def adicionar_aluno(lista):
    nome = input('Digite o nome completo do aluno: ')
    print('')
    nota1 = float(input('Digite a primeira nota do aluno no semestre -> '))
    print('')
    nota2 = float(input('Digite a segunda nota do aluno no semestre -> '))

    media = (nota1 + nota2) / 2

    aluno = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media
    }

    lista.append(aluno)
    print('Aluno cadastrado com sucesso!')


def listar_alunos(lista):
    if not lista:
        print('Nenhum aluno cadastrado!')
        return
    
    for aluno in lista:
        print(f"Nome: {aluno['nome']} | Média: {aluno['media']:.2f}")


def buscar_aluno(lista):
    nome = input('Digite o nome do aluno: ')
    
    for aluno in lista:
        if aluno["nome"].lower() == nome.lower():
            print(f"\nNome: {aluno['nome']}")
            print(f"Nota 1: {aluno['nota1']}")
            print(f"Nota 2: {aluno['nota2']}")
            print(f"Média: {aluno['media']:.2f}")
            return
    
    print("Aluno não encontrado.")


def remover_aluno(lista):
    nome = input('Digite o nome do aluno que deseja remover: ')

    for aluno in lista:
        if aluno["nome"].lower() == nome.lower():
            lista.remove(aluno)
            print('Aluno removido com sucesso!')
            return
        
    print('Aluno não encontrado')


def media_geral(lista):
    if not lista:
        print('Nenhum aluno cadastrado !')
        return
    
    soma = 0 

    for aluno in lista:
        soma += aluno['media']

    media = soma / len(lista)

    print(f'A média geral da escola: {media:.2f}')

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
[2] LISTAR TODOS OS ALUNOS
[3] BUSCAR ALUNO PELO NOME
[4] REMOVER ALUNO
[5] MOSTRAR MÉDIA GERAL DAS NOTAS
[6] SAIR
''')

    escolha = input('-> ')
    print('='*25)

    if escolha == 1:
        adicionar_aluno(lista_alunos)

    elif escolha == 2:
        listar_alunos(lista_alunos)

    elif escolha == 3:
        buscar_aluno(lista_alunos)

    elif escolha == 4:
        remover_aluno(lista_alunos)

    elif escolha == 5:
        media_geral(lista_alunos)
    
    elif escolha == 6:
        break