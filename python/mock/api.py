import requests
import time

class Api:

    def login(self, username, password):
        return 'error'

    def google(self):
        return requests.get('https://google.co.in').text

    def time(self):
        return time.time()
