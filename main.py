from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __clients(self):
        with open("index.html", encoding="utf-8") as index_file:
            page = index_file.read()
            return page

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.__clients(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
