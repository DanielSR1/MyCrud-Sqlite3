from MyCrud import MyCrud
banco=MyCrud('moleza.db')
banco.criarTabela()
print('Vamos executar as aplicações no seu banco de dados.')
while True:
    print('''
    Digite 1 para inserir dados.
    Digite 2 para atualizar dados.
    Digite 3 para deletar.
    Digite 4 ler os dados.
    Digite 5 fechar o banco.''')
    escolha=int(input(''))
    if escolha==1:
        print('Você escolheu inserir.')
        nome=str(input('Digite o nome do usuario: '))
        cpf=str(input('Digite o cpf: '))
        cpf=f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
        banco.inserir(nome, cpf)
    elif escolha==2:
        print('Atualizar dados.')
        id=int(input('Digite o ID a ser alterado: '))
        novoNome=str(input('Digite o novo nome: '))
        novoCpf=str(input('Digite o novo cpf:' ))
        novoCpf=f'{novoCpf[:3]}.{novoCpf[3:6]}.{novoCpf[6:9]}-{novoCpf[9:11]}'
        banco.alterar(novoNome, novoCpf, id)
    elif escolha==3:
        print('Você escolheu Deletar')
        id=int(input('Digite o ID dos dados a serem deletados: '))
        banco.deletar(id)
    elif escolha==4:
        print('Você escolheu Ler.')
        id=int(input('Digite o ID para ler os dados: '))
        banco.ler(id)
    elif escolha==5:
        banco.fecharDB()
    else:
        break