import pickle
import numpy as  np
import pandas as pd
import time


class Model:
    #este é um metodo porque a def vira um metodo porque esta dentro da clase
    def __init__(self) -> None: #-> None é uma antoção
        '''
            Entrada: Dataframe
            Retorna: um diccionario da predição
            de sobrevivencia de um passageiro do TiTanic
        '''
        self.engine = pickle.load(open('../models/model.pkl','rb')) 
    
    def predict(self, data) -> dict: #-> np.ndarray: vai dizer que vai retornar um diccionario
        
        start=time.time()
        # convert data into dataframe
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)
        
        #medir o tempo de resposta
        print("tempo de conversão para dataframe: ", time.time()-start)
        # predictions
        result = self.engine.predict(data_df)
        
        # send back to browser
        output = {'results': int(result[0])}
        
        return output 