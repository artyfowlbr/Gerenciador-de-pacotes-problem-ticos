import sqlite3
pedidos_db = sqlite3.connect("pedidos_db.db")
print("Conexão bem sucedida!")
cursor = pedidos_db.cursor()
sql_rota = """
CREATE TABLE IF NOT EXISTS ROTA (
  nome_rota TEXT UNIQUE
  );
"""

sql_pedidos = """
CREATE TABLE IF NOT EXISTS RETIDOS (
  rastreio TEXT,
  rota TEXT,
  data_bipe DATE,
  situacao TEXT
  );
"""

cursor.execute(sql_rota)
cursor.execute(sql_pedidos)
print("Tabela RETIDOS criada com sucesso!")
print("Tabela ROTA criada com sucesso!")
# Fechando a conexão com o banco de dados
pedidos_db.close()
print("Conexão encerrada.")