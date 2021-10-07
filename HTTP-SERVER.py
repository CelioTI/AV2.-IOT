from http.server import BaseHTTPRequestHandler, HTTPServer
# extrai apenas BaseHTTPRequestHandler vai manipular a requisição e o  HTTPServer
#  que vai levata o servido

HOST = 'localhost'
# faz a conexão com o servidor

PORT = 5000
# porta onde o cliente vai conectar

class MyHandler(BaseHTTPRequestHandler):
# classe vai manipula as informações do cliente e vai envia os dados como respota
#     
    def do_GET(self):
        # vai trata uma requisição e entrega os dados para o destino

        self.send_response(200)
        # responde um codigo para o usuario "sucesso"

        self.send_header("Content-type", "text/html")
        #cabeçalho do protocolo HTTP (tipo do conteudo enviado)

        self.end_headers()
        #Fecha a parte do cabeçalho

        self.wfile.write(bytes("<html><head><title>AULA HTTP</title></head>","utf-8"))
        #mensagem que e enviada para o cliente

        self.wfile.write(bytes("<body>", "utf-8"))
        #mensagem que e enviada para o cliente

        self.wfile.write(bytes("<p>Servidor HTTP de exemplo. </p>", "utf-8"))
        #mensagem que e enviada para o cliente

        self.wfile.write(bytes("</body></html>", "utf-8"))
        #mensagem que e enviada para o cliente

webServer = HTTPServer((HOST,PORT), MyHandler)
#codigo que vai levanta o servidor 

print("Servidor iniciado em http://%s:%s" % (HOST, PORT))
#imprimir a URL do servido

webServer.serve_forever()
#quando for ativado começa a roda o servido