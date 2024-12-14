from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/section1')
def section1():
    return render_template('section1.html')

@app.route('/section2')
def section2():
    return render_template('section2.html')

@app.route('/section3')
def section3():
    return render_template('section3.html')

@app.route('/section4')
def section4():
    return render_template('section4.html')

@app.route('/section5')
def section5():
    return render_template('section5.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

with app.app_context():
    # Создаем папку для статических файлов, если она не существует
    if not os.path.exists('static_site'):
        os.makedirs('static_site')
        print("Создана папка static_site")
    else:
        print("Папка static_site уже существует")

    # Генерируем статические HTML-страницы
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods:
                url = rule.rule
                if url.endswith('/'):
                    url = url[:-1]
                filename = url.replace('/', '') or 'index'
                print(f"Генерация страницы для URL: {url}")
                with app.test_client() as client:
                    response = client.get(url)
                    if response.status_code == 200:
                        with open(f'static_site/{filename}.html', 'w', encoding='utf-8') as f:
                            f.write(response.data.decode('utf-8'))
                            print(f"Создан файл: static_site/{filename}.html")
                    else:
                        print(f"Ошибка при получении URL: {url}, статус: {response.status_code}")
