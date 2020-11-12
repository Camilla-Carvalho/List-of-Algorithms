nome = str(input('Digite seu nome: ')).strip() # --> corta as strings, retira os espaços antes e depois
print('Analisando seu nome...')
print(f'Seu nome com leras maiúsculas é: {nome.upper()}')
print(f' Seu nome com letras minúsculas é: {nome.lower()}')
print('Seu nome tem ao todo é: ', len(nome) - nome.count(' ')) #Objetos ficam dentro dos parenteses.
#var.count() localiza um determinado comando, quando subitraímos ele no código com o conteúdo espaço dentro do
#parenteses, automaticamente, todos os espaços serão subtraídos
print('Seu primeiro nome tem: ', nome.find(' '))# é necessário o espaço dentro das aspas para que ele possa localizar