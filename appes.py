from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd

@app.route('/', methods=['GET'])
def home():
    return render_template('squadraHome.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('squadraIns.html')

@app.route('/dati', methods=['GET'])
def dati():
    squadra = request.args['Squadra']
    data = request.args['Data di fondazione']
    citta = request.args['Citta']
    df = pd.read_csv('/workspace/flaskeserciziodbsquadre/templates/dati.csv')
    nuovi_dati = {'Squadra':squadra,'Data di fondazione':data,'Città':citta}
    df = df.append(nuovi_dati,ignore_index=True)
    df.to_csv('/workspace/flaskeserciziodbsquadre/templates/dati.csv', index=False)
    return render_template("squadraInsS.html")

@app.route('/formricerca', methods=['GET'])
def formricerca():
    return render_template("formRicerca.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
    indice = request.args["Indice"]
    radio = request.args["sel"]
    df = pd.read_csv('/workspace/flaskeserciziodbsquadre/templates/dati.csv')
    df1 = df[df[radio] == indice]
    return df1.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)
