from http.client import HTTPConnection
# extrai apenas HTTPConnection vai manipular a requisição e o  http.client
#  que vai levata o serviço

conexao = HTTPConnection('localhost:5000' )
#cria uma conexão no localhosta: 5000 que vai liga no http-server

conexao.request("GET", "/")
#faz uma requisição do get na raiz

resposta = conexao.getresponse()
#resposta da raiz do get

pagina = resposta.read()
# extrai os dados da respota

print (pagina)
#imprimir a resposta da pagina