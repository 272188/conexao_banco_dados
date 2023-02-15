import sqlite3

conexao = sqlite3.connect('teste.sqlite')
cursor = conexao.cursor()
#criando tabela caso ela não exista
sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY, nome text NOT NULL, email text NOT NULL);"""

nome = 'Sheila'
email = 'sheila.psb@gmail.com'

cursor.execute(sql)  #funcao para executar a conexao
for i in range(5):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?,?)', (nome, email))

cursor.execute('SELECT * from usuarios')  #seleciona toda a tabela de usuarios

for c in cursor:
    print(c)

conexao.commit()
conexao.close()  #encerra a conexao