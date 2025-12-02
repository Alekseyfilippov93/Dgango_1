from flask import Flask, render_template_string
import os

# Имя HTML-файла, который нужно всегда возвращать
HTML_FILE = 'contact.html'

# Инициализация Flask
app = Flask(__name__)

# Путь к HTML-файлу
CONTACTS_PATH = os.path.join(os.path.dirname(__file__), HTML_FILE)


# Мы используем один универсальный роут, который ловит ЛЮБОЙ запрос
# и всегда возвращает contact.html.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')  # Ловит любой URL после слэша, например /hello/world
def serve_contacts(path):
    """
    Обрабатывает ЛЮБОЙ GET-запрос и возвращает содержимое contact.html.
    """

    if not os.path.exists(CONTACTS_PATH):
        return "<h1>404 Not Found</h1><p>Ошибка: Файл contact.html не найден.</p>", 404

    try:
        # Читаем содержимое файла
        with open(CONTACTS_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        return f"Ошибка 500: Не удалось прочитать файл contact.html. {e}", 500

    # Возвращаем HTML. Content-Type: text/html устанавливается автоматически.
    return render_template_string(html_content)


if __name__ == '__main__':
    print("--- Запуск Flask-сервера (Задание 2: Только Контакты) ---")
    print("Сервер всегда возвращает contact.html, независимо от URL.")
    app.run(debug=True)