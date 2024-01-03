import sqlite3

banco = sqlite3.connect('maik_banco.db')

curso = banco.cursor()

#curso.execute("CREATE TABLE pessoas (nome text,email text,assunto text,zap integer)")

curso.execute("INSERT INTO pessoas VALUES('maik','maik123@gmail.com','oi',21993464355)")

banco.commit()
""" curso.execute("SELECT * FROM pessoas")
print(curso.fetchall())  """