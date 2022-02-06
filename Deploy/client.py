
import requests
import json

# url local - definida no app.py - executada pelo Flask
url = 'http://127.0.0.1:5000'

# parâmetros de entrada:
classe = 1
idade = 20
qtdParentes = 2
passagem = 200


# dados da chamada ao serviço
data = {'Pclass': classe, 'Age': idade, 'SibSp': qtdParentes, 'Fare': passagem}

data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request)