from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html")	# notice the 2 new named arguments!


@app.route('/play/<num>')
def play_num(num):
    return render_template("index.html", num_square=int(num))
   

@app.route('/play/<num>/<color>')
def play_num_color(num,color):
    return render_template("index.html", num_square=int(num),color=color)
  



if __name__=="__main__":

    app.run(debug=True)