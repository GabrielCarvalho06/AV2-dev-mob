from flask import Flask
from flask_cors import CORS, cross_origin
from listAlunos import list_alunos


app = Flask(__name__)
CORS(app)


# rota API
@app.route("/professores_old")
def professores_old():
    return {"professores" :["Alex", "Marcia", "Fabio"]}

@app.route("/alunos")
def alunos():
    resultado = list_alunos()
    return resultado

if __name__ == "__main__":
    app.run(debug=True)