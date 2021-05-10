from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/Dojo')
def say_dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    return f'Hi {name} '
@app.route('/repeat/<num>/<text>')
def repeat(text,num):
       return (text+' ')*int(num)
if __name__=="__main__":
    app.run(debug=True)
