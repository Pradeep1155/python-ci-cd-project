from flask import Flask  

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Visvasa CI/CD Flask App!"

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    return f"Result: {a + b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


