import socketserver
from http.server import BaseHTTPRequestHandler

# Настройки сервера
PORT = 8000
HTML_FILE_NAME = "contact.html"
HOST = ""


class ContactPageHandler(BaseHTTPRequestHandler):
    def do_get(self) -> None:
        try:
            # Читаем содержимое HTML-файла
            with open(HTML_FILE_NAME, 'r', encoding='utf-8') as file:
                content = file.read()

            # Отправляем ответ
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            encoded_content = content.encode('utf-8')
            self.send_header('Content-Length', str(len(encoded_content)))
            self.end_headers()
            self.wfile.write(encoded_content)

        except FileNotFoundError:
            self.send_error(404, f"Файл {HTML_FILE_NAME} не найден.")

        except Exception as e:
            self.send_error(500, f"Ошибка сервера: {str(e)}")


def run_server():
    server_address = (HOST, PORT)

    try:
        with socketserver.TCPServer(server_address, ContactPageHandler) as httpd:
            print(f"Сервер работает на http://localhost:{PORT}")
            print(f"Обслуживается файл: {HTML_FILE_NAME}")
            httpd.serve_forever()

    except Exception as e:
        print(f"Ошибка при запуске сервера: {str(e)}")


if __name__ == "__main__":
    run_server()
