import requests
import json
import urllib.parse

class api:
    def __init__(self):
        self.ip_port = "http://192.168.1.136:8000/"
    
    def get_bet_bots(self):
        try:
            url = self.ip_port + "bot_data/"
            response = requests.get(url)
            data = response.json()
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
    
    def sing_up_api(self,email,password):
        try:
            email_encoded = urllib.parse.quote(email)
            password_encoded = urllib.parse.quote(password)
            url = self.ip_port + f"sing_up/{email_encoded}/{password_encoded}"
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
            email_encoded = urllib.parse.quote(email)
            password_encoded = urllib.parse.quote(password)
            print(email_encoded)
            print(password_encoded)
            url = self.ip_port + f"login/{email_encoded}/{password_encoded}"

            response = requests.get(url)
            data = response.json()
            
            return data
        except Exception as e:
            data = {}
            print(e)
            return data
    def sell_buy(self,idUser,coin_compra,compra,coin_venta,venta):
        try:
            print(f"idU: {idUser} \nMoneda Compra:{coin_compra}\nMonto{compra}\nMoneda venta:{coin_venta}\nMonto:{venta}")
            idUser_encoded = urllib.parse.quote(idUser)
            coin_compra_encoded = urllib.parse.quote(coin_compra)
            compra_compra_encoded = urllib.parse.unquote(compra)
            coin_venta_encoded = urllib.parse.quote(coin_venta)
            venta_encoded = urllib.parse.unquote(venta)

            url = self.ip_port + f"sell_buy/{idUser_encoded}/{coin_compra_encoded}/{compra_compra_encoded}/{coin_venta_encoded}/{venta_encoded}"
            
            response = requests.get(url)
            data = response.json()
            
            return data
        except Exception as e:
            data = {"Respuesta":"no"}
            print(e)
            return data

    
     
if __name__ == "__main__":
    api = api()
    # resultado = api.sing_up_api("marcos2@gmail.com","1234567")
    resultado = api.get_bet_bots()
    print(resultado)
