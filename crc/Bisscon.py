from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Inicio')
def Inicio():
    return render_template('Inicio.html')

@app.route('/Form_Proy')
def Form_Proy():
    return render_template('Form_Proy.html')

if __name__ == '__main__':
    app.run(debug=True)