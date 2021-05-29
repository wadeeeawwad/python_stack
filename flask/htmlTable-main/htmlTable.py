from flask import Flask, render_template
app = Flask(__name__)

@app.route('/list')
def list():

    users = [
        {'first_name' : 'Rachel', 'last_name' : 'Peterson'},
        {'first_name' : 'Matthew', 'last_name' : 'Anhalt'},
        {'first_name' : 'Kilo', 'last_name' : 'Meter'},
        {'first_name' : 'Obi Wan', 'last_name' : 'Kenobi'}
    ]
    return render_template("lists.html", users = users)

if __name__=="__main__":
    app.run(debug=True)