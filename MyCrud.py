class MyCrud:
    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def criarTabela(self):
        tabela='''CREATE TABLE IF NOT EXISTS pessoas 
        (nome text not null, id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CPF INTEGER);'''
        self.cursor.execute(tabela)
        print('Tabela criada com sucesso!')

    def ler(self, id):
        leitura='SELECT * FROM pessoas WHERE id = ?'
        dados = self.cursor.execute(leitura, [id])
        print(dados.fetchall())

    def inserir(self, nome, cpf):
        insercao='INSERT INTO pessoas (nome, cpf) VALUES (?,?)'
        self.cursor.execute(insercao,[nome, cpf])
        self.conexao.commit()
        print('Salvo com sucesso.')

    def deletar(self, id):
        delet = """
            DELETE FROM pessoas
            WHERE id = ?;    
        """
        self.cursor.execute(delet, [id])
        self.conexao.commit()
        print('Deletado com sucesso!')

    def alterar(self, nome, cpf, id):
        alteracao='UPDATE pessoas SET nome = ?, cpf = ? WHERE id = ?'
        self.cursor.execute(alteracao, [nome, cpf, id])
        self.conexao.commit()
        print('Alteração executada!') 

    def fecharDB(self):
        self.conexao.close()
        print('Encerrando...')