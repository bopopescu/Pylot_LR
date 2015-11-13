from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('users')

    def index(self):
        return self.load_view('index.html')
    
    def show(self, id):
        pass

    def add(self):
        pass

    def delete(self,id):
        pass