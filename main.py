while True:
  comando = input("Digite um comando (adicionar, listar, atualizar, remover, sair): ").lower()
  if comando == 'adicionar':
      titulo = input("Título do livro: ")
      autor = input("Autor do livro: ")
      ano = input("Ano de publicação: ")
      adicionar_livro(titulo, autor, ano)
  elif comando == 'listar':
      listar_livros()
  elif comando == 'atualizar':
      titulo_atual = input("Título do livro a ser atualizado: ")
      novo_titulo = input("Novo título: ")
      novo_autor = input("Novo autor: ")
      novo_ano = input("Novo ano de publicação: ")
      atualizar_livro(titulo_atual, novo_titulo, novo_autor, novo_ano)
  elif comando == 'remover':
      titulo = input("Título do livro a ser removido: ")
      remover_livro(titulo)
  elif comando == 'sair':
      break
  else:
      print("Comando não reconhecido.")
