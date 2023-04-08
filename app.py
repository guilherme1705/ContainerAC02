from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Guilherme Augusto Alves Pereira da Silva RA: 2200977 ||||| Fabrício Nunes de Araujo RA: 2201093'