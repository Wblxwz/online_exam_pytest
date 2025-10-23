import logging
import requests
import json
#import time

class User:
    def __init__(self, username, password,role,id):
        self.username = username
        self.password = password
        self.role = role
        self.id = id
        self.logger = logging.getLogger(f'{self.role}_{self.username}')
        self.logger.setLevel(logging.DEBUG)
        # handler = logging.FileHandler(f'./log/{self.role}_{time.time()}.log')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)
    def login(self):
        self.logger.info(f"{self.role} {self.username} login") 
        response = requests.get(f'http://localhost:7000/login/{self.username}/{self.password}')
        self.logger.info(response.content)
        return response
        
class Student(User):
    def __init__(self, username, password,id):
        super().__init__(username,password,'student',id)

class Teacher(User):
    def __init__(self, username, password,id):
        super().__init__(username,password,'teacher',id)
    def addClass(self):
        self.logger.info(f'{self.username} addclass')
        data = {
            "class_code": "cs", 
            "class_name": "cs222",
            "tid": self.id
        }
        response = requests.post(url='http://localhost:7000/cclass',json=data)
        self.logger.info(response.content)
        return response
class Root(User):
    def __init__(self, username, password,id):
        super().__init__(username,password,'root')