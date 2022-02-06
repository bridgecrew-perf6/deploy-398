import pandas as pd
from flask import Flask, jsonify, request
from model import Model
import logging 

model = Model() #tamos instnaciando minha clase Model

# app
app = Flask(__name__)

# routes 
@app.route('/', methods=['POST'])

def predict():
    try: 
        
        # get data
        data = request.get_json(force=True)
        result = model.predict(data) #atributo predict dentro de minha clase model do #arquivo model.py 
        
        #devolve o error que pode ter acontecido
        #nosso codigo funciona por isto ele é colocado como texto
        ''''print("conteudo", result)
        print("tipo", type(result))
        exit()''''
        # return data
        return jsonify(results=result) 

    except Exception as e:
        log(e) 
        
        
    
'''model = Model()
for test in teste:
    model.predict(test)'''


if __name__ == '__main__':
    app.run(port = 5000, debug=True)

