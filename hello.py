from flask import Flask, escape, request

app = Flask(__name__)

# @app.route 는 일종의 mapping이라고 할 수 있다.
# app.route('127.0.0.1:5000/')에 해당됨.
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# app.route('127.0.0.1:5000/hi')에 해당됨.
@app.route('/hi')
def hi():
    return 'hi'

@app.route('/veroroot')
def veroroot():
    return 'hello veroroot'

if __name__== '__main__' :
    app.run(debug=True)