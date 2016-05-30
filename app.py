from flask import Flask
from flask import render_template
#from app import forms.NameForm
from forms import NameForm
from forms import RegisterForm

app = Flask(_name_)

app.config['SECRET_KEY'] = "Adivina adivinador"

@app.route('/')
def index():
    return render_template("index.html")
    
    
@app.route(' /form')
def formas():
    form = NameForm()
    return render_template("forma.html", form=form)
    
@app.route( '/registro', methods=['get', 'post'])
def registro():
    form = RegisterForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        print nombre
        form.nombre.data = 'Es otro german'
    return render_template
    
if_name_=="__main__":
    app.run(debug=True)
