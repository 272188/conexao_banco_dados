import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost',db='POO2', user='root', passwd='root')
cursor = conexao.cursor()
#criando tabela caso ela não exista
sql = """CREATE TABLE IF NOT EXISTS usuarios_senha(id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL,senha VARCHAR(32) NOT NULL, email text Not NULL);"""

nome = 'sheila'
senha = 'root'
email = 'sheila.psb@gmail.com'

cursor.execute(sql)
#for i in range(5):
#funcao de execucao para inserir informacoes na tabela usuarios-senha
cursor.execute('INSERT INTO usuarios_senha (nome, senha, email) VALUES (%s,MD5(%s),%s)', (nome,senha,email))

#cursor.execute('SELECT * from usuarios_senha')
cursor.execute('SELECT * FROM usuarios_senha WHERE nome= %s AND senha=MD5(%s)', (nome,senha)) #funcao executar a selecao de toda tabela usuarios_senha

for c in cursor:
    print(c)

conexao.commit()
conexao.close()

