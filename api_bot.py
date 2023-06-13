import requests
import json

class api:
    def __init__(self):
        self.ip_port = "http://192.168.1.136:8000/"
    
    def get_bet_bots(self):
        print("Se llama a la funcion de la api")
        try:
            url = self.ip_port + "bot_data/"
            response = requests.get(url)
            data = response.json()
            print(data)
            return data
        except Exception as e:
            data = {}
            print(e)
            return data

    def get_dataf_pair_bot(self,pair,bot):
        try:
            url = self.ip_port + f"bot_data/{self.bot}/{self.pair}"
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            data = {}
            print(e)
            return data  
    
     
if __name__ == "__main__":
    api = api()

    resultado = api.get_bet_bots()
    print(resultado)
