import logging
import requests
#import time

class User:
    def __init__(self, username, password,role):
        self.username = username
        self.password = password
        self.role = role
        self.logger = logging.getLogger(f'{self.role}_{self.username}')
        self.logger.setLevel(logging.INFO)
        # handler = logging.FileHandler(f'./log/{self.role}_{time.time()}.log')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)
    def login(self):
        self.logger.info(f"{self.role} {self.username} login") 
        response = requests.get(f'http://localhost:7000/login/{self.username}/{self.password}')
        self.logger.info(response.content)
        
class Student(User):
    def __init__(self, username, password):
        super().__init__(username,password,'student')

class Teacher(User):
    def __init__(self, username, password):
        super().__init__(username,password,'teacher')
    def addClass(self):
        self.logger.info(f'{self.username} addclass')
        
class Root(User):
    def __init__(self, username, password):
        super().__init__(username,password,'root')