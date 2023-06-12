import requests
import json

class api:
    def __init__(self):
        ip_port = "http://192.168.1.136:8000/"
    
    def get_bet_pair_bots(self, pair):
        try:
            url = ip_port + f"bot_data/{self.pair}"
            response = requests.get(url)
            data = requests.json()
            return data
        except Exception as e:
            data = {}
            return data

    def get_dataf_pair_bot(self,pair,bot):
        try:
            url = self.ip_port + f"bot_data/{self.bot}/{self.pair}"
            response = requests.get(url)
            data = requests.json()
            return data
        except Exception as e:
            data = {}
            return data  
    
     
    