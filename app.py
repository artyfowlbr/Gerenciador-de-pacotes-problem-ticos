import tkinter as tk
import sqlite3

#--- Funções ---

def limpar_tela(frame):
  for widget in frame_center.winfo_children():
    widget.destroy()

def mostrar_rotas(): #
  limpar_tela(frame_center)
  print("Frame central limpo")
  botao_adicionar_rota = tk.Button(frame_center, text="Adicionar Rota", command = adicionar_rota)
  botao_adicionar_rota.pack(pady=10, padx=20)

def adicionar_rota():
  janela_add_rota = tk.Toplevel()
  janela_add_rota.title("Adicionar Rota")
  janela_add_rota.geometry("300x200")
  print("Mostrando a tela para adicionar uma nova rota!")
  label_nome = tk.Label(janela_add_rota, text="Insira o nome da rota: (Ex.: IMP-XX)")
  label_nome.pack(pady=10)
  campo_nome = tk.Entry(janela_add_rota)
  campo_nome.pack(pady=5)
  #adiciona ao banco de dados 
  botao_salvar = tk.Button(janela_add_rota, text="Salvar rota", command=lambda: salvar_rota(campo_nome.get(), campo_nome))
  botao_salvar.pack(pady=10)
  botao_sair = tk.Button(janela_add_rota, text="Voltar", command=janela_add_rota.destroy)
  botao_sair.pack(pady=5)

def salvar_rota(nome_da_rota, campo_nome):
  if not nome_da_rota: # Verifica se o campo não está vazio
    print("ERRO: O nome da rota não pode estar vazio.")
    return
  
  try:
    # Conecta e salva no banco de dados
    pedidos_db = sqlite3.connect("pedidos_db.db")
    cursor = pedidos_db.cursor()    
    sql_insert_rota = "INSERT INTO ROTA (nome_rota) VALUES (?);"
    cursor.execute(sql_insert_rota, (nome_da_rota,))
    pedidos_db.commit()
    pedidos_db.close() 
    print(f"Rota '{nome_da_rota}' salva no banco de dados!")

  except sqlite3.IntegrityError:
    print(f"ERRO: A rota '{nome_da_rota}' já existe no banco de dados.")
  finally:
    if pedidos_db:
      pedidos_db.close() # Limpa o campo de entrada após salvar  
      print("Conexão com o banco de dados fechada.")
    campo_nome.delete(0, tk.END) 


#---- Configuração da Janela ----
janela = tk.Tk()
janela.title("Gerenciador de Pacotes")
janela.geometry("800x600")

#---- Interface ----
#frames
frame_left = tk.Frame(janela, width=150, bg="lightgray")
frame_center = tk.Frame(janela, bg="white")
frame_left.pack(side="left", fill="y", padx=10, pady=10)
frame_center.pack(side="left", fill="both", expand=True, padx=10, pady=10)

#frame esquerdo
botao_rotas = tk.Button(frame_left, text="Rotas", command = mostrar_rotas)
botao_rotas.pack(pady=10, padx=10)

janela.mainloop()