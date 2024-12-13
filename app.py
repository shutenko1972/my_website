from flask import Flask, render_template
import logging

# Настройка логирования
logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.debug('Index page accessed')
    return render_template('index.html')

@app.route('/section1')
def section1():
    app.logger.debug('Section 1 page accessed')
    return render_template('section1.html')

@app.route('/section2')
def section2():
    app.logger.debug('Section 2 page accessed')
    return render_template('section2.html')

@app.route('/section3')
def section3():
    app.logger.debug('Section 3 page accessed')
    return render_template('section3.html')

@app.route('/section4')
def section4():
    app.logger.debug('Section 4 page accessed')
    return render_template('section4.html')

@app.route('/section5')
def section5():
    app.logger.debug('Section 5 page accessed')
    return render_template('section5.html')

@app.route('/about')
def about():
    app.logger.debug('About page accessed')
    return render_template('about.html')

@app.route('/hello/<name>')
def hello(name):
    app.logger.debug(f'Hello page accessed with name: {name}')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
