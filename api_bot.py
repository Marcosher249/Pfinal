import requests
import json
import urllib.parse

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
            url = self.ip_port + f"bot_data/{bot}/{pair}"
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            data = {}
            print(e)
            return data  
    
    def registro(self,email,password):
        try:
            url = self.ip_port + f"{email}/{password}"
            response = requests.get(url)
            data = response.json()
            print(data)
            return data
        except Exception as e:
            data = {}
            print(e)
            return data
    def login_api(self,email,password):
        try:
            correo_encoded = urllib.parse.quote(email)
            contraseña_encoded = urllib.parse.unquote(password)
            print(correo_encoded)
            print(contraseña_encoded)
            url = self.ip_port + f"login/{correo_encoded}/{contraseña_encoded}"

            response = requests.get(url)
            data = response.json()
            
            return data
        except Exception as e:
            data = {}
            print(e)
            return data
    
     
if __name__ == "__main__":
    api = api()
    resultado = api.login_api("marcos@gmail.com","1234567")
    print(resultado)
