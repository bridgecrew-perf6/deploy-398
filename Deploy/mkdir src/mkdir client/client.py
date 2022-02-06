
from tracemalloc import start
import requests
import json
import time


# url local - definida no app.py - executada pelo Flask
#mesmo formato para que esta definido na notebook
url = 'http://127.0.0.1:5000'

# parâmetros de entrada:
classes = [1,2,3]
idades = [i for i in range(10,90,1)]
qtdParentes = [i for i in range(12)]
passagems = [i for i in range(30,100,50)]

for classe in classes:
    for  idade in idades:
        for parents in qtdParentes:
            for passagem in passagems:


                # dados da chamada ao serviço
                data = {'Pclass': classe, 'Age': idade, 'SibSp': parents, 'Fare': passagem}

                print({'Pclass': classe, 'Age': idade, 'SibSp': parents, 'Fare': passagem})

                data = json.dumps(data)
                start = time.time()
                send_request = requests.post(url, data)
                
                print("tempo de resposta: ", time.time()-start)
                print(send_request)
                print(send_request.json())