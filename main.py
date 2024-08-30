repositorio = [
    {
        "matricula": 1,
        "nome": "Jonas",
        "idade": 29,
        "nota": 8.7
    }
]
matriculaAtual = 1
# menu de navegação
while True:
    print('--- BEM VINDO AO MENU ---')
    print('1 - Cadastrar aluno')
    print('2 - Listar todos')
    print('3 - Pesquisar aluno')
    print('4 - Editar aluno')
    print('5 - Excluir aluno')
    print('6 - Sair')
    opcao = input('Selecione uma opção: ')
    if opcao == '6':
        print('Você saiu do sistema...')
        break
    elif opcao == '1':
        matriculaAtual += 1
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite a idade do aluno: '))
        nota = float(input('Digite a nota do aluno: '))
        #criando um dicionário
        aluno = {
            "matricula": matriculaAtual,
            "nome": nome,
            "idade": idade,
            "nota": nota
        }
        repositorio.append(aluno)
        print('Aluno cadastrado com sucesso!')
        print(repositorio)
    elif opcao == '2':
        print('--- ALUNOS MATRICULADOS ---')
        for aluno in repositorio: #a cada volta, vai ser pegue um dicionário do repositorio
            print(f"Matricula: {aluno['matricula']}") #para apegar o valor no dicionário a sintaxe é: nome do dicionário['chave que quero acessar']
            print(f"Nome: {aluno['nome']}") # aspas duplas e simples são utilizadas para manter o conteudo dentro do outro
            print(f"Idade: {aluno['idade']}")
            print(f"Nota: {aluno['nota']}")
            print('-'*50) # Multiplica o - 50 vezes
    elif opcao == '3':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio: #percorremos a lista à procura da matrícula pesquisada
            if aluno['matricula'] == matricula: 
                print(f"Matricula: {aluno['matricula']}") 
                print(f"Nome: {aluno['nome']}") 
                print(f"Idade: {aluno['idade']}")
                print(f"Nota: {aluno['nota']}")
                print('-'*50)
                break
        else:
            print('Aluno não encontrado!')
    elif opcao == '4':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                aluno['nome'] = input('Digite o novo nome do aluno: ')
                aluno['idade'] = int(input('Digite a nova idade do aluno: '))
                aluno['nota'] = float(input('Digite a nova nota do aluno: '))
                print('Dados alterados com sucesso!')
                break
        else: #esse else não é do if, mas do for. No que chamamos de FOR-ELSE
            print('Aluno não encontrado!')
    elif opcao == '5':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                repositorio.remove(aluno)
                print('Aluno removido com sucesso')
                break
        else: 
            print('Aluno não encontrado!')