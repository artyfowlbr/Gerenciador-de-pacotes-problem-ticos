import sqlite3
pedidos_db = sqlite3.connect("pedidos_db.db")
cursor = pedidos_db.cursor()
print("Conexão bem sucedida!")

# Menu inicial para gerenciar rotas
while True:
  print("----- GERENCIAR ROTAS -----")
  print("1 - Adicionar nova rota")
  print("2 - Listar rotas existentes")
  print("3 - Apagar rota")
  print("4 - Sair")
  escolha = input("O que deseja fazer? ")

  if escolha == "1": # Adicionar nova rota
    try:
      nova_rota  = input("Digite o nome da nova rota: (Formato: IMP-XX)")
      sql_insert_rota = "INSERT INTO ROTA (nome_rota) VALUES (?);"
      cursor.execute(sql_insert_rota, (nova_rota,))
      print(f"Rota {nova_rota} adicionada com sucesso!")
    except sqlite3.IntegrityError:
      print(f"ERRO: A rota '{nova_rota}' já existe. Não é possível adicionar rotas duplicadas.")
  elif escolha == "2": # Consulta para verificar as rotas existentes
    sql_select_rotas = "SELECT * FROM ROTA"
    cursor.execute(sql_select_rotas)
    rotas = cursor.fetchall()
    print("----- ROTAS EXISTENTES -----")
    for item in rotas:
      rota_ok=item[0]
      print(rota_ok)
  elif escolha == "3": # Apagar rota
    excluir= input("Digite o nome da rota a ser excluída:(Formato: IMP-XX)")
    sql_delete_rota = "DELETE FROM ROTA WHERE nome_rota = ?"
    cursor.execute(sql_delete_rota, (excluir,))
    if cursor.rowcount > 0:
      print(f"Rota {excluir} excluída com sucesso!")
    else:
      print(f"Rota {excluir} não encontrada.")
  elif escolha == "4": # Sair do menu
    print("Saindo do gerenciador de rotas.")
    break
  else:
    print("Opção inválida! Por favor, escolha 1, 2, 3 ou 4.")
  pedidos_db.commit()

pedidos_db.close()
print("Conexão encerrada.")