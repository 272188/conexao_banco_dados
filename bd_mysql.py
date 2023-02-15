import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost', db='POO2', user='root', passwd='root') #conexao recebe a funcao mysql conector com informacoes de localizacao, usuario e senha
cursor = conexao.cursor()

#sql cria uma tabela de usuarios
sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL,email text Not NULL);"""

nome = 'sheila'
email = 'sheila.psb@gmail.com'

cursor.execute(sql) #executando a funcao de criacao da tabela no sql
for i in range(5): #loop de execucao para inserir informacoes na tabela usuarios
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s,%s)', (nome,email))

cursor.execute('SELECT * from usuarios') #funcao de execucao que seleciona toda a tabela de usuarios

for c in cursor:  #loop para printar
    print(c)

conexao.commit()
conexao.close()  #funcao para encerrar a conexao
